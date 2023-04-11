from django.urls import path

from . import views

app_name='blogpost'

urlpatterns = [
	path('',views.home,name='home'),
    path('subscribenow',views.subscribenow,name='subscribenow'),
    path('addblog',views.addblog,name='addblog'),
    path('addcategory/',views.addcategory,name='addcategory'),
]
