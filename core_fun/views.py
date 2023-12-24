from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework import permissions, status
import yagmail

from core_fun.serializers import UserReviewSerializer
from core_fun import constants as CONST
from .models import SubscribedUser, UserReview
from django.contrib import messages
from django.contrib.auth import login, logout, get_user_model, authenticate


class HomeTemplateView(APIView):
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, "index2.html")


class BookTemplateView(APIView):
    context = {}

    def get(self, request, *args, **kwargs):
        reviews = UserReview.objects.all()
        print(reviews)
        return render(request, "book1.html", {"reviews": reviews})


class SendNotificationToSubscriberView(APIView):
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, "send_mailers.html")

    def post(self, request, *args, **kwargs):
        subscribers = SubscribedUser.objects.all()
        print(subscribers)
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        try:
            send_email(
                subject,
                message,
                to_email=[CONST.DEFAULT_RECEPIENT, "shashanksumedha@gmail.com"],
            )
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect(request.META.get("HTTP_REFERER", "/"))

        messages.success(request, f"Mail Sent successfully!")
        return redirect(request.META.get("HTTP_REFERER", "/"))


class UploadTemplateView(APIView):
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, "contact.html")

    def post(self, request, *args, **kwargs):
        data = {
            "name": request.POST.get("name"),
            "email": request.POST.get("email"),
            "message": request.POST.get("message"),
        }
        serializer = UserReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, f"Review Stored Successfully!")
            return Response("Review created", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def subscribe(request):
    if request.method == "POST":
        model = SubscribedUser
        email = request.POST.get("email", None)

        if not email:
            messages.error(request, "Please enter a valid email address")
            return redirect(request.META.get("HTTP_REFERER", "/"))

        subscribed_user = model.objects.filter(email=email).first()
        if subscribed_user:
            messages.error(request, f"{email} is already a subscribed user!")
            return redirect(request.META.get("HTTP_REFERER", "/"))

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect(request.META.get("HTTP_REFERER", "/"))

        model_instance = SubscribedUser()
        model_instance.email = email
        model_instance.save()

        messages.success(request, f"{email} is now subscribed")
        return redirect(request.META.get("HTTP_REFERER", "/"))


def send_email(subject, message, to_email=CONST.DEFAULT_RECEPIENT):
    from_email = CONST.SENDER_EMAIL
    user = yagmail.SMTP(user=from_email, password=CONST.SENDER_PASSWORD)
    user.send(to=to_email, subject=subject, contents=message)
