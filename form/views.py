from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import myModelForm #youModelForm

def form(request):

    return render(request, "form.html")




# def get_form(request):
#     form = myModelForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     context = {"form": form}
#     return render(request, 'test.html', context)
# this did not work for me so i had to createthe next function
            
def your(request):
    form = myModelForm(request.POST or None)
    print('nice')
    if form.is_valid():
        print('not nice')
        form.save()
        print('greate')
        return redirect('/')
    context = {"form": form}
    return render(request, 'test.html', context)
            