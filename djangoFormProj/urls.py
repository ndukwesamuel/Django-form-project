from django.contrib import admin
from django.urls import path
from form.views import form , get_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', form, name = "form"),
    path("get_form/", get_form, name="get_form")
]