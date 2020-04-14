from django.contrib.auth.models import User, Group
from rest_framework import serializers
from karyawan.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class DivisiListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        divisis = [Divisi(**item) for item in validated_data]
        print divisis
        return Divisi.objects.bulk_create(divisis)

class DivisiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divisi
        fields = ['nama', 'keterangan'];

class JabatanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jabatan
        fields = ['nama', 'keterangan'];

class KaryawanSerializer(serializers.ModelSerializer):
    divisi = DivisiSerializer().data;
    jabatan = JabatanSerializer().data;

    class Meta:
        model = Karyawan
        fields = ['id','nama', 'alamat', 'jenis_kelamin', 'jenis_karyawan', 'no_telepon', 'email', 'no_rekening', 'pemilik_rekening', 'jabatan', 'divisi',];
