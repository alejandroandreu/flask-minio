import minio
from flask import current_app, _app_ctx_stack


class Minio(object):
    """This class is used to control the Minio integration to one or more Flask
    applications. Depending on how you initialize the object it is usable right
    away or will attach as needed to a Flask application.
    """

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('MINIO_ENDPOINT', 'play.minio.io:9000')
        app.config.setdefault('MINIO_ACCESS_KEY', 'Q3AM3UQ867SPQQA43P2F')
        app.config.setdefault('MINIO_SECRET_KEY', 'zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG')
        app.config.setdefault('MINIO_SECURE', True)
        app.config.setdefault('MINIO_REGION', None)
        app.config.setdefault('MINIO_HTTP_CLIENT', None)
        app.teardown_appcontext(self.teardown)

    def connect(self):
        return minio.Minio(
            current_app.config['MINIO_ENDPOINT'],
            access_key = current_app.config['MINIO_ACCESS_KEY'],
            secret_key = current_app.config['MINIO_SECRET_KEY'],
            secure = current_app.config['MINIO_SECURE'],
            region = current_app.config['MINIO_REGION'],
            http_client = current_app.config['MINIO_HTTP_CLIENT']
        )

    def teardown(self, exception):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'minio'):
            ctx.minio.close()

    @property
    def connection(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'minio'):
                ctx.minio = self.connect()
            return ctx.minio
