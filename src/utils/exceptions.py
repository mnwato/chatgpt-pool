

class ServiceNotFoundError(Exception):
    def __init__(self, error_message) -> None:
        self.error_message = error_message
    
    def __str__(self):
        return self.error_message
    

class NoAvailableServiceError(Exception):
    def __init__(self) -> None:
        self.error_message = "No available service."
    
    def __str__(self):
        return self.error_message


