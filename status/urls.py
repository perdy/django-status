# -*- coding: utf-8 -*-
"""
URLs.
"""
from django.conf.urls import patterns, url

from status.views import ProviderAPIView, RootAPIView
from status import settings

urlpatterns = patterns('')

app_name = 'status'
providers = [url(r'^{}/?$'.format(a),
                 ProviderAPIView.as_view(provider=p, provider_args=args, provider_kwargs=kwargs),
                 name=a)
             for a, p, args, kwargs in settings.CHECK_PROVIDERS]

urlpatterns += providers

urlpatterns += [url(r'^$', RootAPIView.as_view())]
