from flask import Flask
from flask_minio import Minio

app = Flask('test_basic')
minio = Minio(app)

def test_minio_init():
    assert minio.app.config['MINIO_ENDPOINT'] == 'play.minio.io:9000'
