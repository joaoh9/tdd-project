# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import redirect, render
from lists.models import Item, List

def home_page(request):
    return render(request, 'home.html')

def view_list(request, list_id):
    my_list = List.objects.get(id=list_id)
    items = Item.objects.filter(list=my_list)
    return render(request, 'list.html', {'items': items})
def new_list(request):
    my_list = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=my_list)
    return redirect('/lists/'+ str(my_list.id) + '/')