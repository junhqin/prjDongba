from django.shortcuts import render, HttpResponse

# Create your views here.
import os
import numpy as np
import re
from django.core.paginator import Paginator
from app.models import IMG
from django.conf import settings
from django.db import models
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
    items = []
    for file_meaning in file_meaning_list:
        words = file_meaning.split(".")
        # field可以在这里加限制条件
        if (field == 'body' and int(words[0]) % 10 == 1) or (field == 'tool' and int(words[0]) % 10 == 2) or (
                field == 'all') or (field == 'food' and int(words[0]) % 10 == 3) or (
                field == 'cloth' and int(words[0]) % 10 == 4) or (field == 'arch' and int(words[0]) % 10 == 5) or (field == 'action' and int(words[0]) % 10 == 6) or (field == 'weapon' and int(words[0]) % 10 == 7) or (field == 'astronomy' and int(words[0]) % 10 == 8) or (field == 'geo' and int(words[0]) % 10 == 9) or (field == 'math' and int(words[0]) % 10 == 0) or (field == 'animal' and int(words[0]) % 10 == 0) or (field == 'bird' and int(words[0]) % 10 == 0) or (field == 'plant' and int(words[0]) % 10 == 0) or (field == 'religion' and int(words[0]) % 10 == 0):
            items.append({"img": "../static/assets/img/dongba/Image/" + words[0] + ".jpg",
                          "audio": "../static/assets/img/dongba/Audio/" + words[0] + ".wav", "meaning": words[1]})
    page_items = Paginator(items, 40)
    return render(request, "../templates/dictionary.html",
                  {"items": page_items.page(page), "page_num": page_items.num_pages, "field": field, "page": page})


from django.utils import timezone
import hashlib

def translate(request):
    if request.method == "POST":
        user_img = request.FILES.get("upload")
        if user_img:
            time_now = timezone.now()  # 获取当前时间
            print(time_now)
            m = hashlib.md5()
            m.update(str(time_now).encode())  # 给当前时间编码
            time_now = m.hexdigest()
            print(time_now) #编码后的时间
            print(user_img)

            path = os.path.join(settings.MEDIA_ROOT, 'img/' + time_now + user_img.name)
            print(path)
            if user_img.multiple_chunks():
                file_yield = user_img.chunks()
                with open(path,'wb') as f:
                    for buf in file_yield:
                        f.write(buf)
                    else:
                        print("complete huge img write")
            else:
                with open(path,'wb') as f:
                    f.write(user_img.read())
                print("finished small img write")
            path = "/media/img/" + time_now + user_img.name

            return render(request, "../templates/translate.html", {"img": path, "re_img": path})
        # new_img = IMG(
        #     img=request.FILES["upload"],
        #     name=request.FILES["upload"].name
        # )
        # new_img.save()
        return render(request, "../templates/translate.html", {"img": "/static/assets/img/default_user_img.png", "re_img": "/static/assets/img/default_re_img.png"})
    else:
        return render(request, "../templates/translate.html", {"img": "/static/assets/img/default_user_img.png", "re_img": "/static/assets/img/default_re_img.png"})

