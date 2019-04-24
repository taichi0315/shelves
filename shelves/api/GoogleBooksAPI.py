import requests, json

def get_thumbnail_url(title):
    req_url = 'https://www.googleapis.com/books/v1/volumes?q='+title
    response = requests.get(req_url)
    response_dic = json.loads(response.text)
    cover_url = response_dic["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]
    return cover_url