from django.conf.urls import url
from django.views.generic.list import ListView
# from schedule.feeds import CalendarICalendar, UpcomingEventsFeed
from schedule.models import Calendar
from schedule.periods import Day
from .views import DailyV
from .views import CalendarioP

urlpatterns = [
    url(r'^daily/', DailyV, name='daily',),
    url(r'^calendario/', CalendarioP, name='personal',)]
