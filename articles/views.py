from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Articles
from .forms import ArticleForm

@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()
    return render(request, "articles/create.html", context=context)


def article_search_view(request):
    # print(dir(request))
    print(request.GET)
    query_dict = request.GET # this is a dictionary
    # query = query_dict.get("q") # <input type='text' name='q' />
    try:
        query = int(query_dict.get("q"))
    except:
        query = None
    article_obj = None
    if query is not None:
        article_obj = Articles.objects.get(id=query)
    context = {
        "object": article_obj
    }
    return render(request, "articles/search.html", context=context)

def article_detail_view(request, id=None):
    article_obj=None

    if id is not None:
        article_obj = Articles.objects.get(id=id)

    context = {
        "object": article_obj,
    }

    return render(request, "articles/detail.html", context=context)
