from django.core.management.base import BaseCommand, CommandError
from shelves.models import Book
import json, urllib.request

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("test")

        url = "https://www.googleapis.com/books/v1/volumes?q=嫌われる勇気"
        url_data = urllib.request.urlopen(url)
        print(type(url_data))
        #json_data = json.loads(url_data.read().decode("utf-8"))

        #print(json_data)