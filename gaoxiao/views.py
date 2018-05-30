from django.shortcuts import render
from django.http import JsonResponse
import requests
# Create your views here.

import sqlite3

def index(request):
    print()
    page = request.GET.get('page')
    print(page)
    print(type(page))
    print('Iloveyou')
    if page:

        page = int(page)
        if page > 700:
            page = 1
        # response = requests.get(
        #     "http://api.jisuapi.com/xiaohua/pic?pagenum={}&pagesize=300&sort=addtime&appkey=bd503bec9b3904e8".format(str(page+1))).json()

        con = sqlite3.connect('imgs.db')
        cursor = con.cursor()
        sql = "select * from image limit {},{}".format(page*20,page*20+20)
        cursor.execute(sql)
        list = cursor.fetchall()
        print(list)
        print(list)
        return JsonResponse({"page":str(page+1),"list":list},)
    return render(request,'idnex.html')