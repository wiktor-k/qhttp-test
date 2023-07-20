# QHttpServer test

Example project illustrating problems when testing QHttpServer.

To run:

```sh
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
PYTEST_ADDOPTS=--verbose pytest -s
```

The test will never complete and the response will never arrive.

Now test it manually by running:

```sh
python main.py
```

Clicking a button and in another terminal:

```sh
curl localhost:19841
```

It should correctly print `response`.
