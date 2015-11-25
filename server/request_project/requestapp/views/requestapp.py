# coding: utf-8
from django.shortcuts import render, redirect
from django.views.generic.base import View
from requestapp.forms.category import FormCategory
from requestapp.models import Category


class IndexView(View):

    template = 'index.html'

    def get(self, request):
        return render(request, self.template)
