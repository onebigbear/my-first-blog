#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
file_name：'forms.py '
author：'baobinghuan'
create_time：'2018/9/13'
"""
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = ('title', 'text')
		