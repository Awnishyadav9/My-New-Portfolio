
from django.contrib import admin
from django.urls import path
from Portfolio import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.first)
]
