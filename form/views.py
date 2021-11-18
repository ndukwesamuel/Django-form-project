from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import myModelForm

def form(request):

    return render(request, "form.html")



def get_form(request):
    form = myModelForm(request.POST or None)
    if form.is_valid():
        form.save()

    context =  {'form':form}
    return render(request, 'test.html',context )
            