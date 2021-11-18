from django.contrib import admin
from django.urls import path
from form.views import form , your  # get_form,

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', form, name = "form"),
    # path("get_form/", get_form, name="get_form"),
    path("your/", your, name="your")
]





urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


