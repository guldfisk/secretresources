import os

import appdirs


APP_DATA_DIR = appdirs.AppDirs('secretresources', 'secretresources').user_data_dir


def project_name_to_secret_dir(name: str):
	return os.path.join(APP_DATA_DIR, name)
