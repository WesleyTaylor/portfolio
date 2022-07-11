from django.contrib import admin
from django.urls import path, include
from .views import about, contact, home, resume
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path(r'', home, name='home'),
    path(r'about/', about, name='about'),
    path(r'contact/', contact, name='contact'),
    path(r'admin/', admin.site.urls),
    path(r'projects/', include("projects.urls")),
    path(r'blog/', include("blog.urls")),
    path(r'resume/', resume, name='resume'),
]

urlpatterns += staticfiles_urlpatterns()