"""studentManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

import main.urls
import main.views

urlpatterns = [
    url(r'^api/', include(main.urls.departments_router.urls)),
    url(r"^api/departments/(?P<dep_id>\w+)/", include(main.urls.classes_child_router.urls)),
    url(r"^api/departments/(?P<dep_id>\w+)/classes/(?P<cls_id>\w+)/", include(main.urls.students_router.urls)),
    url(r"^.*", main.views.NotFoundView.as_view()),
]