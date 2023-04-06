from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Concrete Command Classes
class CreateUserCommand(Command):
    def __init__(self, user_management, user):
        self.user_management = user_management
        self.user = user

    def execute(self):
        self.user_management.add_user(self.user)

    def undo(self):
        self.user_management.remove_user(self.user)

class SetupDatabaseCommand(Command):
    def __init__(self, database, config):
        self.database = database
        self.config = config

    def execute(self):
        self.database.setup(self.config)

    def undo(self):
        self.database.teardown()

class ConfigureApplicationCommand(Command):
    def __init__(self, application, configuration):
        self.application = application
        self.configuration = configuration

    def execute(self):
        self.application.configure(self.configuration)

    def undo(self):
        self.application.reset_configuration()

# Receiver Classes
class UserManagement:
    def add_user(self, user):
        print(f"Creating user: {user}")

    def remove_user(self, user):
        print(f"Removing user: {user}")

class Database:
    def setup(self, config):
        print(f"Setting up database with configuration: {config}")

    def teardown(self):
        print("Tearing down database")

class Application:
    def configure(self, configuration):
        print(f"Configuring application with: {configuration}")

    def reset_configuration(self):
        print("Resetting application configuration")

# Invoker Class
class Wizard:
    def __init__(self):
        self.history = []
        self.current_step = -1

    def execute_step(self, command):
        if self.current_step < len(self.history) - 1:
            self.history = self.history[:self.current_step + 1]
        command.execute()
        self.history.append(command)
        self.current_step += 1

    def undo_step(self):
        if self.current_step >= 0:
            self.history[self.current_step].undo()
            self.current_step -= 1

    def redo_step(self):
        if self.current_step < len(self.history) - 1:
            self.current_step += 1
            self.history[self.current_step].execute()

# Client Code
user_management = UserManagement()
database = Database()
application = Application()

create_user_command = CreateUserCommand(user_management, "John Doe")
setup_database_command = SetupDatabaseCommand(database, {"host": "localhost", "port": 5432})
configure_application_command = ConfigureApplicationCommand(application, {"theme": "dark"})

wizard = Wizard()

# Execute the steps in the wizard
wizard.execute_step(create_user_command)
wizard.execute_step(setup_database_command)
wizard.execute_step(configure_application_command)

# Undo the last step
wizard.undo_step()

# Redo the last step
wizard.redo_step()
