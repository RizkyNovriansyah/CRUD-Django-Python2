# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from karyawan.models import Karyawan

def karyawan_all(request):
    # data = Karyawan.objects.all()
    # return HttpResponse("test")
    kr_list = []
    for kr in Karyawan.objects.all():
        print kr.nama
        kr_list.append({
            'name' : kr.nama,
            'alamat' : kr.alamat,
        })
    return render(request, 'list.html',{'kr_list':kr_list})
    # return JsonResponse({'data':data})

# Add
# Detail



# Update
# Delete

