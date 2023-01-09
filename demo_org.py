def make_file_accessible(self, file_path: str, file_name: str, user: str) -> str:
		"""
		allow all permissions to the given user for the given file
		"""
		full_path = os.path.join(file_path, file_name)
		os.system(f'sudo chown {user}: {full_path}')
		return full_path