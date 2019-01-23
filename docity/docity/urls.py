from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from qlthuoc import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^product/(?P<product_id>[0-9]+)/$', views.product, name='product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
