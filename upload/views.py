from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .service import FileReader
from .models import FileClass
from django.views.generic import ListView, DetailView, View


@require_POST
@csrf_exempt
def upload_file(request):
    files = tuple(request.FILES.values())

    for f in files:
        new_file = FileClass.objects.create(
            obj=f, numbers=tuple(
                map(
                    lambda x: int(x) if str(x).isdecimal() and 256 > int(
                        x) > 0 else 1, f.read().decode('utf-8').split()
                )
            )
        )

    return HttpResponse('files added')


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
