import random
import string

from payments.models import BasePayment
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


def generate_key():
    key = str()
    for _ in range(6):
        key += random.choice(string.ascii_lowercase + string.digits)

    return key


class User(AbstractUser):
    users = UserManager()
    phone_number = models.CharField(max_length=16)
    key = models.CharField(max_length=16, default=generate_key)


class IndividualRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    birth_day = models.DateField()
    region = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    street_number = models.CharField(max_length=255)
    debt_value = models.CharField(max_length=10)
    term = models.PositiveIntegerField()
    created_workplace = models.PositiveIntegerField()
    proposition = models.TextField()
    paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Jismoniy shaxs arizasi'
        verbose_name_plural = 'Jismoniy shaxs arizalari'


class EntityRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    MFO = models.CharField(max_length=255)
    INN = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    debt_value = models.CharField(max_length=10)
    term = models.PositiveIntegerField()
    created_workplace = models.PositiveIntegerField()
    proposition = models.TextField()
    paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Yuridik shaxs arizasi'
        verbose_name_plural = 'Yuridik shaxs arizalari'


class Payment(BasePayment):
    individual_request = models.ForeignKey(
        IndividualRequest,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    entity_request = models.ForeignKey(
        EntityRequest,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
