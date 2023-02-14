from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



from . import views
urlpatterns = [
    path(r'', views.index, name='homeCv'),
    path(r'mycv', views.mycv, name='mycv'),
    path(r'login', views.LoginUser, name='loginUser'),
    path(r'register', views.RegisterUser, name='registerUser'),
    path(r'create', views.createCV, name='createCV'),
    path(r'logout', views.Logout, name='Logout'),
    path(r'export-pdf', views.exportPDF, name='exportPDF'),
    
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)