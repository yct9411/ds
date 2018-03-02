from django.db import models
from ds_user.models import User
from ds_goods.models import GoodInfo

# Create your models here.
class Cart(models.Model):
  user=models.ForeignKey('ds_user.User',None)
  goods=models.ForeignKey('ds_goods.GoodInfo',None)
  count=models.IntegerField(default=0)

