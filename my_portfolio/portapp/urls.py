from portapp import views
from django.urls import path


urlpatterns = [
    path("main/", views.main_page, name='mainpg')
]