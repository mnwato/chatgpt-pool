import typing

from chatgpt_services.openai.official_openai import OfficialOpenai
from chatgpt_services.gptgo import GPTGoChatgpt
from chatgpt_services.easy_gpt import EasyGptChatgpt

from utils.exceptions import ServiceNotFoundError
from utils.exceptions import NoAvailableServiceError



class ChatGPTPool:
    def __init__(self) -> None:
        self.services = {
            "openai": OfficialOpenai(),
            "gpt_go": GPTGoChatgpt(),
            "easy_gpt": EasyGptChatgpt()
        }
    

    def find_availabe_service(self, prompt):
        """
            Find first available service which respons to prompt
        """
        available_service_name = None
        for k,v in self.services.items():
            service_result = v.make_request(prompt)
            if service_result!=None:
                available_service_name = k
                return available_service_name
        
        if available_service_name==None:
            raise NoAvailableServiceError() 
    

    def req_to_service(self, prompt, service_name):
        """
            Request to specified service
        """
        service = self.services.get(service_name)
        if service!=None:
            try:
                result = service.make_request(prompt)
                return result
            except Exception as e:
                raise e
        else:
            raise ServiceNotFoundError(service_name)


    def req_to_pool(self, prompt, service_name=None):
        """
            params:
                prompt: user prompt
                service_name: Preferred service name. Default is `None` means finding available chatgpt service to request
        """
        if service_name==None:
            available_service_name = self.find_availabe_service(prompt)
            result = self.req_to_service(prompt, available_service_name)
        else:
            result = self.req_to_service(prompt, service_name)
        return result



if __name__ == "__main__":
    obj = ChatGPTPool()

    prompt = "Hi"
    result = obj.req_to_pool(prompt)
    print(result)