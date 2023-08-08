import time

from src.chatgpt_services.openai.token_counter import num_tokens_from_messages
	

def check_rpm_limit(rpm_limit, tpm_limit, start_time):
	elapsed_time = time.time() - start_time
	if elapsed_time<60 and (rpm_limit>=19 or tpm_limit>=39000):
		print('-- RPM limit reached!')
		print('		wait for 1min!')
		time.sleep(60)
		return False
	else:
		return True


def check_input_tokens_limit(messages):
	input_token_counts = num_tokens_from_messages(messages)
	if input_token_counts>=4090:
		print('-- message tokens was > 4096. please send shorter message.')
		return True
	else:
		False