import secrets


class Config(object):
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = "mysql://recep:Recep123*@localhost/deneme"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
