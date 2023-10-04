from os import getenv
from dotenv import load_dotenv

def get_env(env_variable):
	""" First try to get environment variables from .env file.
	If not found, get environment variables from system.
	"""

	env = getenv(env_variable)
	if env is None:
		load_dotenv()
		env = getenv(env_variable)

	return env