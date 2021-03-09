from django.http import HttpResponse

class StripeWH_Handler:
    """Handle stripe webhooks
    """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected event
        """
        return HttpResponse(
            content = f'webhook recieved: {event:["type"]}',
            status=200)