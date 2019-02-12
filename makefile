venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate

test: venv
	. venv/bin/activate; python -m unittest discover --start-directory unit-test

clean:
	rm -rf venv