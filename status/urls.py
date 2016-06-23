# -*- coding: utf-8 -*-
"""
URLs.
"""
from django.conf.urls import patterns, url

from status.views import ProviderAPIView, RootAPIView
from status import settings

urlpatterns = patterns('')

providers = [url(r'^{}/{}/?$'.format(settings.URL_PREFIX, a),
                 ProviderAPIView.as_view(provider=p, provider_args=args, provider_kwargs=kwargs),
                 name='{}_{}'.format(settings.URL_PREFIX, a))
             for a, p, args, kwargs in settings.CHECK_PROVIDERS]

urlpatterns += providers

urlpatterns += [url(r'^{}/?$'.format(settings.URL_PREFIX), RootAPIView.as_view())]
