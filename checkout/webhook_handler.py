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
            content=f'Unhandled webhook received: {event[type]}',
            status=200)

    def handle_payment_intent_succeed(self, event):
        """
        Handle payment intent success from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event[type]}',
            status=200)

    def handle_payment_intent_fail(self, event):
        """
        Handle payment intent fail from Stripe
        """
        return HttpResponse(
            content=f'Intent Failed Webhook received: {event[type]}',
            status=200)


