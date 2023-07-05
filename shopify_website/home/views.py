from django.shortcuts import render
import mysql.connector as sql
# Create your views here.

def homeconn(request):
    return render(request, 'home.html')

def productsconn(request):
    # if request.method == 'POST':
    #     print("POST method called")
    #     product_id=request.POST.get('product')
    #     print('product being added to cart',product_id)

    return render(request, 'cart_new.html')

def product_detailsconn(request):
    return render(request, 'product_details.html')

def cartconn(request):
    return render(request, 'cart_new.html')

def store(request):
    # mydb = sql.connect(
    #     host="localhost",
    #     user="root",
    #     password="Sahil$0901",
    #     database="shopify"
    #     )
    # cursor=mydb.cursor
    # products="select * from Products_Consists"
    # cursor.execute(products)
    # content = {'products': products}
    # return render(request, 'store.html', content)
    if request.method == "POST":
        product_id = request.POST.get('product')
        print('product being added to cart', product_id)
        return render(request, 'product.html')
