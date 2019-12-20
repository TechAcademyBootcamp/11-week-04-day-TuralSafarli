from django.db import models


# Create your models here.

class Author(models.Model):

    fullname=models.CharField ('Ad/Soyad', max_length=255)
    image=models.ImageField('Sekil',upload_to='imagesauthor/',null=True,blank=True)
    gender=models.BooleanField('Cinsiyyet',default=False)
    date_of_birthday=models.DateField('Doguldugu tarix',)
    nationality=models.CharField('Milliyet',max_length=255)
    info=models.TextField('Melumat',default='Yaxsi dram kitablari yazir')


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name= 'Muellif'
        verbose_name_plural= 'Muellifler'
        ordering = ('fullname',)

    def __str__(self):
        return self.fullname






class Category(models.Model):

    title=models.CharField('Basliq', max_length=50)
    


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= 'Kateqoriya'
        verbose_name_plural= 'Kateqoriyalar'
        ordering = ('title',)

    def __str__(self):
        return self.title

class Book(models.Model):
    book_category = models.ManyToManyField(Category,)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField( 'Ad', max_length=255 )
    description = models.TextField('Melumat', default='Recommended Book')
    price = models.DecimalField('Qiymet', max_digits=5, decimal_places=2)
    pagecount = models.IntegerField('Sehife sayi',)
    coverimage = models.ImageField('Uz qabigi', upload_to='images/',null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= 'Kitab'
        verbose_name_plural= 'Kitablar'
        ordering = ('title',)

    def __str__(self):
        return self.title


    



    