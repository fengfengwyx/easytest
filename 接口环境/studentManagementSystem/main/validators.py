#!/usr/bin/env python
# encoding=utf-8
'''
@author: Francis
'''
from rest_framework import serializers

from .models import DepartmentInfo, ClassInfo

def is_dep_exists(value):
    if not DepartmentInfo.objects.filter(pk=value).exists():
        raise serializers.ValidationError('关联的学院对象(dep_id=%s)不存在'%value)

def is_cls_exists(value):
    if not ClassInfo.objects.filter(pk=value).exists():
        raise serializers.ValidationError('关联的班级对象(cls_id=%s)不存在'%value)
