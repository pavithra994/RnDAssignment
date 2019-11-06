from django.shortcuts import render
from .forms import OutputForm

# Create your views here.
def output_page(request):
    form = OutputForm(request.POST or None)
    if form.is_valid():
        # print(form.cleaned_data.get('input_text'))
        output_file = open('C:\\Home\\output.txt','w+')
        output_file.write(form.cleaned_data.get('input_text'))
    return render(request,"output.html",{'form':form})