from django.shortcuts import redirect
from django.conf import settings


def start_page_redirect(request):
    'Redirect to default page.'
    return redirect(settings.START_PAGE)