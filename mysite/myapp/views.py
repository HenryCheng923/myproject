from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Company    #從myapp資料夾抓取models.py檔案，並載入Company這個物件
from django.shortcuts import render_to_response
from django.shortcuts import redirect

def pylinkweb(request):
	return HttpResponse("Django讓python能方便連結網頁")
def deposits(request):
	return render(request,'E_10_1.html',{})
def result(request):
	pv=int(request.GET['amount'])
	i=float(request.GET['rate'])
	n=int(request.GET['period'])
	fv=str((pv*((1+i)**n)))
	return HttpResponse(fv)

def company(request): #資料庫讀取資料
    company = Company.objects.all() #取出所有在Company的資料表內容
    stockid = Company._meta.get_field('stockid').column #將Company資料表的stockid給stockid
    abbreviation = Company._meta.get_field('abbreviation').column
    url = Company._meta.get_field('url').column
    industryname = Company._meta.get_field('industryname').column
    return render_to_response('company.html',locals()) #回傳兩個參數，一個是網頁位置，一個是填入網頁字典，company.html可以使用company內的變數值

def insert(request):
	return render(request, 'insert.html')

def do_insert(request): #將頁面資料寫入資料庫
	stockid = request.POST['stockid']
	abbreviation = request.POST['abbreviation']
	url = request.POST['url']
	employees = request.POST['employees']
	capital = request.POST['capital']
	industryname = request.POST['industryname']
	listeddate = request.POST['listeddate']
	Company.objects.create(stockid=stockid, abbreviation=abbreviation, url=url, employees=employees, capital=capital, industryname=industryname, listeddate=listeddate)
	return render(request, 'go_company.html') #直接使用 redirect('/company/') 不用再透過轉址也可以，目前不知道差異。

def detail(request, stockid):
	detail = Company.objects.get(stockid=stockid)
	return render(request,'detail.html', {'detail': detail})
	
def update(request, stockid):
	update = Company.objects.get(stockid=stockid)
	return render(request,'update.html', {'update': update})

def do_update(request):
	stockid = request.POST['stockid']
	abbreviation = request.POST['abbreviation']
	url = request.POST['url']
	employees = request.POST['employees']
	capital = request.POST['capital']
	industryname = request.POST['industryname']
	listeddate = request.POST['listeddate']
	do_update = Company.objects.filter(stockid=stockid)
	do_update.update(abbreviation=abbreviation)
	do_update.update(url=url)
	do_update.update(employees=employees)
	do_update.update(capital=capital)
	do_update.update(industryname=industryname)
	do_update.update(listeddate=listeddate)
	return redirect('/company/')

def delete(request, stockid):
	delete = Company.objects.get(stockid=stockid)
	return render(request,'delete.html', {'delete': delete})


def do_delete(request):
	stockid = request.POST['stockid']	
	do_delete = Company.objects.filter(stockid=stockid)
	do_delete.delete()
	return redirect('/company/')

# Create your views here.
