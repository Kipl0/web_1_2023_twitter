from bottle import get, template

@get("/upload-picture")
def _():
    return template("upload_files")