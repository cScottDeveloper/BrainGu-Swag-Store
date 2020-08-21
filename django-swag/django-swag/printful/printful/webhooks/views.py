from django.http import HttpResponse
from django.views.decorators.http import require_POST


@require_POST
def example(request):
    return HttpResponse('Hello, world. This is the webhook response.')
