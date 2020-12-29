from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST


@require_POST
def upload_file(request):
    return HttpResponse(status=200)
