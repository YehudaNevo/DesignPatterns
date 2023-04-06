import random
import time

# Simple Observer Interface
class ProgressListener:
    def on_progress(self, percentage):
        pass

# Concrete Progress Listeners
class ProgressBar(ProgressListener):
    def on_progress(self, percentage):
        print(f"Progress Bar: {percentage}%")

class ProgressLabel(ProgressListener):
    def on_progress(self, percentage):
        print(f"Download progress: {percentage}%")

# Subject: Downloader
class FileDownloader:
    def __init__(self):
        self.listeners = []

    def add_progress_listener(self, listener):
        self.listeners.append(listener)

    def remove_progress_listener(self, listener):
        self.listeners.remove(listener)

    def _update_progress(self, percentage):
        for listener in self.listeners:
            listener.on_progress(percentage)

    def download_file(self, url):
        print(f"Downloading file from {url}")
        for i in range(0, 101, random.randint(1, 25)):
            self._update_progress(i)
            time.sleep(0.5)
        print("Download complete!")

# Usage
downloader = FileDownloader()

progress_bar = ProgressBar()
progress_label = ProgressLabel()

downloader.add_progress_listener(progress_bar)
downloader.add_progress_listener(progress_label)

downloader.download_file("https://example.com/file.zip")

# Sample Output:
# Downloading file from https://example.com/file.zip
# Progress Bar: 0%
# Download progress: 0%
# Progress Bar: 5%
# Download progress: 5%
# Progress Bar: 30%
# Download progress: 30%
# ...
# Download complete!
