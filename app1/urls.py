from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app1'
urlpatterns = [
    path('', views.index, name='index'),
    path('/adminadmin/', admin.site.urls),
    path('/create', views.create, name='create'),
    path('/show/<int:id>', views.show, name='show'),
    path('/card', views.card),
    path('/update/<int:id>', views.update, name='update'),
    path('/delete/<int:id>', views.destroy, name='destroy'),
]