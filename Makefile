all: requirements.txt
	pip-sync

requirements.txt: requirements.in
	pip-compile


