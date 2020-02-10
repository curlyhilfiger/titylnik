from flask import (render_template, request, send_file, url_for,
    send_from_directory, after_this_request, redirect, jsonify)

import io, os

from app import app
from app.services import generate, delete_file


@app.route("/")
def index():
    """ Index page """
    print(app.config["DOCUMENT_UPLOADS"])
    return render_template("index.html")

@app.route("/title_curse", methods=["GET", "POST"])
def title_curse():
    """ Generate title page from form
    and returns odt file
    """

    template = "app/static/word/title.odt"

    if request.method == "POST":
        context = request.form

        print(context)

        document = generate.from_template(template, context=context)

        try:
            return send_file(
                io.BytesIO(document), mimetype="application/vnd.oasis.opendocument.text",
                as_attachment=True, attachment_filename="титульник.odt"
            )
        except Exception as e:
            print(e)

    return render_template("curse.html")

@app.route("/title_ref", methods=["GET", "POST"])
def title_ref():
    """ Title page for essay and return odt """

    template = "app/static/word/titul_ref.odt"

    if request.method == "POST":
        context = request.form

        document = generate.from_template(template, context=context)

        try:
            return send_file(
                io.BytesIO(document), mimetype="application/vnd.oasis.opendocument.text",
                as_attachment=True, attachment_filename="титульник_реф.odt"
            )
        except Exception as e:
            print(e)

    return render_template("ref.html")

@app.route("/editor", methods=["GET", "POST"])
def editor():
    """ Editor page """

    if request.method == "POST":
        
        html = request.form["html"]
        name = request.form["document_name"]

        generate.html_to_format(html, "odt", name)

    return render_template("editor.html")

@app.route("/download/<document_name>", methods=["POST"])
def download(document_name):
    """ Send file from download folder """
    print(document_name)

    return send_from_directory(app.config["DOCUMENT_UPLOADS"], document_name, as_attachment=True)

@app.route("/delete/<document_name>", methods=["DELETE"])
def delete(document_name):
    """ We interact with this through ajax
    in our html
    Deletes file after users download(look for editor.html)
    """

    delete_file.delete(document_name) 

    return jsonify({"message": "File Delete..."})
