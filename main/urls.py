from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('top/', top, name='top'),
    path('library/', library, name='library'),
    path('booklist/', booklist, name='booklist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit/', edit_profile, name='edit')
]