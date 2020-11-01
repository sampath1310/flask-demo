from flask import Blueprint, make_response, request,abort
from .isbn import LIST_ISBN, getBook

isbn = Blueprint('isbn', __name__, url_prefix='/api/v1/isbn')


@isbn.route("/list", methods=['GET'])
def allIsbn():
    result = {"isbnList": LIST_ISBN}
    result_status = 200
    return make_response(result, result_status)


@isbn.route("/query/isbn_id/<id>", methods=["POST"])
def getBookInfo(id):
    print(id)
    code = 200
    if id != None:
        book = getBook(id)
        print(book)
    else:
        abort(400)

    return make_response("done", code)
