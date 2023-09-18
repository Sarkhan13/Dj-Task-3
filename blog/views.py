from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from .models import bloglar
from .forms import blogform



# Create your views here.

def home(request):
    form = bloglar.objects.all()

    data = {
        'forms': form
    }

    return render(request, 'main.html',data)

def blog_create(request):
    if request.method == 'POST':
        form = blogform(request.POST or None)
        if form.is_valid():
            form.save()

            return redirect(home)
        else:
            return HttpResponse('alinmadi')
        
    else:
        form = blogform()
        contex = {
            'form':form
        }

        return render(request, 'create.html',contex)
    

def detail(request, id):
    form = bloglar.objects.get(id=id)

    contex = {
        'form': form
    }

    return render(request, 'detail.html',contex)


def update(request,id):
    form = get_object_or_404(bloglar, id=id)
    if request.method == 'POST':
        forma = blogform(request.POST or None, instance=form)
        if forma.is_valid():
            form.save()

            redirect(home)

        else: 
            return HttpResponse('update alinmadi')

    else:
        forma = blogform()
        contex = {
            'form':forma
        }

        return render(request, 'update.html',contex)
    

def delete(request,id):
    form = bloglar.objects.get(id=id)

    form.delete()
    return redirect(home)