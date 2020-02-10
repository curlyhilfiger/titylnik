""" Service which delete downloaded file """

from pathlib import Path

from app import app


def delete(document_name):
    """ Delete document

    Takes a string that represents 
    the file name with the extension

    Returns nothing
    """
    file_to_rem = Path(app.config["DOCUMENT_UPLOADS"]) / document_name
    file_to_rem.unlink()
