from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem
from stock.models import Stock


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on updating or creating line item
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on deleting line item
    """
    instance.order.update_total()


@receiver(post_save, sender=Stock)
def update_on_sale(sender, instance, **kwargs):
    """
    Update stock on sale
    """
    instance.update_on_sale()
