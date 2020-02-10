from pathlib import Path
import os

class Config(object):
    """ Default config settings """
    DEBUG = False
    TESTING = False

    SECRET_KEY = "kekoskska"

    BASE_DIR = Path.cwd()
    STATIC_DIR = Path(BASE_DIR) / "app" / "static"

    DOCUMENT_UPLOADS = Path(STATIC_DIR) / "word" / "uploads"


class DevelopmentConfig(Config):
    """ Devs settings """
    DEBUG = True


class ProductionConfig(Config):
    """ Production settings
    in this case same as default
    """
    pass