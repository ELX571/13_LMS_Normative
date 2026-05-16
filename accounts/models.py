from django.contrib.auth.models import User
from django.db import models
from django.core.mail import send_mail
import random
from django.utils import timezone
from datetime import timedelta
from config.settings import *

def generate_code():
    # 6 xonali code yaratb beradi verifiction qilish uchun emailga send qladi
    return random.randint(100000, 999999)


def exp_time():
    # codeni amal qilish muddatini belgilaydigan vaqt
    return timezone.now() + timedelta(minutes=2)

class VerifyCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='verify_codes')
    code = models.PositiveIntegerField(default=generate_code)
    expiration_date = models.DateTimeField(default=exp_time)

    def is_valid(self):
        return timezone.now() < self.expiration_date

    def __str__(self):
        return f"{self.user.username} - Kode: {self.code}"

    
