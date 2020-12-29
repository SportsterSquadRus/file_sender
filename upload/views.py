from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
# import os
# from django.core.files.storage import default_storage
# from django.core.files.base import ContentFile
# from django.conf import settings
from .models import FileClass
from django.views.generic import ListView, DetailView


@require_POST
@csrf_exempt
def upload_file(request):
    files = request.FILES
    for key in files:
        data = files[key]
        FileClass.objects.create(file=data)

    return HttpResponse("file added")


class FilesListView(ListView):
    model = FileClass
    queryset = FileClass.objects.all()
    template_name = 'upload/list.html'
    context_object_name = 'files'
    paginate_by = 4







