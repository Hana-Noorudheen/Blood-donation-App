from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import request,HttpResponse
from . models import donor_details
from django.contrib.auth.models import User,auth
from django.core.paginator import Paginator
from django.http import JsonResponse


# Create your views here.

def index(request):
  return render(request,'index.html')

def homesignup(request):
  return render(request, 'signup.html')

def homelogin(request):
  return render(request, 'login.html')

def homeregister(request):
  return render(request, 'index.html')  

    

List=[]

List_user=[]



def form(request):
  if request.method == 'POST':


    
    donor=donor_details()
    
    donor.Name= request.POST['name']
    donor.Age=request.POST['age']
    donor.Gender=request.POST['gender']
    donor.BloodGroup=request.POST['blood group']
    donor.City= request.POST['City']
    donor.Phone=request.POST['phone']
    donor.Email=request.POST['email']

    donor.save()

    return redirect('/display')



  else:
    return render(request,'index.html')
    


def display(request):

  if request.method == 'POST':
    Name=request.POST['q']
    details=donor_details.objects.filter(Name__icontains=Name)
  else: 
    details=donor_details.objects.all()  

   # Pagination
  paginator=Paginator(details,5)
  page_number=request.GET.get('page')
  details=paginator.get_page(page_number)
  
  if request.session.has_key('username'):
      username = request.session['username']
      return render(request, 'display.html', {"username" : username,'result':details})
  else:
      return render(request, 'login.html')

  


def signup(request):



    if request.method == 'POST':
        Name = request.POST['name']
        Email = request.POST['email']
        Password=request.POST['password']
        ConfirmPassword=request.POST['confirm_password']

        

        if User.objects.filter(email=Email).exists():
              # messages.info(request,'email taken')
              return JsonResponse(

              {'success':True},
              safe=False
              )

        else:
              user = User.objects.create_user(first_name=Name,email=Email,password=Password,username=Email)
              user.save()
              return JsonResponse(

              {'success':False},
              safe=False
              )
                

            

    else:    
        return render(request,'signup.html')





def login(request):

    
    if request.method== 'POST':

        email = request.POST['email']
        password = request.POST['password']

        check_user = auth.authenticate(username=email, password=password)
        
        if check_user:
          request.session['username'] = email
          return JsonResponse(

              {'success':True},
               safe=False
             )

        else:

            
          return JsonResponse(
               {'success':False},
               safe=False
             )      
          

       

        # user = auth.authenticate(username=email, password=password)

        # if user is not None:
        #     auth.login(request,user)
        #     return JsonResponse(

        #       {'success':True},
        #       safe=False
        #     )

        # else:
            
        #     return JsonResponse(

        #       {'success':False},
        #       safe=False
        #     ) 
       
        



    else:
        return render(request, 'login.html') 



def logout(request):
    try:
        del request.session['username']
    except:
        return redirect('login')


    # auth.logout(request)
    return redirect('/login')           










    

 
   







  






  









  
   







  






  









