from rest_framework.permissions import BasePermission
from .models import EmailVerificationModel
from utils import get_hash_ip_address
from datetime import timedelta
from django.utils import timezone


class IsValidEmail(BasePermission):
    def has_permission(self, request, view):
        try:
            email_code = EmailVerificationModel.objects.get(
                hash_ip_address=get_hash_ip_address(request)
            )
        except EmailVerificationModel.DoesNotExist:
            return False

        return email_code.is_verified


class IsAbleToSendAgain(BasePermission):
    def has_permission(self, request, view):
        try:
            email_code = EmailVerificationModel.objects.get(
                hash_ip_address=get_hash_ip_address(request)
            )
        except EmailVerificationModel.DoesNotExist:
            return False

        if email_code.is_expired():
            return False

        if timezone.now() - email_code.time_updated < timedelta(minutes=5):
            return False

        if email_code.user_sent_mails >= 3:
            email_code.verification_test_failed()
            return False

        return True
