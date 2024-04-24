from django.shortcuts import render,redirect
from .models import Page
from .forms import PageForm


# Create your views here.
def page_list(request):
    pages = Page.objects.all()
    context = {"pages" : pages}
    return render(request, 'diary/page_list.html', context)


def page_detail(request, page_id):
    pages = Page.objects.get(id=page_id)
    context = {"page" : pages}
    return render(request, 'diary/page_detail.html', context)


def info(request):
    pages = Page.objects.all()
    context = {"pages" : pages}
    return render(request, 'diary/info.html', context)


def page_create(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid(): 
            new_page = form.save() 
            return redirect('page-detail', page_id=new_page.id)         
    else:
        form = PageForm()
    return render(request, 'diary/page_form.html', {'form': form})