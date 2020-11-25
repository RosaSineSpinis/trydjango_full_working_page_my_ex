from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.


# def product_create_view(request):
#     '''function below handle RawProductForm, which shows that we can adjust it to ProductForm'''
#     '''ProductForm is just shortcut'''
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     '''idea behind this function is to make form to seem like model and show it is the same '''
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#     context = {}
#
#     return render(request, "products/product_create.html", context)


def product_list_view(request):
    queryset = Product.objects.all() #list of all ibject in the database
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)


def product_delete_detail_view(request, my_id):
    '''function modified to use dynamic URL'''
    obj = get_object_or_404(Product, id=my_id)
    if request.method == "POST":
        #confirming delete if we get POST then delete it
        obj.delete()
        return redirect('../../')
    context = {
        'object': obj
    }
    return render(request, "products/product_delete.html", context)


def product_dynamic_detail_view(request, my_id):
    '''function modified to usde dynamic URL'''
    # obj = Product.objects.get(id=my_id)
    #get_object_or_404  is used when we get obj which does not exist and handle the exception
    # try:
    #     obj = Product.objects.get(id=my_id)
    # except Product.DoesNotExist:
    #     raise Http404
    obj = get_object_or_404(Product, id=my_id)
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)


#########################################################
#below are example for RawForm, Form and Model
def product_create_view(request):
    '''idea behind this function is to make form to seem like model and show it is the same '''
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }

    return render(request, "products/product_create.html", context)


def product_detail_view(request):
    '''function for model URL - actually this is useless, as always take id=1, just for learning purpose'''
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }

    return render(request, "products/product_detail.html", context)

