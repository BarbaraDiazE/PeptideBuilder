"""PeptideBuilder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from Build.views import ServerViews, CSVView
from chemical_space.views import ChemicalSpaceView

urlpatterns = [
    #url(r'^$', views.ServerViews.as_view(), name = "home page"),
    url(r'^$', ServerViews.as_view(), name = "home page"),
    url(r'^csv/(?P<csv_name>.+)/$',CSVView.as_view()),
    url(r'^chemspace/', ChemicalSpaceView.as_view()),
    path('admin/', admin.site.urls),
]
