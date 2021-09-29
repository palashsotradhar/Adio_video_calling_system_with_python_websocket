from django.shortcuts import render,HttpResponse,redirect
from chat.registration import RegistrationFrom
from django.contrib.auth.decorators import login_required

@login_required
def main_view(request):
    context = {}
    return  render(request,'chat/main.html',context=context)

def login_view(request):
    return HttpResponse("Its a login site")


def registration(request):
    if request.method == 'POST':
        form = RegistrationFrom(request.POST or None)
        if form.is_valid():

            form.save()
            print("saved succesfully")

            return redirect("/home")

        else:
            print(form.errors)

    else:
        form = RegistrationFrom()
        args = {"form" : form}
        return render(request,"chat/registration.html",args)


    return render(request,"chat/registration.html")


