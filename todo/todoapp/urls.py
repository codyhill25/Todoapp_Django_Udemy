from django.contrib import admin
from django.urls import path, re_path

from todoapp import views

app_name = 'todoapp'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.IndexView.as_view(),name='index'),
    path('<pk>',views.DetailView.as_view(),name='detail')
]