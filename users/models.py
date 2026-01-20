from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Thêm 2 trường để phân biệt loại tài khoản
    is_client = models.BooleanField(default=False, verbose_name="Là Người thuê")
    is_freelancer = models.BooleanField(default=False, verbose_name="Là Freelancer")
    
    # Ví tiền ảo (quan trọng cho dự án này)
    wallet_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.username