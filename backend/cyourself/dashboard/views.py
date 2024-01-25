from django.shortcuts import render


def dash(request):
    template = 'dashboard/dash.html'
    return render(request, template)
