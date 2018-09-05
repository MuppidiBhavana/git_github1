from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def new(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            recs = [Account.objects.latest('id')]
            return render(request,'screen2.html',{'records':recs})
        else:
            form = AccountForm()
    else:
        form  = AccountForm()
        return render(request,'new_account.html',{'form':form})
