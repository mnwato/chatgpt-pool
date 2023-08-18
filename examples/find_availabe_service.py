import pathlib
import sys

path = pathlib.Path(__file__).parent.parent
sys.path.append(str(path))

from src.pool import ChatGPTPool



obj = ChatGPTPool()


available_service_name = obj.find_first_availabe_service()


print(available_service_name)