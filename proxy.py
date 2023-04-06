import random
import time
from collections import defaultdict

# HTTP request class
class HttpRequest:
    def __init__(self, ip, method, url, user_agent):
        self.ip = ip
        self.method = method
        self.url = url
        self.user_agent = user_agent

# Web server interface
class WebServer:
    def handle_request(self, request):
        pass

# Real web server
class RealWebServer(WebServer):
    def handle_request(self, request):
        print(f"Handling request from {request.ip} - {request.method} {request.url} - User Agent: {request.user_agent}")

# Firewall proxy
class FirewallProxy(WebServer):
    def __init__(self, web_server):
        self.web_server = web_server
        self.blocked_ips = {"192.168.1.2"}
        self.blocked_urls = {"/admin"}
        self.allowed_methods = {"GET", "POST"}
        self.blocked_keywords = {"forbidden"}
        self.blocked_user_agents = {"BadBot"}
        self.rate_limits = {"192.168.1.1": 3}  # Requests per second
        self.request_count = defaultdict(int)

    def handle_request(self, request):
        current_time = int(time.time())
        self.request_count[current_time] += 1

        if self.is_blocked(request):
            print(f"Blocked request from {request.ip} - {request.method} {request.url} - User Agent: {request.user_agent}")
        else:
            self.web_server.handle_request(request)

    def is_blocked(self, request):
        if request.ip in self.blocked_ips:
            return True
        if request.url in self.blocked_urls:
            return True
        if request.method not in self.allowed_methods:
            return True
        if any(keyword in request.url for keyword in self.blocked_keywords):
            return True
        if request.user_agent in self.blocked_user_agents:
            return True
        if self.is_rate_limited(request.ip):
            return True
        return False

    def is_rate_limited(self, ip):
        if ip not in self.rate_limits:
            return False
        current_time = int(time.time())
        return sum(self.request_count[i] for i in range(current_time - 1, current_time + 1)) > self.rate_limits[ip]

# Usage
real_web_server = RealWebServer()
firewall_proxy = FirewallProxy(real_web_server)

# Simulate incoming requests
ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
methods = ["GET", "POST", "PUT", "DELETE"]
urls = ["/", "/admin", "/login", "/dashboard", "/forbidden"]
user_agents = ["Mozilla/5.0", "BadBot"]

for _ in range(20):
    ip = random.choice(ips)
    method = random.choice(methods)
    url = random.choice(urls)
    user_agent = random.choice(user_agents)
    request = HttpRequest(ip, method, url, user_agent)
    firewall_proxy.handle_request(request)
    time.sleep(0.2)
