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
     za = feedparser.parse('https://feeds.npr.org/1001/rss.xml')
     zb = za.entries[0].title + '. ' + za.entries[0].summary
     zc = za.entries[1].title + '. ' + za.entries[1].summary
     zd = za.entries[2].title + '. ' + za.entries[2].summary
     ze = za.entries[3].title + '. ' + za.entries[3].summary
     zf = za.entries[4].title + '. ' + za.entries[4].summary
     zg = za.entries[5].title + '. ' + za.entries[5].summary
     zh = za.entries[6].title + '. ' + za.entries[6].summary
     zi = za.entries[7].title + '. ' + za.entries[7].summary
     zj = za.entries[8].title + '. ' + za.entries[8].summary
     zk = za.entries[9].title + '. ' + za.entries[9].summary
     zl = za.entries[10].title + '. ' + za.entries[10].summary
     zm = za.entries[11].title + '. ' + za.entries[11].summary
     zn = za.entries[12].title + '. ' + za.entries[12].summary
     zo = za.entries[13].title + '. ' + za.entries[13].summary
     zp = za.entries[14].title + '. ' + za.entries[14].summary
     zq = feedparser.parse('https://feeds.arstechnica.com/arstechnica/index')
     zr = zq.entries[0].title + '. ' + zq.entries[0].summary
     zs = zq.entries[1].title + '. ' + zq.entries[1].summary
     zt = zq.entries[2].title + '. ' + zq.entries[2].summary
     zu = zq.entries[3].title + '. ' + zq.entries[3].summary
     zv = zq.entries[4].title + '. ' + zq.entries[4].summary
     zw = zq.entries[5].title + '. ' + zq.entries[5].summary
     zx = zq.entries[6].title + '. ' + zq.entries[6].summary
     zy = zq.entries[7].title + '. ' + zq.entries[7].summary
     zz = zq.entries[8].title + '. ' + zq.entries[8].summary
     zza = zq.entries[9].title + '. ' + zq.entries[9].summary
     zzb = zq.entries[10].title + '. ' + zq.entries[10].summary
     zzc = zq.entries[11].title + '. ' + zq.entries[11].summary
     zzd = zq.entries[12].title + '. ' + zq.entries[12].summary
     zze = zq.entries[13].title + '. ' + zq.entries[13].summary
     zzf = zq.entries[14].title + '. ' + zq.entries[14].summary
     zzg = feedparser.parse('https://www.wgrz.com/feeds/syndication/rss/news/local')
     zzh = zzg.entries[0].title + '. ' + zzg.entries[0].summary
     zzi = zzg.entries[1].title + '. ' + zzg.entries[1].summary
     zzj = zzg.entries[2].title + '. ' + zzg.entries[2].summary
     zzk = zzg.entries[3].title + '. ' + zzg.entries[3].summary
     zzl = zzg.entries[4].title + '. ' + zzg.entries[4].summary
     zzm = zzg.entries[5].title + '. ' + zzg.entries[5].summary
     zzn = zzg.entries[6].title + '. ' + zzg.entries[6].summary
     zzo = zzg.entries[7].title + '. ' + zzg.entries[7].summary
     zzp = zzg.entries[8].title + '. ' + zzg.entries[8].summary
     zzq = zzg.entries[9].title + '. ' + zzg.entries[9].summary
     return JsonResponse((zb,zc,zd,ze,zf,zg,zh,zi,zj,zk,zl,zm,zn,zo,zp,zr,zs,zt,zu,zv,zw,zx,zy,zz,zza,zzb,zzc,zzd,zze,zzf,zzh,zzi,zzj,zzk,zzl,zzm,zzn,zzo,zzp,zzq), safe=False)
