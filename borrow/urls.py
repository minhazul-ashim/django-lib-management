from django.contrib import admin
from django.urls import path, include;
from . import views;
from django.conf import settings;
from django.conf.urls.static import static;

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.ListBorrows.as_view(), name="listBorrows")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)