from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Stock


@receiver(post_save, sender=Stock)
def update_stock(sender, instance, **kwargs):
    """
    Update order total on updating or creating line item
    """
    instance.in_stock -= instance.issue_qty
    instance.save()
