# flask-minio
Flask extension to interface with Minio. It has no fancy features, but just
allows you to properly interface your Flask application with the `minio` library.

## Install

You can either download the source code of this repository or install it via `pip`:

```bash
pip install Flask-Minio
```

## Usage

The simplest way to get started with this Flask extension is to pass the application
object to the `flask_minio.Minio` object. This will connect to the Minio playground
(running at `play.minio.io:9000`).

```python
from flask import Flask
from flask_minio import Minio

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
storage = Minio(app)
```

Once you've done this you're ready to spawn connections to your Minio endpoint like this:

```python
@app.route('/upload')
def upload_file():
    res = storage.connection.fput_object('maylogs', 'pumaserver_debug.log', '/tmp/pumaserver_debug.log')
```

To further customize your deployment, `flask_minio` can use the following parameters
from the application configuration:

| Variable            | Default Value                              | Description                                 |
|---------------------|--------------------------------------------|---------------------------------------------|
| `MINIO_ENDPOINT`    | `play.minio.io:9000`                       | Minio endpoint to connect to                |
| `MINIO_ACCESS_KEY`  | `Q3AM3UQ867SPQQA43P2F`                     | Access key to be used                       |
| `MINIO_SECRET_KEY`  | `zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG` | Secret key to be used                       |
| `MINIO_SECURE`      | `True`                                     | Whether to use HTTPS or not                 |
| `MINIO_REGION`      | `None`                                     | Can be something like `eu-west-1` and so on |
| `MINIO_HTTP_CLIENT` | `None`                                     | Must be a `urllib3.PoolManager` object      |
