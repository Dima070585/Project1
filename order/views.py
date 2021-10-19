from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
# Create your views here.
from order.models import ShopCart
from order.forms import ShopCartForm

def add_to_shopcart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    check_product = ShopCart.objects.filter(user_id=current_user.id, products_id=id)

    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if check_product:
                data = ShopCart.objects.get(user_id=current_user.id, products_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.products_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
            return HttpResponseRedirect(url)

    else:
        if check_product:
            data = ShopCart.objects.get(user_id=current_user.id, products_id=id)
            data.quantity +=1
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.products_id = id
            data.save()
        return HttpResponseRedirect(url)

def shopcart(request):
    current_user = request.user
    cart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for item in cart:
        total += item.amount
    return render(request, 'orders/shopcart.html', {'cart': cart, 'total': total})