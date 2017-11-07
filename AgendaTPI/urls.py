"""AgendaTPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.conf.urls import include
from Evntes.views import HomeView
from Evntes.views import CalendarByPeriodView
from django.contrib.staticfiles.urls import static
from schedule.periods import Day
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^$', HomeView, name='home'),
    url(r'^prueba/daily/(?P<calendar_slug>[-\w]+)/$',
        CalendarByPeriodView.as_view(template_name='home.html'),
        name='dayv',
        kwargs={'period': Day}),
    url(r'^eventos/', include('Evntes.urls'), name='eventos'),
    url(r'^auth/', include('myauth.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    url(r'^superadmin/', admin.site.urls),
    url(r'^schedule/', include('schedule.urls'), name='scheduler'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Agenda'
admin.site.site_title = 'Agenda'
