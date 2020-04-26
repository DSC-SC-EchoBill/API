from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Device(models.Model):
    device_id = models.TextField(max_length=8, default='0', primary_key=True)
    trade_name = models.TextField(max_length=10, default='')


# 영수증 이미지
class Receipt(models.Model):
    receipt_img_url = models.TextField(default='')
    receipt_date = models.DateTimeField(auto_now_add=True)
    is_Storage = models.IntegerField(default=0)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    total_price = models.IntegerField(default=0)


# 확인 코드를 저장하는 모델
class VerifyCodes(models.Model):
    email = models.EmailField()
    verify_code = models.CharField(max_length=5)
    date = models.DateTimeField(auto_now_add=True)

