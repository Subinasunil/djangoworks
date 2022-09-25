from django.urls import path
from bookapi import views

urlpatterns = [
    path('register', views.SignUpView.as_view(), name="register"),
    path("", views.LoginView.as_view(), name="signin"),
    path("home", views.IndexView.as_view(), name="index"),
    path("userpage", views.UserPageView.as_view(), name="userpage"),
    path("signout", views.SignOutView.as_view(), name="signout"),
    path("book/add", views.BookAddView.as_view(), name="addbook"),
    path("book/all", views.BookListView.as_view(), name="listbook"),
    path("book/remove/<int:id>", views.delete_book, name="remove-book"),
    path("book/details/<int:id>", views.TodoDetailView.as_view(), name="book-detail"),
    path("book/change/<int:id>", views.BookEditView.as_view(), name="edit-book")

]
