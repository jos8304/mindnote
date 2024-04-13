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
        title = request.POST['title']
        content = request.POST['content']
        feeling = request.POST['feeling']
        score = request.POST['score']
        dt_created = request.POST['dt_created']
        new_page = Page(
            title = title,
            content = content,
            feeling = feeling,
            score = score,
            dt_created = dt_created
        )
        new_page.save()
        return redirect('page-detail', page_id=new_page.id)
    else:
        page_form = PageForm
        return render(request, 'diary/page_form.html', {'form': page_form})