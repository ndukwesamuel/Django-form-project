from django.contrib import admin
from django.urls import path
from form.views import form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', form, name = "form"),
]
