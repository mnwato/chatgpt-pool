import pathlib
import json
import os

from src.chatgpt_services.openai.official_openai import OfficialOpenai
from src.chatgpt_services.gptgo import GPTGoChatgpt
from src.chatgpt_services.easy_gpt import EasyGptChatgpt
from src.chatgpt_services.p5_v50 import P5V50Chatgpt



class InstantiateServices:
    def __init__(self) -> None:
        self.rootpath = pathlib.Path(__file__).parent.parent
        configs = self._load_config_file()
        self.init_services(configs)

    
    def _load_config_file(self):
        path = os.path.join(self.rootpath, "model_configs.json")
        with open(path) as f:
            configs = json.load(f)
        return configs


    def init_services(self, configs):
        self.services = {
            "openai": OfficialOpenai(configs),
            "gpt_go": GPTGoChatgpt(),
            "easy_gpt": EasyGptChatgpt(),
            "p5_v50": P5V50Chatgpt(configs)
            }