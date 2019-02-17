.PHONY: clean test deploy

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate

deploy: test
	npm install
	serverless deploy

test: venv
	. venv/bin/activate; python -m unittest discover --start-directory test/unit

clean:
	rm -rf venv