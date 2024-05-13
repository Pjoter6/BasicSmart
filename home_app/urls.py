from django.contrib import admin
from django.urls import path
from . import views
from home_app.views import strona_powitalna, wybor_czujnika, login_view, login, image_view, light_view, tabela_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', strona_powitalna, name='strona_powitalna'),
    path('wybory/', login, name=''),
    path('login/', login_view, name='login'),
    path('login/home_app/wybor_czujnika', wybor_czujnika, name='wybor_czujnika'),
    path('', views.image_view, name='image_view'),
    path('light_view/', light_view, name='light_view'),
    path('light_view/', tabela_view, name='tabelaZarowka')

]





