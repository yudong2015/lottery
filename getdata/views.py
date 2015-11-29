from django.shortcuts import render
from django.http import JsonResponse
from models import *
import urllib2
import urllib
import re

# Create your views here.

def get_number(request):
    start = request.GET.get('start','')
    end = request.GET.get('end','')
    
def gethtml(url):
    values={}
    values['selectate']=7
    data = urllib.urlencode(values)
    response = urllib2.urlopen(url + "?selectDate=7")
    return response.read()

def getdata(request):
    html = gethtml("http://trend.caipiao.163.com/cqssc/qianwei.html")
    pattern = re.compile("<tr data-period=\"\d{9}\" data-award=\".{9}")
    items = re.findall(pattern,html)
    new_number = 0
    for item in items:
        li=item.split("\"")
        wei = li[3].split(' ')
        if not CPnumber.objects.filter(qihao=int(li[1])).exists():
            CPnumber.objects.create(qihao=int(li[1]),shuzi=li[3].replace(' ',''),ge=int(wei[0]),shi=int(wei[1]),bai=int(wei[2]),qian=int(wei[3]),wan=int(wei[4]))
            new_number += 1
    return JsonResponse({'items':new_number},status=200)


def analysis(request):
    
