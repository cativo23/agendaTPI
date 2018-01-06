# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from django.http import (
    Http404, HttpResponseBadRequest, HttpResponseRedirect, JsonResponse,
)
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.six.moves.urllib.parse import quote

from django.views.generic.detail import DetailView
from schedule.views import CalendarMixin
from django.utils.decorators import method_decorator
from schedule.utils import (
    check_calendar_permissions, check_event_permissions,
    check_occurrence_permissions, coerce_date_dict,
)
from schedule.models import Calendar, Event, Occurrence
from schedule.periods import weekday_names
from schedule.periods import Day
from myauth.models import Departamento
from schedule.settings import (
    CHECK_EVENT_PERM_FUNC, CHECK_OCCURRENCE_PERM_FUNC, EVENT_NAME_PLACEHOLDER,
    GET_EVENTS_FUNC, OCCURRENCE_CANCEL_REDIRECT, USE_FULLCALENDAR,
)
from schedule.utils import (
    check_calendar_permissions, check_event_permissions,
    check_occurrence_permissions, coerce_date_dict,
)


class CalendarByPeriodView(CalendarMixin, DetailView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(CalendarByPeriodView, self).get_context_data(**kwargs)
        context['site_name'] = settings.SITE_NAME
        depuser = self.request.user.departament
        if (depuser is None):
            print(depuser)
            return redirect('logout')
        else:
            if self.request.user.is_admin:
                # print(self.request.user.is_admin)
                calendar = Calendar.objects.get(name='root')
            else:
                # print(self.request.user.is_admin)
                calendar = Calendar.objects.get(id=depuser.calendario.id)
        period_class = self.kwargs['period']
        try:
            date = coerce_date_dict(self.request.GET)
        except ValueError:
            raise Http404
        if date:
            try:
                date = datetime.datetime(**date)
            except ValueError:
                raise Http404
        else:
            date = timezone.now()
        event_list = GET_EVENTS_FUNC(self.request, calendar)

        local_timezone = timezone.get_current_timezone()
        period = period_class(event_list, date, tzinfo=local_timezone)

        context.update({
            'date': date,
            'period': period,
            'calendar': calendar,
            'weekday_names': weekday_names,
            'here': quote(self.request.get_full_path()),
        })
        return context


@login_required
def HomeView(request):
    depuser = request.user.departament

    if (depuser is None):
        return redirect('logout')
    else:
        if request.user.is_admin:
            # print(self.request.user.is_admin)
            calendar = Calendar.objects.get(name='root')
        else:
            # print(self.request.user.is_admin)
            calendar = Calendar.objects.get(id=depuser.calendario.id)
    period_class = Day
    try:
        date = coerce_date_dict(request.GET)
    except ValueError:
        raise Http404
    if date:
        try:
            date = datetime.datetime(**date)
        except ValueError:
            raise Http404
    else:
        date = timezone.now()
    event_list = GET_EVENTS_FUNC(request, calendar)

    local_timezone = timezone.get_current_timezone()
    period = period_class(event_list, date, tzinfo=local_timezone)
    return render(request, 'home.html', {
        'site_name': settings.SITE_NAME,
        'date': date,
        'period': period,
        'calendar': calendar,
        'weekday_names': weekday_names,
        'here': quote(request.get_full_path()),
    })


@login_required
def DailyV(request):
    depuser = request.user.departament
    if (depuser is None):
        return redirect('logout')
    else:
        if request.user.is_staff:
            calendar = Calendar.objects.get(name='default')
        else:
            calendar = Calendar.objects.get(id=depuser.calendario.id)
    period_class = Day
    try:
        date = coerce_date_dict(request.GET)
    except ValueError:
        raise Http404
    if date:
        try:
            date = datetime.datetime(**date)
        except ValueError:
            raise Http404
    else:
        date = timezone.now()
    event_list = GET_EVENTS_FUNC(request, calendar)

    local_timezone = timezone.get_current_timezone()
    period = period_class(event_list, date, tzinfo=local_timezone)
    return render(request, 'home.html', {
        'date': date,
        'period': period,
        'calendar': calendar,
        'weekday_names': weekday_names,
        'here': quote(request.get_full_path()),
                                        })


@login_required
def CalendarioP(request):
    calendU = request.user.calendarioUser
    if (calendU is None):
        return redirect('logout')
    else:
        if request.user.is_staff:
            calendar = Calendar.objects.get(name='root')
        else:
            calendar = Calendar.objects.get(id=calendU.id)
    period_class = Day
    try:
        date = coerce_date_dict(request.GET)
    except ValueError:
        raise Http404
    if date:
        try:
            date = datetime.datetime(**date)
        except ValueError:
            raise Http404
    else:
        date = timezone.now()
    event_list = GET_EVENTS_FUNC(request, calendar)

    local_timezone = timezone.get_current_timezone()
    period = period_class(event_list, date, tzinfo=local_timezone)
    print(calendU)
    return render(request, 'calendarioP.html', {
        'date': date,
        'period': period,
        'calendar': calendar,
        'weekday_names': weekday_names,
        'here': quote(request.get_full_path()),
                                        })
