from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .form import ctreateuserform,userupdateform,profileupdateform
# Create your views here.
def register(request):
    if request.method=='POST':
        form=ctreateuserform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
    else:
        form=ctreateuserform(request.POST)
        
    context={
        'form':form,
     }
    return render(request,'user/register.html',context)
def profile(request):
    return render(request,'dashboard/profile.html')
def profile_update(request):
    if request.method=='POST':
        
        profile_form=profileupdateform(request.POST, request.FILES, instance=request.user.profile)
        if  profile_form.is_valid():
            
            profile_form.save()
            return redirect('profile')
    else:
       
       profile_form=profileupdateform( instance=request.user.profile)
    context={
        'profile_form':profile_form,
     }
    return render(request,'dashboard/profile_updates.html',context)
def user_update(request):
    if request.method=='POST':
        user_form=userupdateform(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            
            return redirect('profile')
    else:
       user_form=userupdateform( instance=request.user)
       
    context={
        'user_form':user_form,
     }
    return render(request,'dashboard/user_update.html',context)

def setting(request):

    return render(request,'dashboard/user_settings.html')    