import pathlib
import json
import os
import sys
import pathlib


path = pathlib.Path(__file__).parent.parent
sys.path.append(str(path))


from src.services import InstantiateServices
from src.utils.exceptions import ServiceNotFoundError
from src.utils.exceptions import NoAvailableServiceError
from src.utils.exceptions import LongPromptError



class ChatGPTPool:
    def __init__(self) -> None:
        self.services = InstantiateServices().services


    def find_first_availabe_service(self):
        """
            Find first available service which respons to prompt
        """
        available_service_name = None
        for k,v in self.services.items():
            try:
                service_result = v.make_request('Hi.')
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
        self.check_vilations(prompt, service_name)

        service = self.services.get(service_name)
        if service!=None:
            try:
                result = service.make_request(prompt)
                return result
            except Exception as e:
                raise e
        else:
            raise ServiceNotFoundError(service_name)


    def check_vilations(self, prompt, service_name):
        if service_name=='gpt_go' and len(prompt)>2500:
            raise LongPromptError(len(prompt))
        else:
            return True


if __name__ == "__main__":
    obj = ChatGPTPool()

    prompt = "Hi"
    service_name = "gpt_go"
    result = obj.req_to_service(prompt, service_name)
    print(result)