.PHONY: clean test deploy remove

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate

deploy: test
	npm install
	sls deploy

remove:
	npm install
	sls remove

test: venv
	. venv/bin/activate; python -m unittest discover --start-directory test/unit

clean:
	rm -rf venv