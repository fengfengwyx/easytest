#!/usr/bin/env python
# encoding=utf-8
'''
@author: Francis
'''

#!/usr/bin/env python
# encoding=utf-8
'''
@author: Francis
'''

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import Route, DynamicDetailRoute,DynamicListRoute, DefaultRouter

from .views import DepartmentInfoViewSet, ClassInfoViewSet, StudentInfoViewSet

class CustomRouter(DefaultRouter):
    """
    A router for read-only APIs, which doesn't use trailing slashes.
    """
    routes = [
        # List route.
        Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping={
                'get': 'list',
                'post': 'create',
                'delete': 'list',
            },
            name='{basename}-list',
            initkwargs={'suffix': 'List'}
        ),
        # Dynamically generated list routes.
        # Generated using @list_route decorator
        # on methods of the viewset.
        DynamicListRoute(
            url=r'^{prefix}/{methodname}{trailing_slash}$',
            name='{basename}-{methodnamehyphen}',
            initkwargs={}
        ),
        # Detail route.
        Route(
            url=r'^{prefix}/{lookup}{trailing_slash}$',
            mapping={
                'get': 'retrieve',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy'
            },
            name='{basename}-detail',
            initkwargs={'suffix': 'Instance'}
        ),
        # Dynamically generated detail routes.
        # Generated using @detail_route decorator on methods of the viewset.
        DynamicDetailRoute(
            url=r'^{prefix}/{lookup}/{methodname}{trailing_slash}$',
            name='{basename}-{methodnamehyphen}',
            initkwargs={}
        ),
    ]
departments_router = CustomRouter()
departments_router.register(r'departments', DepartmentInfoViewSet)
# router.register(r'classes', ClassInfoViewSet)
# router.register(r'students', StudentInfoViewSet)

classes_child_router = CustomRouter()
classes_child_router.register(r'classes', ClassInfoViewSet)
# departments_child_router.register(r'students', StudentInfoViewSet)

# classes_router = CustomRouter()
# classes_router.register(r'classes', ClassInfoViewSet)

students_router = CustomRouter()
students_router.register(r'students', StudentInfoViewSet)


# urlpatterns = router.urls
#
# urlpatterns += [
#     url("^{prefix1}/{lookup1}/", include(router.urls)),
#     url("^{prefix1}/{lookup1}/{prefix2}/{lookup2}/", include(router.urls)),
# ]

