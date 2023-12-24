from django.contrib import admin
from django.urls import path, include
from .views import HomeTemplateView, subscribe, BookTemplateView, UploadTemplateView, SendNotificationToSubscriberView



urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home_page"),
    path("book", BookTemplateView.as_view(), name="book_details"),
    path("upload_review", UploadTemplateView.as_view(), name="upload_review"),
    path("send_mailers", SendNotificationToSubscriberView.as_view(), name="send_mailers"),

    path("subscribe", subscribe, name="subscribe"),


]
