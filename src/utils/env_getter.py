from dotenv import load_dotenv, find_dotenv
import os


class EnvGetter:
    def __init__(self) -> None:
        load_dotenv(find_dotenv())
        self._define_env_variables()


    def _define_env_variables(self):
        self.env_variables = dict()        
        self.env_variables["OPENAI_API_KEY"] = self.get_env_variable("OPENAI_API_KEY")
        self.env_variables["OPENAI_ORG_KEY"] =  self.get_env_variable("OPENAI_ORG_KEY")


    def get_env_variable(self, var_name, default=None):
        value = os.environ.get(var_name)
        if value:
            return value
        if default:
            return default
        raise Exception("{} env variable doesnt exists".format(var_name))