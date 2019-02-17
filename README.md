# Lambda JWT Authorizer

This project contains an Python implementation of an AWS
Lambda function that can be used as an authorizer with
AWS API Gateway.


## Deploying (using makefile)

A makefile has been provided to deploying the lambda
function to AWS more easily. To do this it uses the
Serverless plugin, additionally the serverless-python-requirements
plugin is used with Serverless in order to allow packaging
of the Python dependencies required for the code to run.
To deploy the function you can run:

```
make deploy
```

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
python -m unittest discover --start-directory test/unit
```

## Deactivating Virtualenv

You can deactivate the virtual env by executing
the following command:

```
deactivate
```