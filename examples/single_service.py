import pathlib
import sys

path = pathlib.Path(__file__).parent.parent
sys.path.append(str(path))

from src.pool import ChatGPTPool

obj = ChatGPTPool()

text = "Hi"
service_name = "gpt_go"

result = obj.req_to_service(prompt=text, service_name=service_name)


print(result)