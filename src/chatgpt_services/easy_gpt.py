'''
	gpt-3.5-turbo
'''



from retry import retry
import requests
import json


class EasyGptApiInfo:
		chat_url = "https://www.easygpt.work/api/openai/v1/chat/completions"
		chat_headers = {
			"authority": "www.easygpt.work",
			"accept": "text/event-stream",
			"accept-language": "en-US,en;q=0.9,fa;q=0.8",
			"content-type": "application/json",
			"cookie": "Hm_lvt_563fb31e93813a8a7094966df6671d3f=1691406906; cf_clearance=6LR8Qjp_dGCv_Lk1KEJ75M8r7p0VDYdx2LXr_mTBTcE-1691407991-0-1-ea9c0475.eaf24523.bd9d5b95-0.2.1691407991; Hm_lpvt_563fb31e93813a8a7094966df6671d3f=1691408124",
			"origin": "https://www.easygpt.work",
			"plugins": "0",
			"referer": "https://www.easygpt.work/",
			"sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
			"sec-ch-ua-mobile": "?0",
			"sec-ch-ua-platform": "linux",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-site",
			"user-agent": "mozilla/5.0 (x11; linux x86_64) applewebkit/537.36 (khtml, like gecko) chrome/115.0.0.0 safari/537.36",
			"usesearch": "false",
			"x-requested-with": "XMLHttpRequest"
			}
		temprature = 0.5
		presence_penalty = 0
		frequency_penalty = 0
		top_p = 1
		stream = True


class EasyGptChatgpt:
	def __init__(self) -> None:
		self.easy_gpt = EasyGptApiInfo()
		self.s = requests.Session()


	def create_body(self, prompt):
		body = {
			"messages": [
				{
				"role": "system",
				"content": "\nYou are ChatGPT, a large language model trained by OpenAI.\nKnowledge cutoff: 2021-09\nCurrent model: gpt-3.5-turbo."
				},
				{
				"role": "user",
				"content": prompt
				}
			],
			"stream": self.easy_gpt.stream,
			"model": "gpt-3.5-turbo",
			"temperature": self.easy_gpt.temprature,
			"presence_penalty": self.easy_gpt.presence_penalty,
			"frequency_penalty": self.easy_gpt.frequency_penalty,
			"top_p": self.easy_gpt.top_p
			}

		return body


	# @retry(tries=2, delay=5)
	def chat(self, body):
		try:
			res = self.s.post(self.easy_gpt.chat_url, json=body, headers=self.easy_gpt.chat_headers, stream=False)
			if res.status_code == 200:
				result = list()
				for line in res.iter_lines(decode_unicode=True):
					if line:
						line = line.replace('data: ', '')
						if line:  # Non-empty line
							try:
								data = json.loads(line)
								tmp = data.get('choices', [{"delta":{"content": ""}}])[0].get('delta', {"content": ""}).get("content")
								result.append(tmp)
							except json.JSONDecodeError as e:
								continue
				result = ''.join([x for x in result if x not in ['', None, '[DONE]']])
				return result
			else:
				raise Exception(f"Status code: {res.status_code}")
		except Exception as e:
			raise e



	def get_response(self, prompt):
		body = self.create_body(prompt)
		result = self.chat(body)
		if result:
			return result
		else:
			return None



if __name__ == "__main__":
	obj = EasyGptChatgpt()

	prompt = "what time is it in tehran?"
	prompt = "Where could i find best samsung mobile phone?"
	res = obj.make_req(prompt)
	print(res)
