from news.models import *
from django.shortcuts import render_to_response

from django.core.paginator import Paginator, EmptyPage, InvalidPage

def news(request, page=1):
    
    news = Paginator(News.objects.order_by('-date'), 10)
    try:
        page_list = news.page(page)
    except (EmptyPage, InvalidPage):
        page_list = news.page(news.num_pages)

    return render_to_response('index.html', {'news': page_list.object_list, 'page_list': page_list, 'viewDesc': True })

def viewNews(request, newsid):
    news = News.objects.filter(pk=newsid)
    return render_to_response('index.html', {'news': news})
