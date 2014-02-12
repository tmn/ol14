run:
    PYTHONPATH=$(shell pwd) venv/bin/python olympics/Olympics.py

test:
	PYTHONPATH=$(shell pwd) venv/bin/python coffee/tests.py

update:
	git fetch && git reset --hard origin/master
	venv/bin/pip install -r requirements.txt