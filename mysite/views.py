from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import feedparser
import re

def index(request):
     a = feedparser.parse('https://feeds.npr.org/1001/rss.xml')
     
     b = a.entries[0].title + '. ' + a.entries[0].summary
     b1 = re.sub('<em>', '',b)
     b2 = re.sub('</em>', '',b1)

     c = a.entries[1].title + '. ' + a.entries[1].summary
     c1 = re.sub('<em>', '',c)
     c2 = re.sub('</em>', '',c1)

     d = a.entries[2].title + '. ' + a.entries[2].summary
     d1 = re.sub('<em>', '',d)
     d2 = re.sub('</em>', '',d1)

     e = a.entries[3].title + '. ' + a.entries[3].summary
     e1 = re.sub('<em>', '',e)
     e2 = re.sub('</em>', '',e1)

     ef = a.entries[4].title + '. ' + a.entries[4].summary
     ef1 = re.sub('<em>', '',ef)
     ef2 = re.sub('</em>', '',ef1)

     g = a.entries[5].title + '. ' + a.entries[5].summary
     g1 = re.sub('<em>', '',g)
     g2 = re.sub('</em>', '',g1)

     h = a.entries[6].title + '. ' + a.entries[6].summary
     h1 = re.sub('<em>', '',h)
     h2 = re.sub('</em>', '',h1)

     i = a.entries[7].title + '. ' + a.entries[7].summary
     i1 = re.sub('<em>', '',i)
     i2 = re.sub('</em>', '',i1)

     j = a.entries[8].title + '. ' + a.entries[8].summary
     j1 = re.sub('<em>', '',j)
     j2 = re.sub('</em>', '',j1)

     k = a.entries[9].title + '. ' + a.entries[9].summary
     k1 = re.sub('<em>', '',k)
     k2 = re.sub('</em>', '',k1)

     l = a.entries[10].title + '. ' + a.entries[10].summary
     l1 = re.sub('<em>', '',l)
     l2 = re.sub('</em>', '',l1)

     m = a.entries[11].title + '. ' + a.entries[11].summary
     m1 = re.sub('<em>', '',m)
     m2 = re.sub('</em>', '',m1)

     n = a.entries[12].title + '. ' + a.entries[12].summary
     n1 = re.sub('<em>', '',n)
     n2 = re.sub('</em>', '',n1)

     o = a.entries[13].title + '. ' + a.entries[13].summary
     o1 = re.sub('<em>', '',o)
     o2 = re.sub('</em>', '',o1)

     p = a.entries[14].title + '. ' + a.entries[14].summary
     p1 = re.sub('<em>', '',p)
     p2 = re.sub('</em>', '',p1)

     q = feedparser.parse('https://feeds.arstechnica.com/arstechnica/index')
     r = q.entries[0].title + '. ' + q.entries[0].summary
     s = q.entries[1].title + '. ' + q.entries[1].summary
     t = q.entries[2].title + '. ' + q.entries[2].summary
     u = q.entries[3].title + '. ' + q.entries[3].summary
     v = q.entries[4].title + '. ' + q.entries[4].summary
     w = q.entries[5].title + '. ' + q.entries[5].summary
     x = q.entries[6].title + '. ' + q.entries[6].summary
     y = q.entries[7].title + '. ' + q.entries[7].summary
     z = q.entries[8].title + '. ' + q.entries[8].summary
     ab = q.entries[9].title + '. ' + q.entries[9].summary
     ac = q.entries[10].title + '. ' + q.entries[10].summary
     ad = q.entries[11].title + '. ' + q.entries[11].summary
     ae = q.entries[12].title + '. ' + q.entries[12].summary
     af = q.entries[13].title + '. ' + q.entries[13].summary
     ag = q.entries[14].title + '. ' + q.entries[14].summary
     ah = feedparser.parse('https://www.wgrz.com/feeds/syndication/rss/news/local')
     ai = ah.entries[0].title + '. ' + ah.entries[0].summary
     aj = ah.entries[1].title + '. ' + ah.entries[1].summary
     ak = ah.entries[2].title + '. ' + ah.entries[2].summary
     al = ah.entries[3].title + '. ' + ah.entries[3].summary
     am = ah.entries[4].title + '. ' + ah.entries[4].summary
     an = ah.entries[5].title + '. ' + ah.entries[5].summary
     ao = ah.entries[6].title + '. ' + ah.entries[6].summary
     ap = ah.entries[7].title + '. ' + ah.entries[7].summary
     aq = ah.entries[8].title + '. ' + ah.entries[8].summary
     ar = ah.entries[9].title + '. ' + ah.entries[9].summary
     return render(request, 'mysite/index.html', {'b2':b2,'c2':c2,'d2':d2,'e2':e2,'ef2':ef2,'g2':g2,'h2':h2,'i2':i2,'j2':j2,'k2':k2,'l2':l2,'m2':m2,'n2':n2,'o2':o2,'p2':p2,'r':r,'s':s,'t':t,'u':u,'v':v,'w':w,'x':x,'y':y,'z':z,'ab':ab,'ac':ac,'ad':ad,'ae':ae,'af':af,'ag':ag,'ai':ai,'aj':aj,'ak':ak,'al':al,'am':am,'an':an,'ao':ao,'ap':ap,'aq':aq,'ar':ar})

def news(request):
     za = feedparser.parse('https://feeds.npr.org/1001/rss.xml')
     zb = {"story": za.entries[0].title + '. ' + za.entries[0].summary}
     zc = {"story": za.entries[1].title + '. ' + za.entries[1].summary}
     zd = {"story": za.entries[2].title + '. ' + za.entries[2].summary}
     ze = {"story": za.entries[3].title + '. ' + za.entries[3].summary}
     zf = {"story": za.entries[4].title + '. ' + za.entries[4].summary}
     zg = {"story": za.entries[5].title + '. ' + za.entries[5].summary}
     zh = {"story": za.entries[6].title + '. ' + za.entries[6].summary}
     zi = {"story": za.entries[7].title + '. ' + za.entries[7].summary}
     zj = {"story": za.entries[8].title + '. ' + za.entries[8].summary}
     zk = {"story": za.entries[9].title + '. ' + za.entries[9].summary}
     zl = {"story": za.entries[10].title + '. ' + za.entries[10].summary}
     zm = {"story": za.entries[11].title + '. ' + za.entries[11].summary}
     zn = {"story": za.entries[12].title + '. ' + za.entries[12].summary}
     zo = {"story": za.entries[13].title + '. ' + za.entries[13].summary}
     zp = {"story": za.entries[14].title + '. ' + za.entries[14].summary}
     zq = feedparser.parse('https://feeds.arstechnica.com/arstechnica/index')
     zr = {"story": zq.entries[0].title + '. ' + zq.entries[0].summary}
     zs = {"story": zq.entries[1].title + '. ' + zq.entries[1].summary}
     zt = {"story": zq.entries[2].title + '. ' + zq.entries[2].summary}
     zu = {"story": zq.entries[3].title + '. ' + zq.entries[3].summary}
     zv = {"story": zq.entries[4].title + '. ' + zq.entries[4].summary}
     zw = {"story": zq.entries[5].title + '. ' + zq.entries[5].summary}
     zx = {"story": zq.entries[6].title + '. ' + zq.entries[6].summary}
     zy = {"story": zq.entries[7].title + '. ' + zq.entries[7].summary}
     zz = {"story": zq.entries[8].title + '. ' + zq.entries[8].summary}
     zza = {"story": zq.entries[9].title + '. ' + zq.entries[9].summary}
     zzb = {"story": zq.entries[10].title + '. ' + zq.entries[10].summary}
     zzc = {"story": zq.entries[11].title + '. ' + zq.entries[11].summary}
     zzd = {"story": zq.entries[12].title + '. ' + zq.entries[12].summary}
     zze = {"story": zq.entries[13].title + '. ' + zq.entries[13].summary}
     zzf = {"story": zq.entries[14].title + '. ' + zq.entries[14].summary}
     zzg = feedparser.parse('https://www.wgrz.com/feeds/syndication/rss/news/local')
     zzh = {"story": zzg.entries[0].title + '. ' + zzg.entries[0].summary}
     zzi = {"story": zzg.entries[1].title + '. ' + zzg.entries[1].summary}
     zzj = {"story": zzg.entries[2].title + '. ' + zzg.entries[2].summary}
     zzk = {"story": zzg.entries[3].title + '. ' + zzg.entries[3].summary}
     zzl = {"story": zzg.entries[4].title + '. ' + zzg.entries[4].summary}
     zzm = {"story": zzg.entries[5].title + '. ' + zzg.entries[5].summary}
     zzn = {"story": zzg.entries[6].title + '. ' + zzg.entries[6].summary}
     zzo = {"story": zzg.entries[7].title + '. ' + zzg.entries[7].summary}
     zzp = {"story": zzg.entries[8].title + '. ' + zzg.entries[8].summary}
     zzq = {"story": zzg.entries[9].title + '. ' + zzg.entries[9].summary}
     return JsonResponse((zb,zc,zd,ze,zf,zg,zh,zi,zj,zk,zl,zm,zn,zo,zp,zr,zs,zt,zu,zv,zw,zx,zy,zz,zza,zzb,zzc,zzd,zze,zzf,zzh,zzi,zzj,zzk,zzl,zzm,zzn,zzo,zzp,zzq), safe=False)
