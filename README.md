# AI API TEMPLATE

A [Cookiecutter](https://github.com/audreyr/cookiecutter) template for exposing AI models with FastAPI.

## Usage

1. cd into the parent directory and run the following

    ```base
    cookiecutter https://github.com/phacic/ai_api_template
    ```

    It will create the app structure neccessary for exposing model through REST API

2. cd into the newly create directory and run

    ```bash
    poetry install
    ```

3. run the app with

    ```bash
    poetry shell
    python -m main
    ```

    The app should be accessible on localhost:8000


### NB

You might want the check the pyproject.toml and Dockerfile if you need other packages or customize the docker container.

## Issues

Running test with `pytest .` in the resulting app throws an error `ModuleNotFoundError: No module named 'requests'`

## Contribution
