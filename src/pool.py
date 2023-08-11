import pathlib
import json
import os
import sys
import pathlib


path = pathlib.Path(__file__).parent.parent
sys.path.append(str(path))


from src.chatgpt_services.openai.official_openai import OfficialOpenai
from src.chatgpt_services.gptgo import GPTGoChatgpt
from src.chatgpt_services.easy_gpt import EasyGptChatgpt
from src.utils.exceptions import ServiceNotFoundError
from src.utils.exceptions import NoAvailableServiceError



class ChatGPTPool:
    def __init__(self) -> None:
        self.rootpath = pathlib.Path(__file__).parent.parent
        configs = self._load_config_file()
        self.services = {
            "openai": OfficialOpenai(configs),
            "gpt_go": GPTGoChatgpt(),
            "easy_gpt": EasyGptChatgpt()
        }
    
    
    def _load_config_file(self):
        path = os.path.join(self.rootpath, "model_configs.json")
        with open(path) as f:
            configs = json.load(f)
        return configs

    def find_first_availabe_service(self, prompt):
        """
            Find first available service which respons to prompt
        """
        available_service_name = None
        for k,v in self.services.items():
            try:
                service_result = v.make_request(prompt)
            except:
                continue
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



if __name__ == "__main__":
    obj = ChatGPTPool()

    prompt = "Hi"
    service_name = "gpt_go"
    result = obj.req_to_service(prompt, service_name)
    print(result)