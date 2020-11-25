from django.db import models

# Create your models here.
# we map here atr to database
from django.urls import reverse

class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=100)
    summary     = models.TextField(blank=False, null=False, default=False)
    featured    = models.BooleanField(default=False)

    # def get_absolute_url(self):
    #     '''grab url and make in consistent django - template so we do not need to care'''
    #     return f"/products/{self.id}/"

    def get_absolute_url(self):
        '''grab url and make in consistent django - template so we do not need to care'''
        return reverse("products:product_dynamic_detail", kwargs={"my_id": self.id}) #f"/products/{self.id}/"

