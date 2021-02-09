from django.db import models


class Category(models.Model):
    cat_name = models.CharField(max_length=254)
    cat_friendlyname = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.cat_name

    def get_friendly_name(self):
        return self.cat_friendlyname

