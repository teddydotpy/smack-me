from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
    # Public views
    path('', views.Index.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact', views.ContactView.as_view(), name='contact'),

    # Internal Namespaces that will require security
    path("smack/", include("smack.urls", namespace="smack")),
    path('admin/', admin.site.urls),
]
