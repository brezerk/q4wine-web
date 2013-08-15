from docs.models import Doc
from django.shortcuts import render_to_response

def index(request, language):
    try:
        lang = Doc.objects.filter(language = language)[0]
        return render_to_response('docs/index.html', {'docs': Doc.objects.filter(language = language).order_by('slug')})
    except:
        return render_to_response('docs/index.html', {'docs': Doc.objects.filter(language = "en_us").order_by('slug')})

def show(request, language, slug):
    try:
        lang = Doc.objects.filter(language = language)[0]
        try:
            doc = Doc.objects.filter(language = language, slug = slug)[0]
            return render_to_response('docs/show.html', {'doc': doc})
        except IndexError:
            return index(request, language)
    except:
        try:
            doc = Doc.objects.filter(language = "en_us", slug = slug)[0]
            return render_to_response('docs/show.html', {'doc': doc})
        except IndexError:
            return index(request, "en_us")
