# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from karyawan.models import Karyawan, Jabatan, Divisi, Weather
from django import forms
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
import requests

@login_required
def karyawan_all(request):
    # data = Karyawan.objects.all()
    # return HttpR  esponse("test")
    kr_list = []
    for kr in Karyawan.objects.all():
        kr_list.append({
            'name' : kr.nama,
            'alamat' : kr.alamat,
            'id' : kr.id,
        })
    return render(request, 'list.html',{'kr_list':kr_list})
    # return JsonResponse({'data':data})

# Add - rinop

class KaryawanForm(forms.Form):
    # , forms.ModelForm
    class Meta:
        model = Karyawan
        fields = []

    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]

    JENIS_KELAMIN_CHOICES = (
        ('pria', 'Pria'),
        ('wanita', 'Wanita'),
    )

    JENIS_KARYAWAN_CHOICES = (
        ('magang', 'Magang'),
        ('kontrak', 'Kontrak'),
        ('tetap', 'Tetap'),
    )

    JENIS_KARYAWAN_CHOICES = JENIS_KARYAWAN_CHOICES + (('hilih', 'hilih'),)

    DIVISI_INSERTED = ()
    JABATAN_INSERTED = ()
    for div in Divisi.objects.all():
        DIVISI_INSERTED = DIVISI_INSERTED + ((div.nama, div.nama),)

    for jab in Jabatan.objects.all():
        JABATAN_INSERTED = JABATAN_INSERTED + ((jab.nama, jab.nama),)

    nama = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Name"
        })
    )
    alamat = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Alamat"
        })
    )
    jenis_kelamin = forms.ChoiceField(
        choices=JENIS_KELAMIN_CHOICES,
    )
    jenis_karyawan = forms.ChoiceField(
        choices=JENIS_KARYAWAN_CHOICES,
    )
    divisi = forms.ChoiceField(
        choices=DIVISI_INSERTED,
    )
    jabatan = forms.ChoiceField(
        choices=JABATAN_INSERTED,
    )
    no_telepon = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "no_telepon"
        })
    )
    email = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "email"
        })
    )
    no_rekening = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "no_rekening"
        })
    )
    pemilik_rekening = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "pemilik_rekening"
        })
    )

def karyawan_insert(request):
    form = KaryawanForm()
    if request.method == 'POST':
        form = KaryawanForm(request.POST)
        print form.errors
        if form.is_valid():
            karyawan = Karyawan(
                nama=form.cleaned_data["nama"],
                alamat=form.cleaned_data["alamat"],
                jenis_kelamin=form.cleaned_data["jenis_kelamin"],
                jenis_karyawan=form.cleaned_data["jenis_karyawan"],
                no_telepon=form.cleaned_data["no_telepon"],
                email=form.cleaned_data["email"],
                no_rekening=form.cleaned_data["no_rekening"],
                pemilik_rekening=form.cleaned_data["pemilik_rekening"],
                jabatan=Jabatan.objects.get(nama=form.cleaned_data["jabatan"]),
                divisi=Divisi.objects.get(nama=form.cleaned_data["divisi"]),
            )
            print 'succed saved'
            karyawan.save()  
            return redirect('/')          
    context = {
        'form':form,

    }
    return render(request, 'form.html', context)

def look_data_tes():
    w_list = []
    for w in Weather.objects.all():
        w_list.append({
            'nama' : w.nama,
            'ext_id' : w.ext_id,
        })
    print w_list

def inserting_data_tes():
    sampleReq = requests.get('https://samples.openweathermap.org/data/2.5/box/city?bbox=12,32,15,37,10&appid=b6907d289e10d714a6e88b30761fae22');
    json = sampleReq.json()
    list_weather = json['list']

    for w in list_weather:
        print w['name']
        weather = Weather(
            ext_id=w['id'],
            nama=w['name'],
            lng=w['coord']['lon'],
            lar=w['coord']['lat'],
            weather_state=w['main']['temp'],
        )
        weather.save()  
    # Weather
    # print json['cod']

# Detail
def karyawan_detail(request, pk):
    # data = Karyawan.objects.all()
    karyawan = Karyawan.objects.get(id=pk)
    return render(request, 'detail.html',{'dataKaryawan':karyawan})
    # return JsonResponse({'data':data})

def karyawan_delete(request, pk):
    # data = Karyawan.objects.all()
    karyawan = Karyawan.objects.get(id=pk)
    karyawan.delete()
    return redirect('/')   
    # return JsonResponse({'data':data})


# Update - asdar
class KaryawanEditForm(forms.ModelForm): 
    class Meta:
        model = Karyawan
        fields = '__all__'

def edit(request, id):
    kr_data= Karyawan.objects.get(id=id)
    form = KaryawanEditForm(request.POST or None, instance=kr_data)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'form.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pswd = request.POST.get('psw')
        user = authenticate(username=uname, password=pswd)
        if user is not None:
            login(request, user)
            return redirect('/')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

