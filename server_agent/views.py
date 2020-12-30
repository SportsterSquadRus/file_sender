from django.shortcuts import redirect


def redirect_view(request):
    return redirect('list_url', permanent=True)