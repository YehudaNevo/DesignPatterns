from abc import ABC, abstractmethod
import datetime

# Mediator Interface
class ApiMediator(ABC):
    @abstractmethod
    def process_request(self, request, client):
        pass

# Concrete Mediator
class ApiManager(ApiMediator):
    def __init__(self):
        self.clients = {}
        self.services = {}
        self.logs = []

    def register_client(self, client, api_key):
        self.clients[api_key] = client

    def register_service(self, name, service):
        self.services[name] = service

    def log_request(self, request):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.logs.append({"timestamp": timestamp, "request": request})
        print(f"Logged request: {timestamp} - {request}")

    def process_request(self, request, api_key):
        if api_key not in self.clients:
            print(f"Unauthorized request with API key {api_key}")
            return

        client = self.clients[api_key]

        service_name = request["service"]
        if service_name not in self.services:
            print(f"Service '{service_name}' not found")
            return

        self.log_request(request)

        service = self.services[service_name]
        response = service.process_request(request)
        client.process_response(response)

# Colleague Interfaces
class ApiClient(ABC):
    @abstractmethod
    def process_response(self, response):
        pass

class ApiService(ABC):
    @abstractmethod
    def process_request(self, request):
        pass

# Concrete Colleagues
class Client(ApiClient):
    def __init__(self, name, mediator, api_key):
        self.name = name
        self.mediator = mediator
        self.api_key = api_key

    def send_request(self, request):
        print(f"Client {self.name} sends request for {request['service']} service")
        self.mediator.process_request(request, self.api_key)

    def process_response(self, response):
        print(f"Client {self.name} receives response: {response}")

class Service(ApiService):
    def __init__(self, name):
        self.name = name

    def process_request(self, request):
        print(f"Service {self.name} processes request")
        return f"Response from {self.name} service"

# Client Code
api_manager = ApiManager()

client1 = Client("Client1", api_manager, "API_KEY_1")
client2 = Client("Client2", api_manager, "API_KEY_2")

service1 = Service("Service1")
service2 = Service("Service2")

api_manager.register_client(client1, "API_KEY_1")
api_manager.register_client(client2, "API_KEY_2")
api_manager.register_service("Service1", service1)
api_manager.register_service("Service2", service2)

client1.send_request({"service": "Service1"})
client2.send_request({"service": "Service2"})
client1.send_request({"service": "Service2", "invalid_api_key": "INVALID_KEY"})
