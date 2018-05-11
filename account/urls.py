from django.urls import path
from . import views
from .views import UpdateInfoView

app_name='account'

urlpatterns=[
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.register,name='register'),
    path('change_pwd/',views.change_pwd,name='change_pwd'),
    path('my-information/',views.myself,name='my_infomation'),
    path('upload_info/',UpdateInfoView.as_view(),name='upload_info'),
]