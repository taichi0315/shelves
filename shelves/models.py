from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.conf import settings
from annoying.fields import AutoOneToOneField

class RecommendUser(models.Model):
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    critics = models.TextField('評価一覧')
    post_cnt_log = models.FloatField('投稿数の対数')

class Book(models.Model):
    book_id = models.CharField('ID',max_length=256, primary_key=True, unique=True)
    title = models.CharField('タイトル',max_length=256)
    cover_url = models.CharField('画像URL',max_length=256,blank=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    item = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
    )

    title = models.CharField('記事タイトル',max_length=256, blank=True)
    comment = models.TextField('コメント', blank=True)
    rating = models.FloatField('評価',default=2.5)
    public = models.BooleanField('公開', default=False)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    def __str__(self):
        return self.title

class Profile(models.Model):
    username = AutoOneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True
    )
    sentence = models.TextField('プロフィール文',max_length=300, blank=True)

    def __str__(self):
        return self.username

class AppUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):

        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)

        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)
    
    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, True, **extra_fields)

class AppUser(AbstractBaseUser, PermissionsMixin):

    username=models.CharField(_('username'), max_length=20, unique=True, primary_key=True, db_index=True)
    email = models.EmailField(_('email address'))
    displayname = models.CharField('表示名', max_length=20)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    objects = AppUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']