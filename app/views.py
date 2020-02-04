from flask import render_template, request, send_file, url_for

import io

from app import app

from app import generate


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/title_curse", methods=["GET", "POST"])
def title_curse():
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
    return render_template("curse.html")

@app.route("/title_ref", methods=["GET", "POST"])
def title_ref():
    template = 'app/static/word/titul_ref.odt'

    if request.method == "POST":
        context = request.form

        document = generate.from_template(template, context=context)

        try:
            return send_file(
                io.BytesIO(document), mimetype='application/vnd.oasis.opendocument.text',
                as_attachment=True, attachment_filename='титульник_реф.odt'
            )
        except Exception as e:
            print(e)
    return render_template("ref.html")
