from django.conf import settings
from django.urls import path, include

from .forms import TestUserForm
from .views import product_list, product_detail, testform, testmodelform
from django.conf.urls import url
app_name='shop'
urlpatterns = [
    path('', product_list, name='product_list' ),
    path('testform/', testform, name='testform'),
    path('testmodelform/', testmodelform, name='modelForm'),
    url(r'^(?P<category_slug>[-\w]+)/$', product_list, name='product_list_by_category'), #регулярное выражение . принимает slug и вытаскивает список продуктов по конкретной категории
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', product_detail, name='product_detail'), #  достаёт описание продукта из БД
]

def testmodelform(request):
    form= TestUserForm()
    context = {form}
    return render(request, 'shop/form_auth.html', context)
