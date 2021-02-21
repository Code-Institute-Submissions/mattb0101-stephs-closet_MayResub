from django.http import HttpResponse


class StripeWeb_Handler:
    """ Handles web hooks from Stripe """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle specific or unknown web hook events
        """
        return HttpResponse(
            content=f'Webhook received: {event[type]}',
            status=200)
