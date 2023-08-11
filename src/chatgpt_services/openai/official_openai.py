
import openai
import time


from src.chatgpt_services.openai.utils import check_input_tokens_limit, check_rpm_limit




class OfficialOpenai:
	def __init__(self, configs) -> None:
		configs = configs["openai"]
		openai.api_key = configs["OPENAI_API_KEY"]
		openai.organization = configs["OPENAI_ORG_KEY"]
		self.prefered_model = configs["OPENAI_Model_Name"]




	def create_simple_body(self, prompt):
		body = {
			"role": 'user',
			"content": prompt,
		}
		return [body]



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