from django.db import models
from django.db.models import Q
from django.core.paginator import Paginator
from django.conf import settings


class ItemManager(models.Manager):

    def get_page(self, page, search):

        if search is not None and search != '':
            items = self.filter(Q(id__icontains=search) | Q(name__icontains=search)|
                                     Q(description__icontains=search) | Q(price__icontains=search)|
                                     Q(category__name__icontains=search))
        else:
            items = self.filter()

        items = items.order_by('name')

        paginator = Paginator(items, settings.PAGE_ROWS)
        try:
            items_page = paginator.page(page)
        except:
            items_page = paginator.page(paginator.num_pages)

        return items_page
