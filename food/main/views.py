from django.shortcuts import render,redirect, get_object_or_404
from main.models import cate,Items,News
from main.forms import ItemForm,NewsForm

# Create your views here.
def home(req):
    return render (req,'home.html')



def catdet(req):
    det = cate.objects.all()
    return render(req,'category.html',{'det':det})



def details(req,name):
    detail = cate.objects.get(cat_name=name)
    return render(req,'details.html',{'detail':detail})

def showcat(request,cat_name):
    cat = Items.objects.filter(category= cat_name)
    return render(request,'cat.html',{'cat':cat})




def item_list(req):
    items = Items.objects.all()
    return render(req,'item.html',{'items':items})



def item_form(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'new.html', {'form': form})


def edit_item(request, name):
   
    item = get_object_or_404(Items, name=name)

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)  
        if form.is_valid():
            form.save()
            return redirect('item_list') 
    else:
        form = ItemForm(instance=item)

    return render(request, 'edit_item.html', {'form': form, 'item': item})





def delete_item(request,name):
    demp = Items.objects.get(name=name)
    demp.delete()
    return redirect(item_list)


def news(request):
    n = News.objects.all()
    return render(request,'news.html',{'n':n})
    
def news_form(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = NewsForm()
    return render(request, 'newsadd.html', {'form': form})

def delete_news(request,Title):
    dnews = News.objects.get(Title=Title)
    dnews.delete()
    return redirect(news)


def edit_news(request, Title):
    nws = get_object_or_404(News, Title=Title)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=nws)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = NewsForm(instance=nws)
    return render(request, 'editnews.html', {'form': form, 'nws': nws})

def about(request):
    return render(request,'about.html')
