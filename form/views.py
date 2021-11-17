from django.http import HttpResponseRedirect
from django.shortcuts import render

from form.forms import myModelForm

def form(request):

    return render(request, "form.html")

def get_form(request):
    # if request.method == 'POST':
    
    form = myModelForm(request.POST or None)
    if form.is_valid():
        form.save()


    form = "sam"
    context = {
        'form': form
    }

    return render(request , 'form.html', context)
            