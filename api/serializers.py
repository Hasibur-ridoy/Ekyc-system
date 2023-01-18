from django.db.models import fields
from rest_framework import serializers
from entries.models import *

class Student_info_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Student_info
        fields = '__all__'