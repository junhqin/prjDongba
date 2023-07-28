from django.shortcuts import render, HttpResponse

# Create your views here.
import os
import numpy as np
import re
def home(request):
    return render(request, "../templates/home.html")


def dictionary(request):
    path = "./static/assets/img/dongba/Image/"
    file_list = os.listdir(path)
    pattern = re.compile('.(.+).')
    file_meaning_list = os.listdir("./static/assets/img/dongba/Meaning/")
    items=[]
    for file_meaning in file_meaning_list:
        words=file_meaning.split(".")
        print(words)
        items.append({"img":"../static/assets/img/dongba/Image/" + words[0] +".jpg" , "audio" : "../static/assets/img/dongba/Audio/" + words[0] + ".wav","meaning":words[1]})

    return render(request, "../templates/dictionary.html", {"items": items,"s1":1})

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