from django.shortcuts import render

# Create your views here.
def productsconn(request):
    # if request.method == 'POST':
    #     print("POST method called")
    #     product_id=request.POST.get('product')
    #     print('product being added to cart',product_id)

    return render(request, 'products.html')