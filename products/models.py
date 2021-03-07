from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    cat_name = models.CharField(max_length=254)
    cat_friendlyname = models.CharField(
        max_length=254, blank=True)

    def __str__(self):
        return self.cat_name

    def get_friendly_name(self):
        return self.cat_friendlyname


class Sub_Category(models.Model):

    class Meta:
        verbose_name_plural = 'Sub Categories'

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    subcat_name = models.CharField(max_length=254)
    subcat_friendlyname = models.CharField(
        max_length=254, blank=True)

    def __str__(self):
        return self.subcat_name

    def get_friendly_name(self):
        return self.subcat_friendlyname


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    subcat = models.ForeignKey(
        'Sub_Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, blank=True)
    gender = models.CharField(max_length=254, blank=True)
    name = models.CharField(max_length=254)
    article_type = models.CharField(max_length=254, blank=True)
    colour = models.CharField(max_length=254, blank=True)
    season = models.CharField(max_length=254, blank=True)
    year = models.CharField(max_length=254, blank=True)
    usage = models.CharField(max_length=254, blank=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(blank=True)
    in_stock = models.IntegerField(blank=True, null=True, default=0)

    def issue_stock(self):
        self.in_stock = self.in_stock - self.stockproduct.amount
        self.save()

    def __str__(self):
        return self.name


class Size(models.Model):
    product = models.ForeignKey(
        Product, null=True, blank=True, on_delete=models.CASCADE)
    size = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.size
