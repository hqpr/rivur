from django.contrib.auth.models import User
from django.db import models

RATING_CHOICES = (
    ('-5', '-5'),
    ('-4', '-4'),
    ('-3', '-3'),
    ('-2', '-2'),
    ('-1', '-1'),
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/', default=0)
    second_image = models.ImageField(upload_to='products/', default=None, blank=True, null=True)
    third_image = models.ImageField(upload_to='products/', default=None, blank=True, null=True)
    fourth_image = models.ImageField(upload_to='products/', default=None, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    added = models.DateField(auto_now_add=True)
    rating = models.CharField(choices=RATING_CHOICES, default=0, max_length=150)

    def __unicode__(self):
        return self.title


class RequestProduct(models.Model):
    product = models.ForeignKey(Product)
    user = models.ForeignKey(User)
    added = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.user