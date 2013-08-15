# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from q4wine.xmlexport.models import *
from django.core.paginator import Paginator
from django.db.models import Q
import re

def checkForAgent(request):
#    regexp = re.compile("^q4wine/[0-1].[0-9]\{3\}([ ]|-[0-9a-zA-Z]+[ ])\([0-9a-zA-Z]+; [0-9a-zA-Z]+ (([0-9a-zA-Z]+)|(x86_64))\) xmlparser/[0-9].[0-9]$");
#    regexp = re.compile("^q4wine/[0-1].[0-9]\{3\}");
#    if regexp.match(request.META['HTTP_USER_AGENT']):
     return True
#    return False

def index(request):
    t = get_template('xmlexport/xmlexport.html')
    html = t.render(Context({}))
    return HttpResponse(html)

def searchApp(request, pattern, page = 1):
    if not checkForAgent(request):
        return index(request)

    search = Appfamily.objects.using('apidb').filter(appname__icontains=pattern,state='accepted')

    if search.count()<=0:
        t = get_template("xmlexport/message.xml")
        xml = t.render(Context({'code': 404}))
        return HttpResponse(xml)

    p = Paginator(search, 9)
    app_list = ""

    for app in p.page(page).object_list:
        versions = getAppVersions(app.appid)
        t = get_template("xmlexport/application.xml")
        app_list += t.render(Context({'app': app, 'versions': versions}))

    t = get_template("xmlexport/header.xml")
    xml = t.render(Context({'action': "searchApp", 'page': page, 'num_pages': p.num_pages, 'app_list': app_list}))
    return HttpResponse(xml)

def viewApp(request, appid):

    if not checkForAgent(request):
        return index(request)

    search = Appfamily.objects.using('apidb').get(appid=appid,state='accepted')
    app_view = ""

    versions = getAppVersions(appid)
    cat_list = getAppCategoryes(search.catid)
    t = get_template("xmlexport/application.xml")
    app_view += t.render(Context({'app': search, 'versions': versions, 'cat_list': cat_list}))

    t = get_template("xmlexport/header.xml")
    xml = t.render(Context({'action': "viewApp", 'app_view': app_view}))
    return HttpResponse(xml)

def viewTest(request, appid, verid, testid = 0):

    if not checkForAgent(request):
        return index(request)

    search = Appfamily.objects.using('apidb').get(appid=appid,state='accepted')
    app_view = ""

    versions = getAppVersions(appid)
    cat_list = getAppCategoryes(search.catid)
    test_info = getAppTestInfo(verid, testid)
    tests = getAppTestList(verid, testid)
    bugs_list = getAppBugsList(verid)
    notes_list = getAppNotes(appid, verid)
    comments_list = getAppComments(verid, 0)
    t = get_template("xmlexport/application.xml")
    app_view += t.render(Context({'app': search, 'verid': int(verid), 'versions': versions, 'cat_list': cat_list, 'test_info': test_info, 'tests': tests, 'bugs_list': bugs_list, 'notes_list': notes_list, 'comments_list': comments_list}))

    t = get_template("xmlexport/header.xml")
    xml = t.render(Context({'action': "viewTest", 'app_view': app_view}))
    return HttpResponse(xml)

def viewCategory(request, catid):
    if not checkForAgent(request):
        return index(request)

    cat_view = ""
    subcat_list = Appcategory.objects.using('apidb').filter(catparent=catid)
    if int(catid)==0:
        cat_list = []
    else:
        cat_list = getAppCategoryes(catid)
    app_list = Appfamily.objects.using('apidb').filter(catid=catid,state='accepted')

    t = get_template("xmlexport/category.xml")
    cat_view += t.render(Context({'cat_list': cat_list, 'subcat_list': subcat_list, 'app_list': app_list}))


    t = get_template("xmlexport/header.xml")
    xml = t.render(Context({'action': "viewCategory", 'cat_view': cat_view}))
    return HttpResponse(xml)

def getAppVersions(appid):
    versions = Appversion.objects.using('apidb').filter(appid=appid,state='accepted')
    return versions

def getAppCategoryes(catid):
    cat_list=[]
    category = Appcategory.objects.using('apidb').get(catid=catid)

    if (category.catparent>0):
        cat_list.append(getAppCategoryes(category.catparent)[0])

    cat_list.append(category)
    return cat_list

def getAppTestInfo(verid, testid):
    testid=int(testid)
    if testid<=0:
        test_info = Testresults.objects.using('apidb').filter(versionid=verid,state='accepted').order_by('-submittime')[:1][0]
    else:
        test_info = Testresults.objects.using('apidb').get(versionid=verid,testingid=testid,state='accepted')

    return test_info

def getAppTestList(verid, testid):
    testid = int(testid)
    xml_view=""
    tests=Testresults.objects.using('apidb').filter(versionid=verid,state='accepted').order_by('-submittime')[:5]
    if testid<=0:
        testid=tests[0].testingid
    for test in tests:
        t = get_template("xmlexport/test.xml")
        distrib = Distributions.objects.using('apidb').get(distributionid=test.distributionid)
        xml_view += t.render(Context({'id': test.testingid, 'distrib': distrib.name, 'date': test.testeddate, 'winever': test.testedrelease, 'installs': test.installs, 'runs': test.runs, 'rating': test.testedrating, 'curid': testid}))
    return xml_view

def getAppBugsList(verid):
    bug_list=[]
    bugs = Buglinks.objects.using('apidb').filter(versionid=verid,state='accepted').order_by('bug_id')
    for bug in bugs:
        try:
            bug_info = Bugs.objects.using('apidb').get(Q(bug_id=bug.bug_id), Q(bug_status='NEW')|Q(bug_status='UNCONFIRMED'))
            bug_list.append(bug_info)
        except NameError:
            pass
        except Exception:
            pass
    return bug_list

def getAppNotes(appid, verid):
    notes_list = Appnotes.objects.using('apidb').filter(Q(versionid=verid)|Q(versionid=verid,appid=appid)).order_by('noteid')
    return notes_list

def getAppComments(verid, parentid):
    comment_list = []
    comment_rawlist = Appcomments.objects.using('apidb').filter(versionid=verid,parentid=parentid).order_by('-time')
    for comment in comment_rawlist:
        comment_list.append(comment)
        re_list = getAppComments(verid, comment.commentid)
        for re in re_list:
            comment_list.append(re)
    return comment_list
