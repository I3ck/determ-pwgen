import hashlib, base64

class DetermPwgen:

	def __init__(self, seed):
		self._seed = seed

	def generate_password(self, hostname, username, rounds):
		pw = self._seed + hostname + username

		for i in range(rounds):
			pw = base64.b64encode((hashlib.sha256(pw).digest()))

		return pw