from django.shortcuts import render
from bookapp.models import *




def t1():
    a = Book.objects.all()
    b =  Category.objects.all()
    c =  Author.objects.all()

def t2():
    a = Book.objects.filter(price__lt=15)
    print(a)

def t3():
    a=Author.objects.filter(date_of_birthday__year__range=[1900,1999])
    print (a)

def t4():
    a=Book.objects.filter(title__icontains='a')
    b=Category.objects.filter(title__icontains='a')
    print(a)
    print(b)
def t5():
    a=Author.objects.filter(fullname="Dostoyekvski")
    print(a)
def t6():
    a=Author.objects.exclude(nationality="British")
    print(a)
def t7():
    a=Book.objects.filter(author__fullname__startswith="D")
def t8():
    a=Book.objects.filter(author__gender=True)
    print(a)
def t9():
    a=Book.objects.filter(book_category__title__endswith='e')
    print(a)
def t10():
    a=Book.objects.filter(id=3)
    print(a)
def hw2_1():
    books = Book.objects.all().update(category='update')
    print(books)
def hw2_2():
    books = Book.objects.filter(author__gender=2).update(price=13.8)
    print(books)
def hw2_3():
    books = Book.objects.all().delete(page_count__gte=200)
    print(books)
def hw2_4():
    authors = Author.objects.filter(fullname__icontains='a').order_by(date_of_birthday)
    print(authors)
def hw2_5():
    books = Book.objects.all().distinct()
    print(books)
def hw2_6():
    new_author = Author.objects.get(id=1)
    books, created = Book.objects.get_or_create(
        author = new_author, title="Tech Academy", description="XXX", price=112, page_count=235, cover_image = "/images/1.jpeg"
        )
    if created:
        cat1 = Category.objects.get(id=2)
        cat2 = Category.objects.get(id=3)
        books.category.add(cat1,cat2)
    print(books)
def hw2_7():
    books = Book.objects.filter(category__title='Novel').count()
    print(books)
def hw2_8():
    book = Book.objects.first()
    print(books)
    authors = Author.objects.last()
    print(authors)
def hw2_9():
    books = Book.objects.order_by('id').reverse()[:3]
    print(books)
def hw2_10():
    price_sum = Book.objects.aggregate(Sum('price'))
    print(price_sum)
    price_avg = Book.objects.aggregate(Avg('price'))
    print(price_avg)
def hw2_11():
    pass
def hw2_12():
    page = Book.objects.filter(page_count__lt=200)
    print(page)
    price = Book.objects.filter(price__gt=15)
    print(price)
















