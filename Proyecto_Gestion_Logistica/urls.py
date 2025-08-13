from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App_Usuarios.urls')),
    path('App_LogIn/', include('App_LogIn.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL, 
                      document_root=settings.MEDIA_ROOT)
