from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .service import FileReader
from .models import FileClass, Number
from django.views.generic import ListView, DetailView, View


@require_POST
@csrf_exempt
def upload_file(request):
    files = request.FILES
    for key in files:
        data_obj = files[key]
        numbers = tuple(map(lambda x: Number.objects.create(
            num=int(x) if str(x).isdecimal() and int(x) > 0 else 1), 
            data_obj.read().decode('utf-8').split()))
        new_file = FileClass.objects.create(obj=data_obj)
        new_file.numbers.set(numbers)
    return HttpResponse("files added")


class FilesListView(ListView):
    model = FileClass
    queryset = FileClass.objects.all()
    template_name = 'upload/list.html'
    context_object_name = 'files'
    paginate_by = 4


class FileDetailView(View):
    def get(self, request, pk):
        obj = get_object_or_404(FileClass, pk=pk)
        data_obj = FileReader(obj.obj.path)
        data = data_obj.read()
        return render(request, 'upload/detail.html', {'file': obj, 'data': data})
