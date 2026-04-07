from django.shortcuts import render
from myapp.models import insitute


# Create your views here.
def sum(request):
    if request.method == "POST":
        if request.POST.get("Send") == "Send":

            AA = request.POST.get("A")
            SS = request.POST.get("B")
            DD = request.POST.get("C")

            insitute.objects.create(name=AA, mail=SS, message=DD)

    
    return render(request,"index.html")
