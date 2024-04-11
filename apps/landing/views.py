from django.shortcuts import render

# Create your views here.


def show_landing_view(request):
    return render(
        request,
        'landing/index.html',
        context={
            'title': 'Ottosender'
        }
    )