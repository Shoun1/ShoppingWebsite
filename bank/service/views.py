from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from service.models import *
from .cart import Cart
# Create (your views here.
def index(request):
    return render(request,'index.html')
    
def insert(request):
    return render(request,'insert.html')

def signupform(request):
        u=person()
        u.email = request.GET['t1']
        u.password = request.GET['t2']
        u.save()
        return redirect('../signin')

def signin(request):
    return render(request,'signin.html')

def signincode(request):
    e = request.GET['t1']
    p = request.GET['t2']
    if person.objects.filter(email=e,password=p):
        return redirect('../index')
    else:
        return render(request,'insert.html')

def get_session_details(request):
    cart_item = ItemsPurchased.objects.last()  
    if not cart_item:
        return HttpResponse("No cart items found.<br>")
    email = cart_item.email
    response=""
    try:
        per = person.objects.get(email=email)
    # Filter CartItems by the email
    except person.DoesNotExist:
        return HttpResponse(f"User with email {email} not found in the Person table.<br>")
    cart_items = ItemsPurchased.objects.filter(email=email).values('name','price')
    response = f"Email: {email}<br>Cart Details:<br>"
    if cart_items.exists():
        for item in cart_items:
            response += f"Product Name: {item['name']}, Price: {item['price']}<br>"
    else:
        response += "No items in the cart.<br>"
    return HttpResponse(response)

def admin_page(request):
    purchases = ItemsPurchased.objects.values('email','name')
    customer_purchase=[]
    for purchase in purchases:
        email = purchase['email']
        name = purchase['name']
        customer_purchase.append({
            'email': purchase['email'],
            'name': purchase['name'],
        })
    return render(request,'admin.html',{'customer_purchase': customer_purchase})
    
def Electronics(request):
    products = Product.objects.all()
    return render(request,'Electronics.html',{'Product':products})

def add_to_cartfirst(request,id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=id)
    cart.add(id=id,product=product)
    return redirect('/updated_cart1')

def add_item(request,id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=id)
    cart.add(id=id,product=product)
    return redirect('/updated_cart1')

def updated_cart1(request):
    prod = Product.objects.all()
    cart = Cart(request)

    cart_items = cart.get_items()
    thisdict = {'quantity': [item['quantity'] for item in cart_items]}
    thislist = {'id':[item['id'] for item in cart_items]}

    #Query set filter
    prod_ids = prod.values_list('id',flat=True)
    prod_names = prod.values('id','name')
    unshopped_items=[]
    cart_ids = [int(id) for sublist in thislist.values() for id in sublist]

    for prod_id in prod_ids:
        if prod_id not in cart_ids: #item not added to cart
            for product in prod_names:
                if product['id'] == prod_id:
                    unshopped_items.append({
                    'id':product['id'],
                    'name': product['name']
                    })

    total = cart.get_total_price()
    context = {'cart_items':cart_items,'thisdict':thisdict,'total':total,'unshopped_items':unshopped_items}
    
    return render(request,'show1.html',context)



def remove_item(request,id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=id)
    #print(id)
    cart.remove(id=id,product=product)
    return redirect('/updated_cart')


def updated_cart(request):
    cart = Cart(request)
    cart_items = cart.get_items()
    thisdict = {'quantity': [item['quantity'] for item in cart_items]}
    total = cart.get_total_price()
    context = {'cart_items':cart_items,'thisdict':thisdict,'total':total}
    return render(request,'show.html',context)


def cart_detail(request):
    cart = Cart(request)
    cart_items = cart.get_items()
    thisdict = {'quantity':[item['quantity'] for item in cart_items]}
    #print(thisdict)
    total = cart.get_total_price()
    context = {'cart_items':cart_items,'thisdict':thisdict,'total':total}
    return render(request,'cart.html',context)


def save(self):
    self.session.modified = True
    print("Session modified:", self.session.get('cart'))  # Print the session cart for debugging

def check_out(request):
    cart = Cart(request)
    cart_items = cart.get_items()
    total = cart.get_total_price()
    thislist = {'id':[item['id'] for item in cart_items]}
    prod = Product.objects.all()
    prod_ids = prod.values_list('id',flat=True)
    prod_names = prod.values('id','name','price')
    cart_ids = [int(id) for sublist in thislist.values() for id in sublist]
    per = person.objects.last() #last logged-in person
    if per is not None:
        for prod_id in prod_ids:
            if prod_id in cart_ids:
                for product in prod_names:
                    if product['id'] == prod_id:
                        cartitem = ItemsPurchased(email=per.email,name=product['name'],price=product['price']) #insert into CartItems
                        cartitem.save()
    else:
        print("no person found to associate with cart items")
    #cart_item.save()
    cartitems = ItemsPurchased.objects.all()
    #for item in cartitems:
     #   print(item.email)
    return render(request,'checkout.html',{'CartItems':cartitems,'total':total})

def clear(request):
    cart = Cart(request)
    cart.clear()
    res="Your cart is empty"
    return HttpResponse(res)
    #return redirect('checkout.html')

