from django.shortcuts import render, HttpResponse

# Create your views here.
def input_file(request):
    try:
        input_f = open("C:\\Home\\input.txt")
        # print(input_f.read())
    except FileNotFoundError:
        return render(request,"input.html",{})
    response = HttpResponse(input_f.read())
    response['Content-Disposition'] = 'inline;filename=some_file.txt'
    return response
