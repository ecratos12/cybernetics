from django.shortcuts import *
from .models import *
from django.http import JsonResponse
# Create your views here.
def home(request):
    news = News.objects.filter(published =True).order_by('-pub_date')[:2]
    return render(request, 'core/index.html', {'news':news})

def news(request):
    news = News.objects.filter(published=True)
    return render(request, 'core/all-news.html', {'news':news})

def new(request, id):
    new = News.objects.get(id=id)
    news = News.objects.filter(published=True).exclude(id=id)[0:2]
    return render(request, 'core/new.html', {'new':new, 'news':news})

def article(request, slug):
    print(slug)
    article = get_object_or_404(Article, slug=slug)
    if article.parent:
        return render(request, article.parent.nav_bar, {'article':article})
    else:
        return render(request, article.nav_bar, {'article':article})

def personality(request):
	person = Person.objects.all()
	result = [person[i:i+2] for i in range(0, len(person), 2)]
	return render(request, 'core/personality.html', {'result':result})

def administration(request):
    person = Administration.objects.all()
    result = [person[i:i+2] for i in range(0, len(person), 2)]
    return render(request, 'core/administration.html', {'result':result})

def gallery(request):
    photo = Photo.objects.filter(in_gallery = True)
    return render(request, 'core/gallery.html', {'photo':photo})


def departments(request, id):
    departments = Department.objects.get(id=id)
    return render(request, 'core/department.html', {'departments':departments})


def degree(request, id):
    degree = OKR.objects.get(id=id)
    year = list()
    for y in Year.objects.all():
        if not y.number in year:
            year.append(y.number)
    stat = Statistic.objects.filter(okr=degree)
    return render(request, 'core/degree.html', {'degree':degree, 'year':year, "stat":stat})

def schedule(request):
    grup = Grup.objects.all()
    return render(request, 'core/schedule.html', {'grup':grup})

def get_schedule(request):
    g = Grup.objects.get(name=request.GET['g'])
    grup = Schedule_block.objects.filter(grup=g)
    result = {}
    for g in grup:
        result[g.get_date()] = []
        for p in g.get_para():
            result[g.get_date()].append([p.number, p.name, p.professor, p.adress])
    print (result)
    return JsonResponse(result)

def contacts(request):
    contacts = Contacts.objects.all()
    return render(request, 'core/contacts.html', {'contacts':contacts})

def student_life(request):
    student = Student_action.objects.all()
    return render(request, 'core/action.html', {'student':student})

def study(request):
    article = Article.objects.get(slug="study")
    print ('test')
    study_info = Study_info.objects.all()[0]
    return render(request, 'core/study_main.html', {'article':article, "study_info":study_info})

def library(request, slug):
    student = Libery.objects.get(slug=slug)
    print (student)
    return render(request, 'core/library.html', {'student':student})

def olimp(request, id):
    olimp = Olimp.objects.get(id=id)
    return render(request, 'core/programming-contests.html', {'olimp':olimp})

def olimp_other(request):
    olimp_all = Olimp.objects.all()[4:]
    return render(request, 'core/other.html', {'olimp_all':olimp_all})
