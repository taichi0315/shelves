from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _

from .models import AppUser, Post, Profile, RecommendUser, Book

class AppUserChangeForm(UserChangeForm):
    class Meta:
        model = AppUser
        fields = '__all__'

class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ('username', 'email','displayname')

class AppUserAdmin(UserAdmin):
    fieldsets = (
        (None,      {'fields': ('username','password')}),
        (_('email'),      {'fields': ('email',)}),
        (_('displayname'),      {'fields':('displayname',)}),
        (_('Permissions'),{'fields':('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

    form = AppUserChangeForm
    add_form = AppUserCreationForm
    list_display = ('username', 'email', 'displayname', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username',)
    ordering = ('username',)

class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        ('作成者',      {'fields': ('created_by',)}),
        ('本',          {'fields':('item',)}),
        ('評価',          {'fields':('rating',)}),
        ('タイトル',     {'fields': ('title',)}),
        ('コメント',     {'fields': ('comment',)}),
        ('公開',     {'fields': ('public',)}),
    )

class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('ユーザ名',      {'fields': ('username',)}),
        ('プロフィール文',      {'fields': ('sentence',)}),
    )

class RecommendUserAdmin(admin.ModelAdmin):
    fieldsets = (
        ('評価一覧',      {'fields': ('critics',)}),
        ('投稿数の対数',      {'fields': ('post_cnt_log',)}),
    )

class BookAdmin(admin.ModelAdmin):
    fieldsets = (
        ('ID',      {'fields': ('book_id',)}),
        ('タイトル',      {'fields': ('title',)}),
        ('画像URL',      {'fields': ('cover_url',)}),
    )

admin.site.register(AppUser, AppUserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(RecommendUser, RecommendUserAdmin)
admin.site.register(Book, BookAdmin)