from importlib.metadata import files

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import DocumentForm, CreateDocumentForm
from .models import Document

def upload_file(request):
    form = DocumentForm(request.POST)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        else:
            form = DocumentForm()

        return render(request, 'upload.html', {'form': form})


def file_list(request):
    files = Document.objects.all()
    return render(request, 'files/file_list.html', {
        'files': files
    })


