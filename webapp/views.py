from django.shortcuts import render,redirect
from webapp.models import contact_db,Register_db,cart_db,proceed_db
from adminapp.models import Category_db,Product_db
from django.contrib import messages
import razorpay



# Create your views here.
def home_page(request):
    products = Product_db.objects.all()
    cat = Category_db.objects.all()
    return render(request,"home.html",{'cat':cat,'products':products})
def about_us(request):
    cat = Category_db.objects.all()
    return render(request,"about_us.html",{'cat':cat})
def contact_page(request):
    cat = Category_db.objects.all()
    return render(request,"contacts.html",{'cat':cat})
def save_message(request):
    if request.method=="POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('message')
        obj = contact_db(Name=a,Email=b,Message=c)
        obj.save()
        return redirect(contact_page)
def products_page(request):
    cat = Category_db.objects.all()
    products=Product_db.objects.all()
    return render(request,"all_products.html",{'products':products, 'cat':cat})
def single_product(request,pro_id):
    cat = Category_db.objects.all()
    product=Product_db.objects.get(id=pro_id)
    return render(request,"single_product.html",{'product':product,'cat':cat})
def filtered_product(request,cat_name):
    cat = Category_db.objects.all()
    data = Product_db.objects.filter(Category_name=cat_name)
    return render(request,"filtered_product.html",{'data':data,'cat':cat})
def signup(request):
    return render(request,"signup.html")
def save_signup(request):
    if request.method=="POST":
        un = request.POST.get('uname')
        em = request.POST.get('email')
        ps = request.POST.get('pass')
        obj= Register_db(Username=un,Email=em,Password=ps)
        obj.save()
        return redirect(reg_login)
def reg_login(request):
    return render(request,"reglogin.html")

def user_login(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        ps = request.POST.get('pass')
        if Register_db.objects.filter(Username=un,Password=ps).exists():
            request.session['Username']=un
            request.session['Password']=ps
            messages.success(request,"Welcome User")
            return redirect(home_page)
        else:
            messages.error(request, "Incorrect Username or Password")
            return redirect(reg_login)
    else:
        # messages.error(request,"")
        return redirect(reg_login)
def user_logout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(home_page)
def save_cart(request):
    if request.method=="POST":
        a = request.POST.get('uname')
        b = request.POST.get('pro_name')
        c = request.POST.get('quantity')
        d = request.POST.get('price')
        e = request.POST.get('total_price')
        obj = cart_db(User_Name=a,Product_Name=b,Quantity=c,Price=d,Total_Price=e)
        obj.save()
        messages.success(request,"product added to cart")
        return redirect(home_page)
def cart_page(request):
    pro = Category_db.objects.all()
    cat = cart_db.objects.filter(User_Name=request.session['Username'])
    subtotal = 0
    shipping = 0
    total = 0
    for i in cat:
        subtotal+=i.Total_Price
        if subtotal>3000:
            shipping = 150
        else:
            shipping = 250
        total = subtotal+shipping
    return render(request,"cart_page.html",{'cat':cat, 'pro':pro,'subtotal':subtotal, 'shipping':shipping,'total':total})

def delete_cart(request,cart_id):
    x = cart_db.objects.filter(id=cart_id)
    x.delete()
    return redirect(cart_page)

def checkout(request):
    pro = Category_db.objects.all()
    cat = cart_db.objects.filter(User_Name=request.session['Username'])
    subtotal = 0
    shipping = 0
    total = 0
    for i in cat:
        subtotal += i.Total_Price
        if subtotal > 3000:
            shipping = 150
        else:
            shipping = 250
        total = subtotal + shipping
    return render(request,"checkout.html",{'cat':cat,'subtotal':subtotal,'shipping':shipping,'total':total,'pro':pro})

def payment_page(request):
    #retrieve proceed db objects with specified Id
    customer = proceed_db.objects.order_by('-id').first()
   #gwt the payment amount of specified customer
    payy = customer.total_price
    #convert amount to paisa (smallest currency unit)
    amount = int(payy * 100)
    payy_str = str(amount)
    #printing each character of payment amount
    for i in payy_str:
        print(i)
    if request.method=="POST":
        order_currency= 'INR'
        client = razorpay.Client(auth=('rzp_test_tZXamsZNO4haBn','RizqSupC6vtioVddMdRwEKsj'))
        payment = client.order.create({'amount':amount, 'currency':order_currency})
    return render(request,"payment.html",{'customer':customer,'payy_str':payy_str})

def checkout_save(request):
    if request.method == "POST":
        a = request.POST.get('firstname')
        b = request.POST.get('lastname')
        c = request.POST.get('country')
        d = request.POST.get('address')
        e = request.POST.get('town')
        f = request.POST.get('state')
        g = request.POST.get('pin')
        h = request.POST.get('phone')
        i = request.POST.get('email')
        j = request.POST.get('price')
        obj = proceed_db(First_Name=a,Last_Name=b,Country=c,Address=d,Town=e,State=f,Pincode=g,Phone=h,Email=i,total_price=j)
        obj.save()
        return redirect(payment_page)





