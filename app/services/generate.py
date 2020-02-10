""" Service that generates 
a document according to a ready template

Uses a secretary package and pypandoc
"""

from pathlib import Path
from secretary import Renderer
import pypandoc

from app import app


def from_template(template, context):
    """ Generates odt file
    template - string path to odt template 
    context - context variables like in Jinja2
    """

    engine = Renderer()

    result = engine.render(template, context=context)

    return result

def html_to_format(html, format, filename):
    """ Generates odt file from html
    html - raw html string
    format - convert format(maybe later, just now only odt)
    filename - file location
    """

    output_file = str(Path(app.config["DOCUMENT_UPLOADS"])) + f'\\{filename}.odt'

    pypandoc.convert(html, 'odt', format='html', outputfile=output_file)
