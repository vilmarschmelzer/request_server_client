# coding: utf-8
from django.shortcuts import render, redirect
from django.views.generic.base import View
from requestapp.forms.category import FormCategory
from requestapp.models import Category
from rest_framework.views import APIView
from requestapp.serializer import CategorySerializer
from .json_response import JSONResponse
from rest_framework.permissions import IsAuthenticated, AllowAny


class CategorySaveView(View):

    template = 'category/save.html'

    def get(self, request, category_id=None):

        if category_id:
            category = Category.objects.get(pk=category_id)
            form = FormCategory(instance=category)
        else:
            form = FormCategory()

        return render(request, self.template, {'form': form})

    def post(self, request, category_id=None):

        if category_id:
            category = Category.objects.get(pk=category_id)
            form = FormCategory(instance=category, data=request.POST)
        else:

            form = FormCategory(request.POST)

        if form.is_valid():
            form.save(request)

            return redirect('category-list')

        return render(request, self.template, {'form': form})


class CategoryListRestView(APIView):

    permission_classes = (IsAuthenticated, AllowAny)

    def get(self, request):

        category_page = Category.objects.get_page(1,'')
        categories = CategorySerializer(list(category_page), many=True)
        page = {'num_pages': category_page.paginator.num_pages, 'number': category_page.number, 'categories': categories.data}

        return JSONResponse(page)

    def post(self, request):

        category_page = Category.objects.get_page(request.POST['page'],request.POST['search'])
        categories = CategorySerializer(list(category_page), many=True)

        page = {'num_pages': category_page.paginator.num_pages, 'number': category_page.number, 'categories': categories.data}

        return JSONResponse(page)


class CategoryListView(View):

    template = 'category/list_angular.html'

    def get(self, request):

        return render(request, self.template)