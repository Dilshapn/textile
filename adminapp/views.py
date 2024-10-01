from django.shortcuts import render,redirect
from adminapp.models import Category_db,Product_db
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from webapp.models import contact_db,Register_db
from django.contrib import messages


# Create your views here.
def index_page(request):
    return render(request,"index.html")
def add_category(request):
    return render(request,"add_category.html")
def save_category(request):
    if request.method=="POST":
        a = request.POST.get("name")
        b = request.POST.get("description")
        img = request.FILES['image']
        obj = Category_db(Category_Name=a,Description=b,Image=img)
        obj.save()
        messages.success(request,"Category added Successfully")
        return redirect(add_category)
def display_category(request):
    data = Category_db.objects.all()
    return render(request,"display_category.html",{'data':data})
def edit_category(request,cat_id):
    data = Category_db.objects.get(id=cat_id)
    return render(request,"edit_category.html",{'data':data})
def edit_save(request,cat_id):
    if request.method=="POST":
        a = request.POST.get("name")
        b = request.POST.get("description")
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = Category_db.objects.get(id=cat_id).Image
        Category_db.objects.filter(id=cat_id).update(Category_Name=a,Description=b,Image=file)
        messages.success(request,"Category Edited..!")
        return redirect(display_category)
def delete_category(request,cat_id):
        data=Category_db.objects.filter(id=cat_id)
        data.delete()
        messages.error(request,"Category Deleted Successfully")
        return redirect(display_category)
def add_product(request):
    category=Category_db.objects.all()
    return render(request,"add_products.html",{'Category_Name':category})
def display_product(request):
    data = Product_db.objects.all()
    return render(request,"display_product.html",{'data':data})
def save_product(request):
    if request.method=="POST":
        a = request.POST.get("category")
        b = request.POST.get("name")
        c = request.POST.get("description")
        d = request.POST.get("price")
        e = request.POST.get("brand")
        f = request.FILES['image1']
        g = request.FILES['image2']
        h = request.FILES['image3']
        obj=Product_db(Category_name=a,Product_name=b, Description=c,Price=d,Brand=e,Product_img1=f,Product_img2=g,Product_img3=h)
        obj.save()
        messages.success(request,"Product Added Successfully")
        return redirect(display_product)
def edit_product(request,edit_id):
    cat = Category_db.objects.all()
    data=Product_db.objects.get(id=edit_id)
    return render(request,"edit_product.html",{'data':data, 'cat':cat})
def update_product(request,edit_id):
    if request.method=="POST":
        a = request.POST.get("category")
        b = request.POST.get("name")
        c = request.POST.get("description")
        d = request.POST.get("price")
        e = request.POST.get("brand")
        try:
            img1 = request.FILES['image1']
            fs = FileSystemStorage()
            file1 = fs.save(img1.name, img1)
        except MultiValueDictKeyError:
            file1 = Product_db.objects.get(id=edit_id).Product_img1
        try:
            img2 = request.FILES['image2']
            fs = FileSystemStorage()
            file2 = fs.save(img2.name, img2)
        except MultiValueDictKeyError:
            file2 = Product_db.objects.get(id=edit_id).Product_img2
        try:
            img3 = request.FILES['image3']
            fs = FileSystemStorage()
            file3 = fs.save(img3.name, img3)
        except MultiValueDictKeyError:
            file3 = Product_db.objects.get(id=edit_id).Product_img3
        Product_db.objects.filter(id=edit_id).update(Category_name=a,Product_name=b, Description=c,Price=d,Brand=e,Product_img1=file1,Product_img2=file2,Product_img3=file3)
        messages.success(request,"Edited Successfully")
        return redirect(display_product)
def delete_product(request,edit_id):
    x= Product_db.objects.filter(id=edit_id)
    x.delete()
    messages.error(request,"Product Removed...!")
    return redirect(display_product)
def admin_login(request):
    return render(request,"admin_login.html")
def admin_login_page(request):
    if request.method=="POST":
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                messages.success(request,"Welcome Admin")
                return redirect(index_page)
            else:
                messages.error(request,"Incorrect Username or Password")
                return redirect(admin_login)
        else:
            messages.error(request,"User Not found")
            return redirect(admin_login)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login)
def contact_view(request):
    data = contact_db.objects.all()
    return render(request,"contact_view.html",{'data':data})
def delete_message(request,msg_id):
    data=contact_db.objects.filter(id=msg_id)
    data.delete()
    return redirect(contact_view)
def admin_view_user(request):
    data = Register_db.objects.all()
    return render(request,"admin_view_user.html",{'data':data})



