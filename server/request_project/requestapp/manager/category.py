from django.db import models
from django.db.models import Q
from django.core.paginator import Paginator
from django.conf import settings


class CategoryManager(models.Manager):

    def get_page(self, page, search):

        if search is not None and search != '':
            categories = self.filter(Q(id__icontains=search) | Q(name__icontains=search))
        else:
            categories = self.filter()

        categories = categories.order_by('name')

        paginator = Paginator(categories, 1)
        #paginator = Paginator(categories, settings.PAGE_ROWS)
        try:
            categories_page = paginator.page(page)
        except:
            categories_page = paginator.page(paginator.num_pages)

        return categories_page

    def get_actives(self):

        return self.filter(active=True).all()
