from django.http import HttpResponse
import random
from articles.models import Articles
from django.template.loader import render_to_string


def home_view(request,id=None, *args, **kwargs):
    random_id = random.randint(1,2)
    article_object = Articles.objects.get(id=random_id)
    article_title = article_object.title
    article_content = article_object.content

    article_list = Articles.objects.all()
    my_list = article_list

    context = {
        "object_list": my_list,
        "object": article_object,
        "title": article_object.title,
        "content": article_object.content,
        "id": article_object.id,
    }

    HTML_STRING = render_to_string("home-view.html", context = context)

    return HttpResponse(HTML_STRING)