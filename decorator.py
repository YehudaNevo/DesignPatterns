from abc import ABC, abstractmethod

# Component Interface
class ApiService(ABC):
    @abstractmethod
    def get_data(self, user_id):
        pass

# Concrete Component (API v1)
class ApiServiceV1(ApiService):
    def get_data(self, user_id):
        return {"id": user_id, "name": "John Doe", "email": "john.doe@example.com"}

# Decorator Base Class
class ApiDecorator(ApiService):
    def __init__(self, api_service):
        self.api_service = api_service

    def get_data(self, user_id):
        return self.api_service.get_data(user_id)

# Concrete Decorator (API v2)
class ApiServiceV2(ApiDecorator):
    def get_data(self, user_id):
        data = super().get_data(user_id)
        data["phone"] = "123-456-7890"  # Added a new field
        return data

# Concrete Decorator (API v3)
class ApiServiceV3(ApiDecorator):
    def get_data(self, user_id):
        data = super().get_data(user_id)
        del data["email"]  # Removed a field
        data["address"] = "123 Main St"  # Added a new field
        return data

# Usage
api_v1 = ApiServiceV1()
print("API v1:", api_v1.get_data(1))

api_v2 = ApiServiceV2(api_v1)
print("API v2:", api_v2.get_data(1))

api_v3 = ApiServiceV3(api_v2)
print("API v3:", api_v3.get_data(1))

