from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import feedparser
import re

#Use function rss(rss_address) to get RSS feed data. Function parameter rss_address is the RSS Feed address. Variable npr_list is is the saved RSS feed
#data for NPR's feed. ars_list and buffalo_list are the saved RSS feed data for two other feeds.
def rss(rss_address):
    feedparser_parse = feedparser.parse(f"{rss_address}")
    story_list = []
    clean_story_list1 = []
    clean_story_list2 = []
    for i in range(0,15):
        story_list.append(feedparser_parse.entries[i].title + '. ' + feedparser_parse.entries[i].summary)

    for cleantag in story_list:
        clean_story_list1.append(re.sub('<em>', '', cleantag))

    for cleantag2 in clean_story_list1:
        clean_story_list2.append(re.sub('</em>', '', cleantag2))

    return clean_story_list2

npr_list = rss("https://feeds.npr.org/1001/rss.xml")

ars_list = rss("https://feeds.arstechnica.com/arstechnica/index")

buffalo_list = rss("https://www.wgrz.com/feeds/syndication/rss/news/local")

def index(request):
    context = { "npr_list" : npr_list, "ars_list" : ars_list, "buffalo_list" : buffalo_list } 
    return render(request, 'mysite/index.html', context)

def news(request):
    return JsonResponse((npr_list, ars_list, buffalo_list), safe=False)
