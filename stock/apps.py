from django.apps import AppConfig


class StockConfig(AppConfig):
    name = 'stock'

    def ready(self):
        import checkout.signals
