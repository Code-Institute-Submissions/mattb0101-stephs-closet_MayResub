from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem
from stock.models import StockTransactions


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


# might need a dispatch_uid in here....
@receiver(post_save, sender=StockTransactions)
def update_stock(sender, instance, **kwargs):
    """
    Updating stock on order
    """
    instance.product.in_stock -= instance.amount
    instance.product.save()
