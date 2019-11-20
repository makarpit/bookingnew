"""software URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', views.index, name='Home Page'),
	path('shop/', include('shop.urls')),
	path('blog/', include('blog.urls')),
	path('about', views.about, name='About us Page'),
	path('testimonial/<int:id>', views.testimonial, name='testimonial'),
	path('service/<int:id>', views.service, name='service'),
	path('member', views.member, name='Member Page'),
	path('news/<int:id>', views.news, name='news'),
	path('rules', views.rules, name='Rules Page'),
	path('notifications', views.notifications, name='Notification Page'),
	path('appointment', views.appointment, name='Appointment Page'),
<<<<<<< HEAD
	path('postSubscribeNewsLetter/', views.postSubscribeNewsLetter, name='SubscribeNewsLetter'),
=======
	path('live', views.live, name='Live Streaming Page'),

>>>>>>> 91ad5d2126dce37ea8f97e3a6e7f7cf68ad63a24

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = 'Manav Mandir - Lavkush Ashram'
admin.site.index_title = 'Karauli Sarkar Administration Area'
admin.site.site_title = 'Manav Mandir - Lavkush Ashram'    