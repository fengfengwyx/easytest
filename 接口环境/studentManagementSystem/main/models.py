from django.db import models

# Create your models here.

class DepartmentInfo(models.Model):
    dep_id = models.CharField(max_length=10, primary_key=True)
    dep_name = models.CharField(max_length=20)
    master_name = models.CharField(max_length=20)  # 院长
    slogan = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "departments"


class ClassInfo(models.Model):
    cls_id = models.CharField(max_length=10, primary_key=True)
    cls_name = models.CharField(max_length=20)
    master_name = models.CharField(max_length=20)    # 班主任
    slogan = models.CharField(max_length=100, null=True, blank=True)
    dep = models.ForeignKey(DepartmentInfo)

    class Meta:
        db_table = "classes"


class StudentInfo(models.Model):
    stu_id = models.CharField(max_length=20, primary_key=True)
    stu_name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    birthday = models.DateField()
    native = models.CharField(max_length=20)
    cls = models.ForeignKey(ClassInfo)
    dep = models.ForeignKey(DepartmentInfo)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=8, null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)
    note = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = "students"

