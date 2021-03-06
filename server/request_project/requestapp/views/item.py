# coding: utf-8
from django.shortcuts import render, redirect
from django.views.generic.base import View
from requestapp.forms.item import FormItem
from requestapp.models import Item


class ItemSaveView(View):

    template = 'item/save.html'

    def get(self, request, item_id=None):

        if item_id:
            item = Item.objects.get(pk=item_id)
            form = FormItem(instance=item)
        else:
            form = FormItem()

        return render(request, self.template, {'form': form})

    def post(self, request, item_id=None):

        if item_id:
            item = Item.objects.get(pk=item_id)
            form = FormItem(instance=item, data=request.POST)
        else:

            form = FormItem(request.POST)

        if form.is_valid():
            form.save(request)

            return redirect('/')

        return render(request, self.template, {'form': form})


class ItemListView(View):

    template_name = 'item/list.html'

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

        items_page = Item.objects.get_page(page, search)

        return render(request, self.template_name, {'items': items_page, 'search': search})

    def get(self, request):
        return self.__page(request)

    def post(self, request):
        return self.__page(request)
