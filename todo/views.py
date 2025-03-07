from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# import todo form and models

from .forms import TodoForm
from .models import Todo

###############################################


def index(request, item_id=None):
    if item_id:
        item = get_object_or_404(Todo, id=item_id)
        if request.method == "POST":
            form = TodoForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                messages.success(request, "Item updated successfully!")
                return redirect('todo')
        else:
            form = TodoForm(instance=item)
    else:
        if request.method == "POST":
            form = TodoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('todo')
        else:
            form = TodoForm()

    item_list = Todo.objects.order_by("-date")
    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)


### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')


def update(request, item_id):
    item = get_object_or_404(Todo, id=item_id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Item updated successfully!")
            return redirect('todo')
    else:
        form = TodoForm(instance=item)
    
    page = {
        "forms": form,
        "title": "Update TODO Item",
    }
    return render(request, 'todo/update.html', page)
