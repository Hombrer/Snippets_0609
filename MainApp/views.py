from django.http import Http404
from django.shortcuts import render, redirect

from MainApp.models import Snippet
from MainApp.forms import SnippetForm

from django.core.exceptions import ObjectDoesNotExist


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    # Хотим получить чистую форму для заполнения полей
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form
            }
        return render(request, 'pages/add_snippet.html', context)
    # Хотим создать новый Snippet на основе данных от формы
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("snippets_list")
        return render(request,'add_snippet.html', {'form': form})


def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {
        'pagename': 'Просмотр сниппетов',
        "snippets": snippets
        }
    return render(request, 'pages/view_snippets.html', context)


def snippet_detail(request, snippet_id):
    try:
        snippet = Snippet.objects.get(id=snippet_id)
    except ObjectDoesNotExist:
        raise Http404
    else:
        context = {
            'pagename': 'Просмотр сниппета',
            "snippet": snippet
            }
        return render(request, 'pages/snippet_detail.html', context)


def snippet_delete(request, snippet_id):
    try:
        snippet = Snippet.objects.get(id=snippet_id)
    except ObjectDoesNotExist:
        raise Http404
    else:
        snippet.delete()
        return redirect("snippets_list")
    

# def create_snippet(request):
#     if request.method == "POST":
#         form = SnippetForm(request.POST)
#         print(vars(form))
#         if form.is_valid():
#             form.save()
#             return redirect("snippets_list")
#         return render(request,'add_snippet.html', {'form': form})
