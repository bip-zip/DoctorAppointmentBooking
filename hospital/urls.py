"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from mainapp import views
from mainapp import urls
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
     path('admin/', admin.site.urls),
    path('',include(('accounts.urls','accounts'), namespace='accounts')),
    path('app/',include(('mainapp.urls','mainapp'), namespace='mainapp')),
    path('doctorsapp/',include(('doctorsapp.urls','doctorsapp'), namespace='doctorsapp')),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


from django.contrib import admin
admin.site.site_header = 'Appointment Nepal'                  # default: "Django Administration"
admin.site.index_title = 'Appointment Nepal'                 # default: "Site administration"
admin.site.site_title = 'Appointment Nepal'                 # default: "Django site admin"