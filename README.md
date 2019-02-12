# Basic Python Unit Tests

This is a very noddy project with an example of some
unit tests that test some code that uses an published
python package

## Running the tests (using makefile)

A makefile has been provided to make running the tests
more simple, to use this can you running the following
command:

```
make test
```

The steps performed by this make file are explained below.

## Environment Set Up

You can activate the virtual env to isolate the packages
required to run this code by executing the following
command:

```
source venv/bin/activate
```

You can then install the required packages by executing
the following command:

```
pip install -r requirements.txt
```

## Running the Tests

Once the environment has been set up you can run the
tests by executing the following command:

```
python -m unittest discover --start-directory unit-test
```

## Deactivating Virtualenv

You can deactivate the virtual env by executing
the following command:

```
deactivate
```