from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.shortcuts import render
from blog.models import Employee,Blog,Author,Book

def index(req,id): #id为URL传递进来的参数 (?P<id>\d{2})
    user={'name':'lihe','age':23}
    # user=['a','b']
    return render(req,'moban1.html',{'title':'my page','user':user,'id':id})
    # return render(req,'moban1.html',{'title':'主页'})
def insert(req,name):
    # emp=Employee(name=name)
    # emp.save() #第一种方式
    emp = Employee.objects.create(name=name) #第二种方式
    print(emp)
    return render(req,'index.html',{'name':name})
def insert2(req,name):
    print(name)
    emp = Employee.objects.create(name=name)
    blog = Blog.objects.create(name=name+'_blog',employee=emp) #表关联插入事要指定关联记录
    print(blog)
    return render(req,'index.html',{'name':name+'_blog'})

def select(req):
    emps=Employee.objects.all()
    for item in emps:
        print(item.id,item.name)
    print(len(emps))
    return render(req,'select.html',{'name':emps})

def select2(req,name):
    print(name)
    blog1=Blog.objects.filter(employee__name=name)  #正向查
    return render(req,'select.html',{'name':blog1})

def createauthor(req,name):
    au=Author.objects.create(name=name)
    return render(req,'index.html',{'name':au})
def selectauthorall(req):
    au=Author.objects.all()
    return render(req,'select.html',{'name':au})
def addbook(req,name,author):
    book1=Book.objects.create(name=name)
    authors=Author.objects.get(name__exact=author)
    print(authors)
    book1.authors.add(authors)
    print(book1.authors.all())
    return render(req,'index.html',{'name':book1})

def select0(req,name):
    print(name)
    book1=Book.objects.filter(name=name).first()
    print(book1)
    au=book1.authors.all()
    return render(req,'select.html',{'name':au})

def update(req,name,auther):
    print(name,auther)
    book1=Book.objects.filter(name=name).first()
    print(book1)
    au=book1.authors.set([2])
    return render(req,'select.html',{'name':au})