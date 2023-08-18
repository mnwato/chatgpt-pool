
import requests


class P5V50ApiInfo:
		chat_url = "https://p5.v50.ltd/api/chat-process"
		chat_headers = {
			"authority": "p5.v50.ltd",
			"accept": "application/json, text/plain, */*'",
			"accept-language": "en-us,en;q=0.9,fa;q=0.8",
			"content-type": "application/json",
			"origin": "https://p5.v50.ltd",
			"referer": "https://p5.v50.ltd/",
			"sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
			"sec-ch-ua-mobile": "?0",
			"sec-ch-ua-platform": "linux",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "cross-site",
			"user-agent": "mozilla/5.0 (x11; linux x86_64) applewebkit/537.36 (khtml, like gecko) chrome/115.0.0.0 safari/537.36"
			}


class P5V50Chatgpt:
	def __init__(self, configs) -> None:
		configs = configs['p5_v50']
		self.model = configs['model']
		self.temperature = configs['temperature']
		self.p5_v5 = P5V50ApiInfo()
		self.s = requests.Session()


	def create_body(self, prompt):
		body = {
			"prompt": prompt,
			"options": {},
			"systemMessage": ".",
			"temperature": self.temperature,
			"top_p": 1,
			"model": self.model,
			"user": None
		}
		return body
	

	def chat(self, prompt):
		try:
			body = self.create_body(prompt)
			res = self.s.post(self.p5_v5.chat_url, headers=self.p5_v5.chat_headers, json=body)
			if res.status_code == 200:
				if res.text and res.text not in ['', ' ']:
					return res.text
			else:
				raise Exception(f"Status code: {res.status_code}")
		except Exception as e:
			print(e)
			return None


	def make_request(self, prompt):
		result = self.chat(prompt)
		return result



if __name__ == "__main__":
	obj = P5V50Chatgpt()

	prompt = "hi"
	res = obj.make_request(prompt)
	print(res)
