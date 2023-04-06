class Singleton:
    # The unique instance is stored as a class attribute to be shared among all instances
    _instance = None

    @classmethod
    def getInstance(cls):
        # Check if the instance is None, meaning it hasn't been created yet
        if cls._instance is None:
            # Create the single instance and store it in the class attribute
            cls._instance = cls()
        # Return the unique instance of the class
        return cls._instance

    def __init__(self):
        # Ensure that a new instance cannot be created using the constructor
        if self._instance is not None:
            raise RuntimeError("Use getInstance() to create a new instance")


import json


class ConfigurationManager:
    _instance = None

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        if self._instance is not None:
            raise RuntimeError("Use getInstance() to create a new instance")
        self._config = None

    def load_config(self, config_file):
        with open(config_file, "r") as file:
            self._config = json.load(file)

    def get_config(self, key):
        if self._config is None:
            raise RuntimeError("Configuration has not been loaded")
        return self._config.get(key)


class MusicPlayer:
    _instance = None

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        if self._instance is not None:
            raise RuntimeError("Use getInstance() to create a new instance")
        self.state = "stopped"
        self.volume = 50

    def play(self):
        self.state = "playing"
        print("Playing music")

    def pause(self):
        self.state = "paused"
        print("Music paused")

    def set_volume(self, volume):
        if 0 <= volume <= 100:
            self.volume = volume
            print(f"Volume set to {volume}")
        else:
            print("Invalid volume level")


# Usage
player1 = MusicPlayer.getInstance()
player1.play()  # Output: Playing music
player1.set_volume(80)  # Output: Volume set to 80

player2 = MusicPlayer.getInstance()
player2.pause()  # Output: Music paused

print(player1 is player2)  # Output: True
