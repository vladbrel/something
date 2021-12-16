from django.shortcuts import render, get_object_or_404

# Create your views here.
from .forms import TestUserForm
from .models import Product, Category, TestUser


def product_list(request, category_slug=None): #ф-ция выводит объект товара и показ все о нём
    category=None
    categories=Category.objects.all()
    products=Product.objects.filter(available=True) #фильтрует продукты по доступности
    if category_slug:
        category=get_object_or_404(Category_slug=category_slug)
        products=products.filter(category=category)
    context={'categories':categories, 'products':products}
    return render(request, 'shop/list.html', context) #context то есть сделали
def product_detail(request, id, slug): #ф-ция показ вкратце о продукте, контекстное окошко высвечивает
    product=get_object_or_404(Product, id=id, slug=slug, available=True)
    context={'product':product}
    return render(request, 'shop/detail.html',context)

def testform(request):
    #print(TestUser.objects,get(pk=1))
    form = TestUserForm()
    context = {'form':form}
    #print(request.POST)
    if request.method == 'POST':
        form = TestUserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            allusers=TestUser.objects.all()   #топорный метод. Для того, чтобы нагрузка на сервер приложения была, а не на ДБ
            for i in allusers:
                if i.login == form.cleaned_data['login']:
                    context = {'user':'Такой пользователь есть', 'form':'form'}
                    return render(request, 'shop/form_auth.html', context)
            user = TestUser(**form.cleaned_data)
            user.save()
    return render(request, 'shop/form_auth.html', context)

# for field in save_form.errors:
#            field = str(field["field"})
#            message = str(field["error_message"])
#
#            print "Sale Error Detail"
#            print field
#            print message
