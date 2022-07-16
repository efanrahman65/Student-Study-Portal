
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from dashboard import views as dash_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('register/', dash_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="dashboard/login.html"), name='login'),


]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
