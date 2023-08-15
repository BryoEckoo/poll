from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('settings/', views.user_settings, name='settings'),
    path('', views.index, name='index'),
    path('imprint/', views.imprint, name='imprint'),
    path('about/', views.about, name='about'),
    path('licenses/', views.licenses, name='base_licenses'),
    path('technical_info/', views.tecnical, name='technical'),
    path('autocomplete', views.autocomplete, name='base_autocomplete'),
    path('problems', views.problems, name='base_problems'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    

