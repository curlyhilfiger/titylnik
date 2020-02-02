from docxtpl import DocxTemplate

from secretary import Renderer


def from_template(template, context):
    engine = Renderer()

    result = engine.render('app/static/word/title.odt', context=context)

    return result
