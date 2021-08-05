from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, ParseError
from django.shortcuts import redirect

from .models import DepartmentInfo, ClassInfo, StudentInfo
from .serializers import DepartmentInfoSerializer, ClassInfoSerializer, StudentInfoSerializer


class BaseModelViewSet(viewsets.ModelViewSet):
    model = None
    query_fields = []
    must_fields = []
    should_fields = []
    foreign_fields = []
    pkField = ""

    http_method_names = ['get', 'post', 'put', 'delete']

    def filter_list(self, kwargs):
        dep_id = kwargs.get("dep_id")
        cls_id = kwargs.get("cls_id")
        if dep_id and cls_id:
            self.queryset = self.queryset.filter(dep_id=dep_id, cls_id=cls_id)
            if not self.queryset.exists():
                raise NotFound("未找到学院为(dep_id=%s)、班级为(cls_id=%s)的学生对象" % (dep_id, cls_id))
        elif dep_id and cls_id == None:
            self.queryset = self.queryset.filter(dep_id=dep_id)
        elif dep_id == None and cls_id:
            self.queryset = self.queryset.filter(cls_id=cls_id)
        else:
            return
        error_messages = ""

        if dep_id:
            if not DepartmentInfo.objects.filter(dep_id=dep_id).exists():
                error_messages += "未找到学院对象(dep_id=%s)。"%dep_id
        if cls_id:
            if not ClassInfo.objects.filter(cls_id=cls_id).exists():
                error_messages += "未找到班级对象(cls_id=%s)不存在。"%cls_id

        if error_messages != "":
            raise NotFound(error_messages)

    def filter_create_update(self, data, kwargs):
        dep_id = kwargs.get("dep_id")
        cls_id = kwargs.get("cls_id")
        error_messages = ""
        if dep_id:
            if type(data) == dict:
                data["dep_id"] = dep_id
            elif type(data) == list:
                for d in data:
                    d["dep_id"] = dep_id
            if not DepartmentInfo.objects.filter(dep_id=dep_id).exists():
                error_messages += "学院对象(dep_id=%s)不存在。" % dep_id
        if cls_id:
            if type(data) == dict:
                data["cls_id"] = cls_id
            elif type(data) == list:
                for d in data:
                    d["cls_id"] = cls_id
            if not ClassInfo.objects.filter(cls_id=cls_id).exists():
                error_messages += "班级对象(cls_id=%s)不存在。" % cls_id
        if error_messages != "":
            raise NotFound(error_messages)

    def list(self, request, *args, **kwargs):
        self.filter_list(kwargs)

        blur = request.query_params.get("blur")
        blur = True if blur == "1" else False

        fieldKeyword = {}
        for field in self.query_fields:
            params = request.query_params.get(field)
            if params:
                if blur:
                    fieldKeyword[field+"__contains"] = params
                else:
                    fieldKeyword[field] = params

        fieldList = {}
        for field in self.query_fields+[self.pkField]:
            params = request.query_params.get("$"+field+"_list", "")
            if params:
                if blur:
                    fieldList[field+"__contains"] = params.split(",")
                else:
                    fieldList[field] = params.split(",")

        # if fieldList.get(self.pkField):
        #     try:
        #         fieldList[self.pkField] = [int(i) for i in fieldList[self.pkField]]
        #     except:
        #         raise ParseError("无效的参数：%s_list '%s'"%(self.pkField, request.query_params.get("$%s_list"%self.pkField)))
        #         # return Response({"detail": "Parameter %sList '%s' is invalid, please checkout"%(self.pkField, request.query_params.get("$%sList"%self.pkField))},status=status.HTTP_400_BAD_REQUEST)

        if request.method == "DELETE":
            if not fieldList.get(self.pkField):
                raise ParseError("请提供有效的参数：'$%s_list'"%self.pkField)
                # return Response({"detail":"Please provide valid parameter '$%sList'"%self.pkField},status=status.HTTP_400_BAD_REQUEST)
            for _id in fieldList[self.pkField]:
                if not self.model.objects.filter(pk=_id).exists():
                    raise NotFound("未找到对象：%s"%_id)
                    # return Response({"detail":"Object not found which id is %d"%_id}, status=status.HTTP_404_NOT_FOUND)
            for _id in fieldList[self.pkField]:
                obj = self.model.objects.filter(pk=_id)[0]
                obj.delete()
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)

        elif request.method == "GET":

            if fieldKeyword:
                print(fieldKeyword)
                self.queryset = self.queryset.filter(**fieldKeyword)
                
            results = []
            for f,l in fieldList.items():
                print(f,l)
                # for v in l:
                #     if not self.queryset.filter(**{f:v}).exists():
                #         raise NotFound("未找到对象：%s"%str(v))
                        # return Response({"detail": "Object not found which pk is %s"%str(v)}, status=status.HTTP_404_NOT_FOUND)
                for v in l:
                    obj = self.queryset.filter(**{f:v})
                    results += obj

            if fieldList:
                self.queryset = self.queryset.filter(pk__in=[getattr(i,self.pkField) for i in results])
                
        return super(BaseModelViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        dataList = request.data.get("data", [])
        _ = request.data.get("data",[])
        if type(_) == list:
            for i in _:
                if type(i) != dict:
                    raise ParseError("请求体参数格式错误。")
        else:
            dataList = []

        self.filter_create_update(dataList, kwargs)
        
        already_exists = []
        for data in dataList:
            if data.get(self.pkField):
                if self.model.objects.filter(pk=data.get(self.pkField)).exists():
                   already_exists.append(data)

        for _ in already_exists:
            dataList.remove(_)

        serializer_need_to_be_created = []
        for data in dataList:
            serializer = self.get_serializer(data=data)
            serializer.fields.get(self.pkField).required = True
            serializer.is_valid(raise_exception=True)
            serializer_need_to_be_created.append(serializer)

        created_success_data = []
        for serializer in serializer_need_to_be_created:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            created_success_data.append(serializer.data)

        results = {
            "already_exist": {
                "count": len(already_exists),
                "results": already_exists,
            },
            "create_success": {
                "count": len(created_success_data),
                "results": created_success_data
            }
        }
        _status = status.HTTP_200_OK if len(created_success_data)==0 else status.HTTP_201_CREATED
        return Response(results, status=_status)

    def update(self, request, *args, **kwargs):
        self.filter_create_update(request.data, kwargs)

        _ = request.data.get("data")
        if type(_) == list:
            data = _[0] if len(_)>=1 else {}
            data = data if type(data)==dict else {}
        else:
            data = {}

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        self.filter_create_update(request.data, kwargs)
        return super(BaseModelViewSet, self).retrieve(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        self.filter_create_update(request.data, kwargs)
        return super(BaseModelViewSet, self).destroy(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        if serializer.validated_data.get(self.pkField):
            serializer.validated_data.pop(self.pkField)
        serializer.save()


class DepartmentInfoViewSet(BaseModelViewSet):
    model = DepartmentInfo
    query_fields = ["master_name", "dep_name", "slogan"]
    must_fields = ["dep_id","dep_name", "master_name"]
    should_fields = ["slogan"]
    pkField = "dep_id"

    queryset = DepartmentInfo.objects.all()
    serializer_class = DepartmentInfoSerializer


class ClassInfoViewSet(BaseModelViewSet):
    model = ClassInfo
    query_fields = ["cls_name", "master_name", "dep", "slogan"]
    must_fields = ["cls_id", "cls_name", "master_name", "dep"]
    should_fields = ["slogan"]
    pkField = "cls_id"

    queryset = ClassInfo.objects.all()
    serializer_class = ClassInfoSerializer


class StudentInfoViewSet(BaseModelViewSet):
    model = StudentInfo
    query_fields = ["stu_name", "gender", "birthday", "native", "cls_id", "dep_id", "phone_number", "address", "zipcode", "email", "note"]
    must_fields = ["stu_name", "gender", "birthday", "native", "cls_id", "dep_id"]
    should_fields = ["phone_number", "address", "zipcode", "email", "note"]
    pkField = "stu_id"

    queryset = StudentInfo.objects.all()
    serializer_class = StudentInfoSerializer


class NotFoundView(views.APIView):
    http_method_names = ['get', 'post', 'put', 'delete']

    def get(self, request):
        if not request.path.endswith("/"):
            if "?" in request.get_raw_uri():
                return redirect(request.get_raw_uri().replace("?","/?"))
            else:
                return redirect(request.path+"/")
        raise NotFound

    def post(self, request):
        if not request.path.endswith("/"):
            raise NotFound("POST请求uri请以'/'结尾")
        raise NotFound

    def put(self, request):
        if not request.path.endswith("/"):
            raise NotFound("PUT请求uri请以'/'结尾")
        raise NotFound

    def delete(self, request):
        if not request.path.endswith("/"):
            if "?" in request.get_raw_uri():
                return redirect(request.get_raw_uri().replace("?","/?"))
            else:
                return redirect(request.path+"/")
        raise NotFound
