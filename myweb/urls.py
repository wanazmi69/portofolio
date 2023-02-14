
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path(r'', views.index, name='homepage'),
    path(r'projects/', views.project, name='projects'),
    path(r'projects/curriculum-vitae/', include('Apps.CurriculumVitae.urls'), name='curriculumvitae'),
    path(r'projects/curriculum-vitae/login-user/', include('Users.urls'), name='mylogin'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'myweb.views.error_404_view'