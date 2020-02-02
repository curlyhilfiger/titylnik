from flask import render_template, request, send_file, url_for

import io

from app import app

from app import generate

@app.route("/", methods=["GET", "POST"])
def index():
    template = 'app/static/word/title.odt'

    if request.method == "POST":
        context = request.form

        print(context)

        document = generate.from_template(template, context=context)

        try:
            return send_file(
                io.BytesIO(document), mimetype='application/vnd.oasis.opendocument.text',
                as_attachment=True, attachment_filename='титульник.odt'
            )
        except Exception as e:
            print(e)
    return render_template("index.html")
