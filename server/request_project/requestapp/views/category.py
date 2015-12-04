# coding: utf-8
from django.shortcuts import render, redirect
from django.views.generic.base import View
from requestapp.forms.category import FormCategory
from requestapp.models import Category
from rest_framework.views import APIView
from requestapp.serializer import CategorySerializer
from .json_response import JSONResponse


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

            return redirect('/')

        return render(request, self.template, {'form': form})


'''class CategoryListView(View):

    template_name = 'category/list.html'

    def __page(self, request):
        search = ''

        if request.method == 'POST':

            if 'search' in request.POST:
                search = request.POST['search']
        else:

            if 'search' in request.GET:
                search = request.GET['search']
        try:
            page = int(request.GET.get('page', 1))

        except:
            page = 1

        categories_page = Category.objects.get_page(page, search)

        return render(request, self.template_name, {'categories': categories_page, 'search': search})

    def get(self, request):
        return self.__page(request)

    def post(self, request):
        return self.__page(request)'''


class CategoryListRestView(APIView):

    def get(self, request):

        category_page = Category.objects.get_page(1,'')
        categories = CategorySerializer(list(category_page), many=True)
        print(categories.data)
        page = {'num_pages': category_page.paginator.num_pages, 'number': category_page.number, 'categories': categories.data}


        return JSONResponse(page)

    def post(self, request):

        print(request.POST['search'])
        print(request.POST['page'])
        category_page = Category.objects.get_page(request.POST['page'],request.POST['search'])
        categories = CategorySerializer(list(category_page), many=True)

        page = {'num_pages': category_page.paginator.num_pages, 'number': category_page.number, 'categories': categories.data}

        return JSONResponse(page)






        return JSONResponse(serializer.data)


class CategoryListView(View):

    template = 'category/list_angular.html'

    def get(self, request):

        items = Category.objects.filter(name='category 2').all()

        print(items)

        return render(request, self.template, {'items_':items})