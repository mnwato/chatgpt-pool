
from retry import retry
import openai
import time
import sys
import pathlib


path = pathlib.Path(__file__).parent.parent.parent.parent
sys.path.append(str(path))

from src.chatgpt_services.openai.utils import check_input_tokens_limit, check_rpm_limit
from src.utils.env_getter import EnvGetter




class OfficialOpenai:
	def __init__(self) -> None:
		api_key = ""
		openai.organization = ""
		openai.api_key = api_key
		self.prefered_model = "gpt-3.5-turbo-0301"
		self.prefered_model = "gpt-3.5-turbo"
		self.models = openai.Model.list()




	def create_simple_body(self, prompt):
		body = {
			"role": 'user',
			"content": prompt,
		}
		return [body]



	# @retry(tries=2, delay=5)
	def make_request(self, prompt):
		start_time = time.time()
		tpm_limit = 0
		rpm_limit = 0

		try:
			if not check_rpm_limit(rpm_limit, tpm_limit, start_time):
				start_time = time.time()

			messages = self.create_simple_body(prompt)
			if check_input_tokens_limit(messages):
				return False

			completion = openai.ChatCompletion.create(model=self.prefered_model, messages=messages)
			result = completion['choices'][0]['message']

			rpm_limit+=1
			tpm_limit += completion['usage']['total_tokens']

			return result
		
		except Exception as e:
			raise e
		
		


if __name__ == "__main__":
	obj = OfficialOpenai()

	prompt = "Hi"
	res = obj.get_response(prompt)
	print(res)