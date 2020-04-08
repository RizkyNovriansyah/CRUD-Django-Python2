# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from karyawan.models import Karyawan, Jabatan, Divisi
from django import forms

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

# Add - rinop

class KaryawanForm(forms.Form):
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
        required=True,
        widget=forms.RadioSelect,
        choices=JENIS_KELAMIN_CHOICES,
    )
    jenis_karyawan = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
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
            print 'succedsaved'
            karyawan.save()  
            return redirect('/')          
    context = {
        'form':form,

    }
    return render(request, 'add.html', context)

# Detail
def karyawan_detail(request, pk):
    # data = Karyawan.objects.all()
    karyawan = Karyawan.objects.get(id=pk)
    print karyawan.alamat
    return render(request, 'detail.html',{'dataKaryawan':karyawan})
    # return JsonResponse({'data':data})



# Update - asdar
# Delete

def edit(request, id):
    kr_data = Karyawan.objects.get(id=id)

    return render(request,'edit.html',{'kr_data':kr_data})
