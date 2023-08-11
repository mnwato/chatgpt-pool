import pathlib
import sys

path = pathlib.Path(__file__).parent.parent
sys.path.append(str(path))

from src.pool import ChatGPTPool



obj = ChatGPTPool()


text = "Hi"
available_service_name = obj.find_first_availabe_service(prompt=text)


print(available_service_name)