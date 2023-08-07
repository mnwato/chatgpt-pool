
from retry import retry
import requests
import json


class GPTGoApiInfo:
		token_url = "https://gptgo.ai/action_get_token.php?q={}&hlgpt=default&hl=en"
		token_header = {
			"authority": "gptgo.ai",
			"accept": "*/*",
			"accept-language": "en-US,en;q=0.9,fa;q=0.8",
			"cookie": "__gads=ID=c7fc2d846c4d6707:T=1691399052:RT=1691399052:S=ALNI_MbaDhKBe0-SCwj9RGlDy-rjg7U_WQ; __gpi=UID=00000c7a1f1c431c:T=1691399052:RT=1691399052:S=ALNI_MbzVeEeF9hyj1dCvbQ_WbZe-nrUOw; __cflb=0H28vyAds12gjjCbfLnww9BRakymDKbjqQMB9aPnv3m; _cfuvid=eBOZh.snvDwCQHXlIFb7BKqpU3hE_Ul8ZdRyQZ.ReQw-1691399065764-0-604800000; _ga=GA1.1.1253448084.1691399067; _pbjs_userid_consent_data=3524755945110770; _pubcid=a67c4b37-9bc3-4d4b-86e0-85362b440704; cto_bundle=HMPJgF9yTkglMkJwajk2Zm4lMkJ0VG1KMXQxRHd6aWhSY242b3ZsJTJCWVdQTTNBTEQ4VzdZR2JRZjNwaEVpWCUyRkFPeTdjR08lMkZCUHlGdEJoM3ZFYXUlMkJqVW1vaGI0ZCUyQnBiUFozUFdGdUVHbHBhUkxLRDZGVUVFWTF5MEtOaWNrMnBpWEVjdyUyQmtZUWo; cto_bidid=9KZf-V90c3VHNWh1QSUyRk5nQThWMlFMUSUyRjlYdHZFMHBiMkdkcWRySGQ2d3lZOGRmM1dxWHdXcGpXZ2JFa25OVzFjQjhPQk9QMGtFMEJyNVFOVDNydnBOajk0NEElM0QlM0Q; FCNEC=%5B%5B%22AKsRol_8_R7AhcHkSJ61sHxss1Zz-58vGywugGOIb04_ZHjQm0ofNGoE-KTH8zrvLiWvNKsNeHc7xeZVkaITcJL9kAadhhMbR1IYb5YDecwHRohphW3fp_bbcrtetWcj2ZZvf3qWgkNBpBGUqy_1MeUrVH3QwQYHjA%3D%3D%22%5D%2Cnull%2C%5B%5D%5D; __jscuActive=true; _ga_79DKXDR85G=GS1.1.1691399066.1.0.1691399157.0.0.0",
			"referer": "https://gptgo.ai/?hl=en",
			"sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
			"sec-ch-ua-mobile": "?0",
			"sec-ch-ua-platform": "linux",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-site",
			"user-agent": "mozilla/5.0 (x11; linux x86_64) applewebkit/537.36 (khtml, like gecko) chrome/115.0.0.0 safari/537.36"
			}

		sug_url = "https://gptgo.ai/sug.php?token={}"
		sug_header = {
			"authority": "gptgo.ai",
			"accept": "*/*",
			"accept-language": "en-us,en;q=0.9,fa;q=0.8",
			"cache-control": "no-cache",
			"cookie": "__cflb=0H28vyAds12gjjCbfLnww9BRakymDKbjqQMB9aPnv3m; _cfuvid=eBOZh.snvDwCQHXlIFb7BKqpU3hE_Ul8ZdRyQZ.ReQw-1691399065764-0-604800000; _ga=GA1.1.1253448084.1691399067; _pbjs_userid_consent_data=3524755945110770; _pubcid=a67c4b37-9bc3-4d4b-86e0-85362b440704; cto_bundle=HMPJgF9yTkglMkJwajk2Zm4lMkJ0VG1KMXQxRHd6aWhSY242b3ZsJTJCWVdQTTNBTEQ4VzdZR2JRZjNwaEVpWCUyRkFPeTdjR08lMkZCUHlGdEJoM3ZFYXUlMkJqVW1vaGI0ZCUyQnBiUFozUFdGdUVHbHBhUkxLRDZGVUVFWTF5MEtOaWNrMnBpWEVjdyUyQmtZUWo; cto_bidid=9KZf-V90c3VHNWh1QSUyRk5nQThWMlFMUSUyRjlYdHZFMHBiMkdkcWRySGQ2d3lZOGRmM1dxWHdXcGpXZ2JFa25OVzFjQjhPQk9QMGtFMEJyNVFOVDNydnBOajk0NEElM0QlM0Q; FCNEC=%5B%5B%22AKsRol_8_R7AhcHkSJ61sHxss1Zz-58vGywugGOIb04_ZHjQm0ofNGoE-KTH8zrvLiWvNKsNeHc7xeZVkaITcJL9kAadhhMbR1IYb5YDecwHRohphW3fp_bbcrtetWcj2ZZvf3qWgkNBpBGUqy_1MeUrVH3QwQYHjA%3D%3D%22%5D%2Cnull%2C%5B%5D%5D; __jscuActive=true; __gads=ID=c7fc2d846c4d6707:T=1691399052:RT=1691399671:S=ALNI_MbaDhKBe0-SCwj9RGlDy-rjg7U_WQ; __gpi=UID=00000c7a1f1c431c:T=1691399052:RT=1691399671:S=ALNI_MbzVeEeF9hyj1dCvbQ_WbZe-nrUOw; _ga_79DKXDR85G=GS1.1.1691399066.1.1.1691399904.0.0.0",
			"referer": "https://gptgo.ai/?hl=en",
			"sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
			"sec-ch-ua-mobile": "?0",
			"sec-ch-ua-platform": "linux",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-site",
			"user-agent": "mozilla/5.0 (x11; linux x86_64) applewebkit/537.36 (khtml, like gecko) chrome/115.0.0.0 safari/537.36"
			}
		
		chat_url = "https://gptgo.ai/action_ai_gpt.php?token={}"
		chat_headers = {
			"authority": "gptgo.ai",
			"accept": "text/event-stream",
			"accept-language": "en-us,en;q=0.9,fa;q=0.8",
			"cache-control": "no-cache",
			"referer": "https://gptgo.ai/?hl=vi",
			"sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
			"sec-ch-ua-mobile": "?0",
			"sec-ch-ua-platform": "linux",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "cross-site",
			"user-agent": "mozilla/5.0 (x11; linux x86_64) applewebkit/537.36 (khtml, like gecko) chrome/115.0.0.0 safari/537.36",
			"x-signature": "e135078028ee88749a25f9f5afcee2e75185edeaa48a24d4ae1d663ae130bd95453a8ec32d8ea5df8b9fa298595c5ee00011f593a2c0acfcf2ca9c28d4eb4b27"
			}


class GPTGoChatgpt:
	def __init__(self) -> None:
		self.gpt_go = GPTGoApiInfo()
		self.s = requests.Session()

	
	def get_token(self, prompt):
		try:
			res = self.s.get(self.gpt_go.token_url.format(prompt), headers=self.gpt_go.token_header)
			if res.status_code == 200:
				res_text = res.text
				try:
					if json.loads(res_text).get('status')==True:
						res_json = json.loads(res_text)
					else:
						res_json = None
				except Exception as e:
					print(e)

				if res_json!=None:
					result = res_json.get('token')
					return result
				else:
					return None
				
			else:
				raise Exception(f"Status code: {res.status_code}")
			
		except Exception as e:
			raise e


	def req_sug(self, token):
		try:
			res = self.s.get(self.gpt_go.sug_url.format(token), headers=self.gpt_go.sug_header)
			if res.status_code == 200:
				res_text = res.text
				return res_text
			else:
				raise Exception(f"Status code: {res.status_code}")
		except Exception as e:
			raise e
	

	# @retry(tries=2, delay=5)
	def chat(self, token):
		try:
			res = self.s.get(self.gpt_go.chat_url.format(token), headers=self.gpt_go.chat_headers, stream=True)
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



	def make_request(self, prompt):
		token = self.get_token(prompt)
		if token!=None:
			self.req_sug(token)
			result = self.chat(token)
			return result
		else:
			print('-- token is None')



if __name__ == "__main__":
	obj = GPTGoChatgpt()

	prompt = "what time is it in tehran?"
	res = obj.make_req(prompt)
	print(res)
