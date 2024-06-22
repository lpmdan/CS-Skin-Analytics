import datetime
from django.db import models
from django.db.models import JSONField
from django.contrib.auth.models import User
# Create your models here.


class buff163(models.Model):
    class Meta:
        db_table = 'buff163_data'
        managed = False
    market_hash_name = models.CharField(max_length=100)
    buy_max_price = models.FloatField(null=True)
    buy_num = models.IntegerField(null=True)
    can_bargain = models.BooleanField(null=True)
    buff_custom_id = models.IntegerField(null=True)
    market_min_price = models.IntegerField(null=True)
    quick_price = models.FloatField(null=True)
    sell_min_price = models.FloatField(null=True)
    sell_num = models.FloatField(null=True)
    sell_reference_price = models.FloatField(null=True)
    transacted_num = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.market_hash_name

class skinout(models.Model):
    class Meta:
        db_table = 'skinout_data'
        managed = False
    market_hash_name = models.CharField(max_length=100)
    skinout_custom_id = models.IntegerField(null=True)
    float = models.FloatField(null=True)
    stickers = JSONField(null=True)
    price = models.FloatField(null=True)
    locked = models.BooleanField(null=True)
    unlock_time = models.CharField(max_length=20, null=True)
    total_count = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.market_hash_name


class skinport(models.Model):
    class Meta:
        db_table = 'skinport_data'
        managed = False
    market_hash_name = models.CharField(max_length=100)
    suggested_price = models.FloatField(null=True)
    min_price = models.FloatField(null=True)
    max_price = models.FloatField(null=True)
    mean_price = models.FloatField(null=True)
    median_price = models.FloatField(null=True)
    quantity = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.market_hash_name


class steam(models.Model):
    class Meta:
        db_table = 'steam_data'
        managed = False
    hash_name = models.CharField(max_length=100)
    sell_listings = models.IntegerField(null=True)
    sell_price = models.IntegerField(null=True)
    sale_price_text = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.hash_name
    
class personalMarketData(models.Model): # This is for the user's personal details for any markets that need it. E.g. Buff163 cookie, any api keys, etc.
    #user 
    pass