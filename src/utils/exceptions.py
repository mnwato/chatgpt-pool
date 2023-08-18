

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


class LongPromptError(Exception):
    def __init__(self, value) -> None:
        self.value = value
        super().__init__(f"Prompt length exceeds limit: {value},  must be lower than 2500 character")