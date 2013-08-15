# -*- coding: utf-8 -*-
from stripogram import html2safehtml
from HTMLParser import HTMLParser
import cgi

def openHeader(action):
    xml_view="""<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<appdb_export version=\"1.0\" action=\"%s\">""" % action
    return xml_view

def prepareString(string, lenght = 0, strip_html = True):
    string = string.strip()

    if (strip_html):
        result = []
        parser = HTMLParser()
        parser.handle_data = result.append
        parser.feed(string)
        parser.close()
        string = ''.join(result)
    else:
        string = html2safehtml(string, valid_tags=("b", "a", "i", "br", "ul", "li", "strong"))

    if lenght > 0:
        string = string[0:lenght]
        string += "..."

    string = cgi.escape(string)

    return string

def createPages(page, count):
    xml_view="""
    <page>
        <current>%s</current>
        <count>%s</count>
    </page>""" % (page, count)
    return xml_view

def closeHeader():
    xml_view="""\n</appdb_export>"""
    return xml_view

def createAppInfo(appId, verId, appName, appDesc, category, url, verstions_list="", category_list="", test_results="", comment_list="", bugs_list=""):
    xml_view="""
    <app id=\"%s\"""" % appId

    if verId:
        xml_view += " verid=\"%s\" " % verId

    xml_view += """>
        <name>%s</name>
        <desc>""" % prepareString(appName)

    if len(test_results)>0:
        xml_view += prepareString(appDesc, -1, False)
    else:
        xml_view += prepareString(appDesc, 252)

    xml_view += "</desc>"

    xml_view += """
        <category>%s</category>""" % category

    xml_view += """
        <url>%s</url>""" % url

    return xml_view


