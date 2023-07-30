from django.shortcuts import render, HttpResponse

# Create your views here.
import os
import numpy as np
import re
from django.core.paginator import Paginator


def home(request):

    return render(request, "../templates/home.html")


def dictionary(request):
    page = request.GET.get('page', 1)
    field = request.GET.get('field', 'all')
    print(page, field)
    path = "./static/assets/img/dongba/Image/"
    file_list = os.listdir(path)
    pattern = re.compile('.(.+).')
    file_meaning_list = os.listdir("./static/assets/img/dongba/Meaning/")
    items=[]
    for file_meaning in file_meaning_list:
        words=file_meaning.split(".")
        #field可以在这里加限制条件
        if (field == 'body' and int(words[0]) % 10 == 1) or (field == 'tool' and int(words[0]) % 10 == 2) or (field == 'all' and int(words[0]) % 10 == 3):
            items.append({"img":"../static/assets/img/dongba/Image/" + words[0] +".jpg" , "audio" : "../static/assets/img/dongba/Audio/" + words[0] + ".wav","meaning":words[1]})
    page_items = Paginator(items,40)
    return render(request, "../templates/dictionary.html", {"items": page_items.page(page),"page_num":page_items.num_pages,"field":field,"page":page})


def dictionary_body(request):
    path = "./static/assets/img/dongba/Image/"
    file_list = os.listdir(path)
    pattern = re.compile('.(.+).')
    file_meaning_list = os.listdir("./static/assets/img/dongba/Meaning/")
    items = []
    for file_meaning in file_meaning_list:
        words = file_meaning.split(".")
        print(words)
        if int(words[0])%5==0:
           items.append({"img": "../../static/assets/img/dongba/Image/" + words[0] + ".jpg",
                      "audio": "../../static/assets/img/dongba/Audio/" + words[0] + ".wav", "meaning": words[1]})

    return render(request, "../templates/dictionary_body.html", {"items": items})

def translate(request):
    return render(request,"../templates/translate.html")