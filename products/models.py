from django.db import models


class Category(models.Model):
    cat_name = models.CharField(max_length=254)
    cat_friendlyname = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.cat_name

    def get_friendly_name(self):
        return self.cat_friendlyname


class Sub_Category(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    subcat_name = models.CharField(max_length=254)
    subcat_friendlyname = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.subcat_name

    def get_friendly_name(self):
        return self.subcat_friendlyname


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    subcat = models.ForeignKey('Sub_Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    gender = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    article_type = models.CharField(max_length=254, null=True, blank=True)
    colour = models.CharField(max_length=254, null=True, blank=True)
    season = models.CharField(max_length=254, null=True, blank=True)
    year = models.CharField(max_length=254, null=True, blank=True)
    usage = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
