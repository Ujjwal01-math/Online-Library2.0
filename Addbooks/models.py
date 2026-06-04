from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    book_image = models.ImageField(upload_to='book/')
    book_title=models.CharField(max_length=50)
    book_author=models.CharField(max_length=50,default="Unknown")
    book_des=models.TextField()
    book_pdf=models.FileField(upload_to='pdf/',null=True,blank=True)
    is_rented = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    total_books = models.IntegerField(default=1)

    rented_books = models.IntegerField(default=0)

    renter_type = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    expiry_date = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.book_title
    
class Programming(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    book_image =models.ImageField(upload_to='Programming/')  
    book_title=models.CharField(max_length=50) 
    book_author=models.CharField(max_length=50,default="Unknown")
    book_des=models.TextField()
    book_pdf=models.FileField(upload_to='pdf/',null=True,blank=True)
    is_rented = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    total_books = models.IntegerField(default=1)

    rented_books = models.IntegerField(default=0)

    renter_type = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    expiry_date = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.book_title

class Mystery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    book_image=models.ImageField(upload_to='Mystery/')
    book_title=models.CharField(max_length=50)
    book_author=models.CharField(max_length=50,default="Unknown")
    book_des=models.TextField()
    book_pdf=models.FileField(upload_to='pdf/',null=True,blank=True)
    is_rented = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    total_books = models.IntegerField(default=1)

    rented_books = models.IntegerField(default=0)

    renter_type = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    expiry_date = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.book_title

class history(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    book_image=models.ImageField(upload_to='history/')
    book_title=models.CharField(max_length=50)
    book_author=models.CharField(max_length=50,default="Unknown")
    book_des=models.TextField()
    book_pdf=models.FileField(upload_to='pdf/',null=True,blank=True)
    is_rented = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    total_books = models.IntegerField(default=1)

    rented_books = models.IntegerField(default=0)

    renter_type = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    expiry_date = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.book_title

class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    book_image=models.ImageField(upload_to='Business/')
    book_title=models.CharField(max_length=50)
    book_author=models.CharField(max_length=50,default="Unknown")
    book_des=models.TextField()
    book_pdf=models.FileField(upload_to='pdf/',null=True,blank=True)
    is_rented = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    total_books = models.IntegerField(default=1)

    rented_books = models.IntegerField(default=0)

    renter_type = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    expiry_date = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.book_title

class Electronics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    book_image=models.ImageField(upload_to='Electronics/')
    book_title=models.CharField(max_length=50)
    book_author=models.CharField(max_length=50,default="Unknown")
    book_des=models.TextField()
    book_pdf=models.FileField(upload_to='pdf/',null=True,blank=True) 
    is_rented = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    total_books = models.IntegerField(default=1)

    rented_books = models.IntegerField(default=0)

    renter_type = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    expiry_date = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.book_title   
class Science(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    book_image=models.ImageField(upload_to='Science/')
    book_title=models.CharField(max_length=50)
    book_author=models.CharField(max_length=50,default="Unknown")
    book_des=models.TextField()
    book_pdf=models.FileField(upload_to='pdf/',null=True,blank=True)
    is_rented = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    total_books = models.IntegerField(default=1)

    rented_books = models.IntegerField(default=0)

    renter_type = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    expiry_date = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.book_title 
    
class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    book_image=models.ImageField(upload_to='Story/')
    book_title=models.CharField(max_length=50)
    book_author=models.CharField(max_length=50,default="Unknown")
    book_des=models.TextField()
    book_pdf=models.FileField(upload_to='pdf/',null=True,blank=True)
    is_rented = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    total_books = models.IntegerField(default=1)

    rented_books = models.IntegerField(default=0)

    renter_type = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    expiry_date = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.book_title
        

# class IssuedBook(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     book = models.ForeignKey(book, on_delete=models.CASCADE)
#     status = models.CharField(max_length=20, default="Issued")    

