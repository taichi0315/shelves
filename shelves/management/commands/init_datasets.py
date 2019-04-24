from django.core.management.base import BaseCommand
from django.contrib.auth.base_user import BaseUserManager

from ...models import Book, Post, AppUser
from ...api.GoogleBooksAPI import get_thumbnail_url

toby = {"claudia":{"Snakes on a Plane": 3.5, "Just My Luck": 3.0, "The Night Listener": 4.5, "Superman Returns": 4.0, "You, Me and Dupree": 2.5},"gene":{"Lady in the Water": 3.0, "Snakes on a Plane": 3.5, "Just My Luck": 1.5, "Superman Returns": 5.0, "The Night Listener": 3.0, "You, Me and Dupree": 3.5},"jack":{"Lady in the Water": 3.0, "Snakes on a Plane": 4.0, "The Night Listener": 3.0, "Superman Returns": 5.0, "You, Me and Dupree": 3.5},"lisa":{"Lady in the Water": 2.5, "Snakes on a Plane": 3.5, "Just My Luck": 3.0, "Superman Returns": 3.5, "You, Me and Dupree": 2.5, "The Night Listener": 3.0},"michael":{"Lady in the Water": 2.5, "Snakes on a Plane": 3.0, "Superman Returns": 3.5, "The Night Listener": 4.0},"mick":{"Lady in the Water": 3.0, "Snakes on a Plane": 4.0, "Just My Luck": 2.0, "Superman Returns": 3.0, "The Night Listener": 3.0, "You, Me and Dupree": 2.0},"toby":{"Snakes on a Plane": 4.5, "You, Me and Dupree": 1.0, "Superman Returns": 4.0}}

class Command(BaseCommand):

    def add_arguments(self, dataset):
        dataset.add_argument('dataset', type=str)

    def handle(self, *args, **options):
        if options['dataset'] == 'toby':
            for user in toby:
                u = AppUser(username=user, email=f'{user}@example.com', password='password')
                u.save()
                for post in toby[user]:
                    b = Book(book_id=post, title=post, cover_url=get_thumbnail_url(post))
                    b.save()
                    if not Post.objects.filter(item=b, created_by=u).exists():
                        p = Post(item=b, created_by=u, title=post, rating=toby[user][post], public=True)
                        p.save()
            self.stdout.write(self.style.SUCCESS('success'))