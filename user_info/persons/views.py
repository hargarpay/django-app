from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

# Create your views here.
def index(request):
    return render(request, 'persons/index.html')

def lists(request):
    persons = Person.objects.order_by('-created_at')

    context = {
        'persons': persons
    }
    return render(request, 'persons/lists.html', context)

def add(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        
        if form.is_valid():
            try:
                form.save()
                return redirect('/list')
            except:
                pass
        
    else:
        form = PersonForm()
    return render(request, 'persons/add.html', {'form': form})