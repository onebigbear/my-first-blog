#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
file_name：'urls.py '
author：'baobinghuan'
create_time：'2018/9/13'
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    
]