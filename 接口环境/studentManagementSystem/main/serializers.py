#!/usr/bin/env python
# encoding=utf-8
'''
@author: Francis
'''
from rest_framework import serializers


from .models import DepartmentInfo, ClassInfo, StudentInfo
from .validators import is_cls_exists, is_dep_exists


class DepartmentInfoSerializer(serializers.ModelSerializer):
    dep_id = serializers.CharField(required=False)

    class Meta:
        model = DepartmentInfo
        fields = "__all__"


class ClassInfoSerializer(serializers.ModelSerializer):
    cls_id = serializers.CharField(required=False)

    dep_id = serializers.CharField(validators=[is_dep_exists])
    class Meta:
        model = ClassInfo
        exclude = ["dep"]


class StudentInfoSerializer(serializers.ModelSerializer):
    stu_id = serializers.CharField(required=False)

    dep_id = serializers.CharField(validators=[is_dep_exists])
    cls_id = serializers.CharField(validators=[is_cls_exists])
    class Meta:
        model = StudentInfo
        exclude = ["dep", "cls"]
