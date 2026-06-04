from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from Addbooks.models import book
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from django.contrib import messages
from Addbooks.models import book,Programming,Mystery,Science,Electronics,Business,history,Story
from django.contrib.auth.decorators import login_required
import razorpay
from datetime import timedelta
from django.utils import timezone


def Home(request):
  
    return render(request,"homepage.html")
def about(request):
 return render(request,"about.html")
def newhome(request):
 return render(request,"newhome.html")

def payment_page(request):
    client = razorpay.Client(auth=("YOUR_KEY", "YOUR_SECRET"))

    payment = client.order.create({
        "amount": 50000,
        "currency": "INR",
        "payment_capture": 1
    })

    return render(request, "payment.html", {
        "payment": payment
    })


def addbook(request):
    servicesData = book.objects.all().order_by('book_title')   #[:3] <--  for shoowing only 3 results add this [:3]
    data={
     'servicesData':servicesData
    }
    return render(request,"addbook.html",data)
@login_required
def program(request):

   servicesData = Programming.objects.all().order_by('book_title')

   # expired access reset
   for i in servicesData:
      i.available_books = (
         i.total_books - i.rented_books
      )

      if i.expiry_date and i.expiry_date < timezone.now():

         i.is_rented = False
         i.user = None
         i.renter_type = None
         i.expiry_date = None
         i.is_verified = False

         i.save()

   data = {
      'servicesData': servicesData
   }

   return render(request, "programming.html", data)
@login_required
def rent_programming(request, id):

    book = Programming.objects.get(id=id)

    if request.method == "POST":

        renter = request.POST.get("renter_type")

        # STUDENT LIMIT CHECK
        if renter == "student":

            rented_books = Programming.objects.filter(
                user=request.user,
                renter_type="student",
                is_rented=True
            ).count()

            if rented_books >= 3:

                messages.error(
                    request,
                    "Book limit over! Students can rent only 3 books."
                )

                return redirect('/programming-book/')
         # Available books check
        if book.rented_books >= book.total_books:

            messages.error(
                request,
                "No books available."
            )

            return redirect('/programming-book/')


        # Rent count increase
        book.rented_books += 1

        # Save user
        book.user = request.user

        # Save renter type
        book.renter_type = renter
       

        if renter == "student":

            book.is_verified = True

            book.expiry_date = (
                timezone.now() + timedelta(days=2)
            )

        else:

            book.is_verified = False

        book.save()

        return redirect('/programming-book/')

    return render(request, "rent.html", {
        'book': book
    })


@login_required
def mysterybook(request):

   servicesData = Mystery.objects.all().order_by('book_title')

   for i in servicesData:
      i.available_books = (
         i.total_books - i.rented_books
      )

      if i.expiry_date and i.expiry_date < timezone.now():

         i.is_rented = False
         i.user = None
         i.renter_type = None
         i.expiry_date = None
         i.is_verified = False

         i.save()

   data = {
      'servicesData': servicesData
   }

   return render(request, "Mystery.html", data)
@login_required
def rent_mystery(request, id):

    book = Mystery.objects.get(id=id)

    if request.method == "POST":

        renter = request.POST.get("renter_type")

        if renter == "student":

            rented_books = Mystery.objects.filter(
                user=request.user,
                renter_type="student",
                is_rented=True
            ).count()

            if rented_books >= 3:

                messages.error(
                    request,
                    "Book limit over! Students can rent only 3 books."
                )

                return redirect('/Mystery-book/')
         # Available books check
        if book.rented_books >= book.total_books:

            messages.error(
                request,
                "No books available."
            )

            return redirect('/Mystery-book/')


        # Rent count increase
        book.rented_books += 1

        # Save user
        book.user = request.user

        # Save renter type
        book.renter_type = renter
       
        if renter == "student":

            book.is_verified = True

            book.expiry_date = (
                timezone.now() + timedelta(days=2)
            )

        else:

            book.is_verified = False

        book.save()

        return redirect('/Mystery-book/')

    return render(request, "rent.html", {
        'book': book
    })

@login_required
def science(request):

   servicesData = Science.objects.all().order_by('book_title')

   for i in servicesData:
      i.available_books = (
         i.total_books - i.rented_books
      )

      if i.expiry_date and i.expiry_date < timezone.now():

         i.is_rented = False
         i.user = None
         i.renter_type = None
         i.expiry_date = None
         i.is_verified = False

         i.save()

   data = {
      'servicesData': servicesData
   }

   return render(request, "Science.html", data)
@login_required
def rent_science(request, id):

    book = Science.objects.get(id=id)

    if request.method == "POST":

        renter = request.POST.get("renter_type")

        if renter == "student":

            rented_books = Science.objects.filter(
                user=request.user,
                renter_type="student",
                is_rented=True
            ).count()

            if rented_books >= 3:

                messages.error(
                    request,
                    "Book limit over! Students can rent only 3 books."
                )

                return redirect('/Science-book/')
         # Available books check
        if book.rented_books >= book.total_books:

            messages.error(
                request,
                "No books available."
            )

            return redirect('/Science-book/')


        # Rent count increase
        book.rented_books += 1

        # Save user
        book.user = request.user

        # Save renter type
        book.renter_type = renter
       

        if renter == "student":

            book.is_verified = True

            book.expiry_date = (
                timezone.now() + timedelta(days=2)
            )

        else:

            book.is_verified = False

        book.save()

        return redirect('/Science-book/')

    return render(request, "rent.html", {
        'book': book
    })


@login_required
def electronics(request):

   servicesData = Electronics.objects.all().order_by('book_title')

   for i in servicesData:
      i.available_books = (
         i.total_books - i.rented_books
      )

      if i.expiry_date and i.expiry_date < timezone.now():

         i.is_rented = False
         i.user = None
         i.renter_type = None
         i.expiry_date = None
         i.is_verified = False

         i.save()

   data = {
      'servicesData': servicesData
   }

   return render(request, "Electronics.html", data)

@login_required
def rent_electronics(request, id):

    book = Electronics.objects.get(id=id)

    if request.method == "POST":

        renter = request.POST.get("renter_type")

        if renter == "student":

            rented_books = Electronics.objects.filter(
                user=request.user,
                renter_type="student",
                is_rented=True
            ).count()

            if rented_books >= 3:

                messages.error(
                    request,
                    "Book limit over! Students can rent only 3 books."
                )

                return redirect('/Electronics-book/')

         # Available books check
        if book.rented_books >= book.total_books:

            messages.error(
                request,
                "No books available."
            )

            return redirect('/Electronics-book/')


        # Rent count increase
        book.rented_books += 1

        # Save user
        book.user = request.user

        # Save renter type
        book.renter_type = renter

        if renter == "student":

            book.is_verified = True

            book.expiry_date = (
                timezone.now() + timedelta(days=2)
            )

        else:

            book.is_verified = False

        book.save()

        return redirect('/Electronics-book/')

    return render(request, "rent.html", {
        'book': book
    })

@login_required
def business(request):

   servicesData = Business.objects.all().order_by('book_title')

   for i in servicesData:
      i.available_books = (
         i.total_books - i.rented_books
      )

      if i.expiry_date and i.expiry_date < timezone.now():

         i.is_rented = False
         i.user = None
         i.renter_type = None
         i.expiry_date = None
         i.is_verified = False

         i.save()

   data = {
      'servicesData': servicesData
   }

   return render(request, "business.html", data)

@login_required
def rent_business(request, id):

    book = Business.objects.get(id=id)

    if request.method == "POST":

        renter = request.POST.get("renter_type")

        if renter == "student":

            rented_books = Business.objects.filter(
                user=request.user,
                renter_type="student",
                is_rented=True
            ).count()

            if rented_books >= 3:

                messages.error(
                    request,
                    "Book limit over! Students can rent only 3 books."
                )

                return redirect('/Business-book/')
         # Available books check
        if book.rented_books >= book.total_books:

            messages.error(
                request,
                "No books available."
            )

            return redirect('/Business-book/')


        # Rent count increase
        book.rented_books += 1

        # Save user
        book.user = request.user

        # Save renter type
        book.renter_type = renter
        
        if renter == "student":

            book.is_verified = True

            book.expiry_date = (
                timezone.now() + timedelta(days=2)
            )

        else:

            book.is_verified = False

        book.save()

        return redirect('/Business-book/')

    return render(request, "rent.html", {
        'book': book
    })

@login_required
def History(request):

   servicesData = history.objects.all().order_by('book_title')

   for i in servicesData:
      i.available_books = (
         i.total_books - i.rented_books
      )

      if i.expiry_date and i.expiry_date < timezone.now():

         i.is_rented = False
         i.user = None
         i.renter_type = None
         i.expiry_date = None
         i.is_verified = False

         i.save()

   data = {
      'servicesData': servicesData
   }

   return render(request, "History.html", data)

@login_required
def rent_history(request, id):

    book = history.objects.get(id=id)

    if request.method == "POST":

        renter = request.POST.get("renter_type")

        if renter == "student":

            rented_books = history.objects.filter(
                user=request.user,
                renter_type="student",
                is_rented=True
            ).count()

            if rented_books >= 3:

                messages.error(
                    request,
                    "Book limit over! Students can rent only 3 books."
                )

                return redirect('/History-book/')
         # Available books check
        if book.rented_books >= book.total_books:

            messages.error(
                request,
                "No books available."
            )

            return redirect('/History-book/')


        # Rent count increase
        book.rented_books += 1

        # Save user
        book.user = request.user

        # Save renter type
        book.renter_type = renter
      

        if renter == "student":

            book.is_verified = True

            book.expiry_date = (
                timezone.now() + timedelta(days=2)
            )

        else:

            book.is_verified = False

        book.save()

        return redirect('/History-book/')

    return render(request, "rent.html", {
        'book': book
    })

@login_required
def story(request):

   servicesData = Story.objects.all().order_by('book_title')

   for i in servicesData:
      i.available_books = (
         i.total_books - i.rented_books
      )

      if i.expiry_date and i.expiry_date < timezone.now():

         i.is_rented = False
         i.user = None
         i.renter_type = None
         i.expiry_date = None
         i.is_verified = False
        
         i.save()

   data = {
      'servicesData': servicesData
   }

   return render(request, "story.html", data)

@login_required
def rent_story(request, id):

    book = Story.objects.get(id=id)

    if request.method == "POST":

        renter = request.POST.get("renter_type")

        # Student limit check
        if renter == "student":

            rented_books = Story.objects.filter(
                user=request.user,
                renter_type="student"
            ).count()

            if rented_books >= 3:

                messages.error(
                    request,
                    "Book limit over! Students can rent only 3 books."
                )

                return redirect('/Story-book/')


        # Available books check
        if book.rented_books >= book.total_books:

            messages.error(
                request,
                "No books available."
            )

            return redirect('/Story-book/')


        # Rent count increase
        book.rented_books += 1

        # Save user
        book.user = request.user

        # Save renter type
        book.renter_type = renter


        if renter == "student":

            book.is_verified = True

            book.expiry_date = (
                timezone.now() + timedelta(days=2)
            )

        else:

            book.is_verified = False


        book.save()

        return redirect('/Story-book/')


    return render(request, "rent.html", {
        'book': book
    })




def books(request):
 return render(request,"books.html")
def contact(request):
  return render(request,"contact.html")

def login(request):
    if request.method == 'POST':
       email = request.POST.get("email")
       password = request.POST.get("password")

       try:
          value = User.objects.get(email=email)
       except User.DoesNotExist:
          messages.error(request, "User not registered ❌ Please signup first")
          return render(request,"login.html")
       myUser = authenticate(request, username=value.username, password=password)
       if myUser is not None:
          auth_login(request,myUser)
          return redirect("/Mystery-book/")
    return render(request,"login.html")


def signup(request):
    if request.method =='POST':
        user =request.POST.get("username")
        email =request.POST.get("email")
        password =request.POST.get("password")
        password1 =request.POST.get("confirm_password")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered use another email")
            return redirect('/signup/')
        myUser =User.objects.create_user(user,email,password)
        myUser.save()
        messages.success(request, "Signup successful! 🎉 Please login.")
        # return redirect("/login/")
    
    return render(request,"signup.html")