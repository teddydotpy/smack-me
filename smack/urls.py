from django.urls import path
from . import views

app_name = 'smack'

urlpatterns = [
    path('<str:id>/*', views.SmackView.as_view(), name='dashboard'),
    path('forgot/', views.ForgotView.as_view(), name='forgot'),
    path('click/', views.ClickView.as_view(), name='click'),
]