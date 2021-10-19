from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from main.models import Post


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    products = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.products.title

    @property
    def amount(self):
        return self.quantity*self.products.prise