from docxtpl import DocxTemplate

from secretary import Renderer


def from_template(template, context):
    engine = Renderer()

    result = engine.render(template, context=context)

    return result
