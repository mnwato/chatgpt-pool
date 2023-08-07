import tiktoken
import pathlib
import pickle
import os
import sys


datapath = os.path.join(os.getcwd(), 'openai', 'data')

def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301"):
	"""Returns the number of tokens used by a list of messages."""
	try:
		encoding_model = load_encoding_model()
		if encoding_model != None:
			encoding = encoding_model
		else:
			encoding = tiktoken.encoding_for_model(model)
			# save_encoding_model(encoding)
	except KeyError:
		encoding = tiktoken.get_encoding("cl100k_base")
	if model == "gpt-3.5-turbo-0301":  # note: future models may deviate from this
		num_tokens = 0
		for message in messages:
			# every message follows <im_start>{role/name}\n{content}<im_end>\n
			num_tokens += 4
			for key, value in message.items():
				num_tokens += len(encoding.encode(value))
				if key == "name":  # if there's a name, the role is omitted
					num_tokens += -1  # role is always required and always 1 token
		num_tokens += 2  # every reply is primed with <im_start>assistant
		return num_tokens
	else:
		raise NotImplementedError(f"""num_tokens_from_messages() is not presently implemented for model {model}.
  See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")


def load_encoding_model():
	try:
		encoding_model_name = "cl100k_base_encoding_model.pkl"
		encoding_model_path = pathlib.Path(os.path.join(datapath, encoding_model_name))
		if os.path.exists(encoding_model_path):
			with open(encoding_model_path, 'rb') as f:
				encoding_model = pickle.load(f)
			return encoding_model
		else:
			return None
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		extra_msg = {
			"last_exec_line": str(exc_tb.tb_lineno),
			"error_message": str(e),
		}
		print(extra_msg)
		return None
	

def save_encoding_model(encoding_model):
	try:
		encoding_model_name = "cl100k_base_encoding_model.pkl"
		encoding_model_path = pathlib.Path(os.path.join(datapath, encoding_model_name))
		with open(encoding_model_path, 'wb') as f:
			pickle.dump(encoding_model, f)
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		extra_msg = {
			"last_exec_line": str(exc_tb.tb_lineno),
			"error_message": str(e),
		}
		print(extra_msg)