import requests
import json
from requests.exceptions import HTTPError
from model.dbo import ISBNDO

GOOGLE_BOOKS_URL = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
LIST_ISBN = [
    '9780002005883',
    '9780002238304',
    '9780002261982',
    '9780006163831',
    '9780006178736',
    '9780006280897',
    '9780006280934',
    '9780006353287',
    '9780006380832',
    '9780006470229']


def createDo(item):
    dbo = ISBNDO(item)
    return dbo


def get_book_details_seq(isbn, session):
    url = GOOGLE_BOOKS_URL + isbn
    response = None
    try:
        response = session.get(url)
        response.raise_for_status()
        #print("Response status ({0}): {1}".format(url, response.status_code))
    except HTTPError as http_err:
        print("HTTP error occurred: {0}".format(http_err))
    except Exception as err:
        print("An error ocurred: {0}".format(err))
    response_json = response.json()
    items = response_json.get("items", [{}])[0]
    return items, response.status_code


def getBook(isbn):
    with requests.Session() as session:
        try:
            response, external_status = get_book_details_seq(isbn, session)
            info = response.get("volumeInfo")
            title = info.get("title", None)
            subtitle = info.get("subtitle", "No")
            description = info.get("description", None)
            pb_date = info.get("published_date", None)
            result = ISBNDO(title, subtitle, description, pb_date)
        except Exception as err:
            result = ""
            print("Exception occured: {0}".format(err))
            pass
    return result, external_status


if __name__ == "__main__":
    data = getBook(LIST_ISBN[0])
    print(data[1])