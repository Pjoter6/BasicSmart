from django.contrib import admin
from django.urls import path
from home_app.views import strona_powitalna, wybor_czujnika, login_view
from registration.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', strona_powitalna, name='strona_powitalna'),
    path('wybory/', login, name=''),
    path('login/', login_view, name='login'),




]
