from django.urls import path
from book_outlet import views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:slug>", views.book_details, name="book-details")
]
