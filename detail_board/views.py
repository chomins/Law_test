from django.shortcuts import render,redirect,get_object_or_404
from .models import *
import requests, pprint
from bs4 import BeautifulSoup as BS
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator

# Create your views here.

def family_board(request):
   
    if  len(Family_Board.objects.all())== 0: 
        
        
        url='http://easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?onhunqnaAstSeq=25&pagingType=default&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(14):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            title_list=html.select('div.vote_list > ul.question > li.title ')
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]

           
            
            for q in question_list:
                question= q.text
                
                F_board=Family_Board()
                F_board.question=question
                F_board.save()
                id_list.append(F_board.id)
           
                
            for i in range(len(answer_list)):
                answer= answer_list[i].a.get('href')
                answer='http://easylaw.go.kr/CSP/'+answer
                tmp1=requests.get(answer)
                html = BS(tmp1.text, 'html.parser')
                real=html.select('ul.question > li.qa > div.q > div.ans')
                interest_area=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 >table.normal.st5 > tbody > tr > td.bdn > p > a   ')
                interest_rule=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 > table.normal.st5 > tbody > tr > td > p')
                h=''
                for r in real:
                    h=r.text
                
                
                F_board=Family_Board.objects.get(id=id_list[i])
                F_board.title=title_list[i].span.text
                F_board.answer=h
                F_board.save()
                for r in interest_area:
                    F_board=Family_Board.objects.get(id=id_list[i])
                    F_board.relevant_area=r.text
                    F_board.save()
                for r in interest_rule:
                    F_board=Family_Board.objects.get(id=id_list[i])
                    F_board.relevant_rule=r.text
                    F_board.catagory='가정법률'
                    F_board.save()
              
                    
    F_boards=Family_Board.objects.all()
    paginator = Paginator(F_boards,10)
    page = request.GET.get('page')
    lb= paginator.get_page(page)
    cat_name='가정법률'
   
        
    return render(request,'detailBoard_list.html',{'F_boards':lb, 'cat_name':cat_name})

def traffic_board(request):
   
    if  len(Traffic_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=90&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(9):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            title_list=html.select('div.vote_list > ul.question > li.title ')
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Traffic_Board()
                F_board.question=question
                F_board.save()
                id_list.append(F_board.id)
            
                
            for i in range(len(answer_list)):
                answer= answer_list[i].a.get('href')
                answer='http://easylaw.go.kr/CSP/'+answer
                tmp1=requests.get(answer)
                html = BS(tmp1.text, 'html.parser')
                real=html.select('ul.question > li.qa > div.q > div.ans')
                interest_area=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 >table.normal.st5 > tbody > tr > td.bdn > p > a   ')
                interest_rule=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 > table.normal.st5 > tbody > tr > td > p')
                h=''
                for r in real:
                    h=r.text
                
                
                F_board=Traffic_Board.objects.get(id=id_list[i])
                F_board.title=title_list[i].span.text
                F_board.answer=h
                
                F_board.save()
                for r in interest_area:
                    F_board=Traffic_Board.objects.get(id=id_list[i])
                    F_board.relevant_area=r.text
                    F_board.save()
                for r in interest_rule:
                    F_board=Traffic_Board.objects.get(id=id_list[i])
                    F_board.relevant_rule=r.text
                    F_board.catagory='교통\운전'
                    F_board.save()
    F_boards=Traffic_Board.objects.all()
    paginator = Paginator(F_boards,10)
    page = request.GET.get('page')
    lb= paginator.get_page(page)
    cat_name='교통\운전'
   
   
        
    return render(request,'detailBoard_list.html',{'F_boards':lb, 'cat_name':cat_name})

def government_board(request):
   
    if  len(Government_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=95&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(4):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            title_list=html.select('div.vote_list > ul.question > li.title ')
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Government_Board()
                F_board.question=question
                F_board.save()
                id_list.append(F_board.id)
            
                
            for i in range(len(answer_list)):
                answer= answer_list[i].a.get('href')
                answer='http://easylaw.go.kr/CSP/'+answer
                tmp1=requests.get(answer)
                html = BS(tmp1.text, 'html.parser')
                real=html.select('ul.question > li.qa > div.q > div.ans')
                interest_area=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 >table.normal.st5 > tbody > tr > td.bdn > p > a   ')
                interest_rule=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 > table.normal.st5 > tbody > tr > td > p')
                h=''
                for r in real:
                    h=r.text
                
                
                F_board=Government_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.title=title_list[i].span.text
                F_board.save()
                for r in interest_area:
                    F_board=Government_Board.objects.get(id=id_list[i])
                    F_board.relevant_area=r.text
                    F_board.save()
                for r in interest_rule:
                    F_board=Government_Board.objects.get(id=id_list[i])
                    F_board.relevant_rule=r.text
                    F_board.catagory='국가 및 지자체'
                    F_board.save()
    F_boards=Government_Board.objects.all()
    paginator = Paginator(F_boards,10)
    page = request.GET.get('page')
    lb= paginator.get_page(page)
    cat_name='국가 및 지자체'
    
   
        
    return render(request,'detailBoard_list.html',{'F_boards':lb, 'cat_name':cat_name})

def army_board(request):
   
    if  len(Army_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=81&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(6):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            title_list=html.select('div.vote_list > ul.question > li.title ')
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Army_Board()
                F_board.question=question
                F_board.save()
                id_list.append(F_board.id)
            
                
            for i in range(len(answer_list)):
                answer= answer_list[i].a.get('href')
                answer='http://easylaw.go.kr/CSP/'+answer
                tmp1=requests.get(answer)
                html = BS(tmp1.text, 'html.parser')
                real=html.select('ul.question > li.qa > div.q > div.ans')
                interest_area=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 >table.normal.st5 > tbody > tr > td.bdn > p > a   ')
                interest_rule=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 > table.normal.st5 > tbody > tr > td > p')
                h=''
                for r in real:
                    h=r.text
                
                
                F_board=Army_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.title=title_list[i].span.text
                F_board.save()
                for r in interest_area:
                    F_board=Army_Board.objects.get(id=id_list[i])
                    F_board.relevant_area=r.text
                    F_board.save()
                for r in interest_rule:
                    F_board=Army_Board.objects.get(id=id_list[i])
                    F_board.relevant_rule=r.text
                    F_board.catagory='국방\보훈'
                    F_board.save()
    F_boards=Army_Board.objects.all()
    paginator = Paginator(F_boards,10)
    page = request.GET.get('page')
    lb= paginator.get_page(page)
    cat_name='국방\보훈'
   
   
        
    return render(request,'detailBoard_list.html',{'F_boards':lb, 'cat_name':cat_name})

def labor_board(request):
   
    if  len(Labor_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=82&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(17):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            title_list=html.select('div.vote_list > ul.question > li.title ')
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Labor_Board()
                F_board.question=question
                F_board.save()
                id_list.append(F_board.id)
            
                
            for i in range(len(answer_list)):
                answer= answer_list[i].a.get('href')
                answer='http://easylaw.go.kr/CSP/'+answer
                tmp1=requests.get(answer)
                html = BS(tmp1.text, 'html.parser')
                real=html.select('ul.question > li.qa > div.q > div.ans')
                interest_area=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 >table.normal.st5 > tbody > tr > td.bdn > p > a   ')
                interest_rule=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 > table.normal.st5 > tbody > tr > td > p')
                h=''
                for r in real:
                    h=r.text
                
                
                F_board=Labor_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.title=title_list[i].span.text
                F_board.save()
                for r in interest_area:
                    F_board=Labor_Board.objects.get(id=id_list[i])
                    F_board.relevant_area=r.text
                    F_board.save()
                for r in interest_rule:
                    F_board=Labor_Board.objects.get(id=id_list[i])
                    F_board.relevant_rule=r.text
                    F_board.catagory='근로\노동'
                    F_board.save()
    F_boards=Labor_Board.objects.all()
    paginator = Paginator(F_boards,10)
    page = request.GET.get('page')
    lb= paginator.get_page(page)
    cat_name='근로\노동'
   
   
        
    return render(request,'detailBoard_list.html',{'F_boards':lb, 'cat_name':cat_name})

def financial_board(request):
   
    if  len(Financial_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=92&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(11):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            title_list=html.select('div.vote_list > ul.question > li.title ')
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Financial_Board()
                F_board.question=question
                F_board.save()
                id_list.append(F_board.id)
            
                
            for i in range(len(answer_list)):
                answer= answer_list[i].a.get('href')
                answer='http://easylaw.go.kr/CSP/'+answer
                tmp1=requests.get(answer)
                html = BS(tmp1.text, 'html.parser')
                real=html.select('ul.question > li.qa > div.q > div.ans')
                interest_area=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 >table.normal.st5 > tbody > tr > td.bdn > p > a   ')
                interest_rule=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 > table.normal.st5 > tbody > tr > td > p')
                h=''
                for r in real:
                    h=r.text
                
                
                F_board=Financial_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.title=title_list[i].span.text
                F_board.save()
                for r in interest_area:
                    F_board=Financial_Board.objects.get(id=id_list[i])
                    F_board.relevant_area=r.text
                    F_board.save()
                for r in interest_rule:
                    F_board=Financial_Board.objects.get(id=id_list[i])
                    F_board.relevant_rule=r.text
                    F_board.catagory='금융\금전'
                    F_board.save()
    F_boards=Financial_Board.objects.all()
    paginator = Paginator(F_boards,10)
    page = request.GET.get('page')
    lb= paginator.get_page(page)
    cat_name='금융\금전'

   
        
    return render(request,'detailBoard_list.html',{'F_boards':lb, 'cat_name':cat_name})

def trade_board(request):
   
    if  len(Trade_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=100&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(10):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            title_list=html.select('div.vote_list > ul.question > li.title ')
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Trade_Board()
                F_board.question=question
                F_board.save()
                id_list.append(F_board.id)
            
                
            for i in range(len(answer_list)):
                answer= answer_list[i].a.get('href')
                answer='http://easylaw.go.kr/CSP/'+answer
                tmp1=requests.get(answer)
                html = BS(tmp1.text, 'html.parser')
                real=html.select('ul.question > li.qa > div.q > div.ans')
                interest_area=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 >table.normal.st5 > tbody > tr > td.bdn > p > a   ')
                interest_rule=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 > table.normal.st5 > tbody > tr > td > p')
                h=''
                for r in real:
                    h=r.text
                
                
                F_board=Trade_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.title=title_list[i].span.text
                F_board.save()
                for r in interest_area:
                    F_board=Trade_Board.objects.get(id=id_list[i])
                    F_board.relevant_area=r.text
                    F_board.save()
                for r in interest_rule:
                    F_board=Trade_Board.objects.get(id=id_list[i])
                    F_board.relevant_rule=r.text
                    F_board.catagory='무역\출입국'
                    F_board.save()
    F_boards=Trade_Board.objects.all()
    paginator = Paginator(F_boards,10)
    page = request.GET.get('page')
    lb= paginator.get_page(page)
    cat_name='무역\출입국'

   
        
    return render(request,'detailBoard_list.html',{'F_boards':lb, 'cat_name':cat_name})

def leisure_board(request):
   
    if  len(Leisure_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=87&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(6):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            title_list=html.select('div.vote_list > ul.question > li.title ')
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Leisure_Board()
                F_board.question=question
                F_board.save()
                id_list.append(F_board.id)
            
                
            for i in range(len(answer_list)):
                answer= answer_list[i].a.get('href')
                answer='http://easylaw.go.kr/CSP/'+answer
                tmp1=requests.get(answer)
                html = BS(tmp1.text, 'html.parser')
                real=html.select('ul.question > li.qa > div.q > div.ans')
                interest_area=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 >table.normal.st5 > tbody > tr > td.bdn > p > a   ')
                interest_rule=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 > table.normal.st5 > tbody > tr > td > p')
                h=''
                for r in real:
                    h=r.text
                
                
                F_board=Leisure_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.title=title_list[i].span.text
                F_board.save()
                for r in interest_area:
                    F_board=Leisure_Board.objects.get(id=id_list[i])
                    F_board.relevant_area=r.text
                    F_board.save()
                for r in interest_rule:
                    F_board=Leisure_Board.objects.get(id=id_list[i])
                    F_board.relevant_rule=r.text
                    F_board.catagory='문화\여가생활'
                    F_board.save()
    F_boards=Leisure_Board.objects.all()
    paginator = Paginator(F_boards,10)
    page = request.GET.get('page')
    lb= paginator.get_page(page)
    cat_name='문화\여가생활'

   
        
    return render(request,'detailBoard_list.html',{'F_boards':lb, 'cat_name':cat_name})


def lawsuit_board(request):
   
    if  len(Lawsuit_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=85&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(13):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            title_list=html.select('div.vote_list > ul.question > li.title ')
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Lawsuit_Board()
                F_board.question=question
                F_board.save()
                id_list.append(F_board.id)
            
                
            for i in range(len(answer_list)):
                answer= answer_list[i].a.get('href')
                answer='http://easylaw.go.kr/CSP/'+answer
                tmp1=requests.get(answer)
                html = BS(tmp1.text, 'html.parser')
                real=html.select('ul.question > li.qa > div.q > div.ans')
                interest_area=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 >table.normal.st5 > tbody > tr > td.bdn > p > a   ')
                interest_rule=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 > table.normal.st5 > tbody > tr > td > p')
                h=''
                for r in real:
                    h=r.text
                
                
                F_board=Lawsuit_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.title=title_list[i].span.text
                F_board.save()
                for r in interest_area:
                    F_board=Lawsuit_Board.objects.get(id=id_list[i])
                    F_board.relevant_area=r.text
                    F_board.save()
                for r in interest_rule:
                    F_board=Lawsuit_Board.objects.get(id=id_list[i])
                    F_board.relevant_rule=r.text
                    F_board.catagory='민형사\소송'
                    F_board.save()
    F_boards=Lawsuit_Board.objects.all()
    paginator = Paginator(F_boards,10)
    page = request.GET.get('page')
    lb= paginator.get_page(page)
    cat_name='민형사\소송'

   
        
    return render(request,'detailBoard_list.html',{'F_boards':lb, 'cat_name':cat_name})

def welfare_board(request):
   
    if  len(Welfare_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=97&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(18):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            title_list=html.select('div.vote_list > ul.question > li.title ')
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Welfare_Board()
                F_board.question=question
                F_board.save()
                id_list.append(F_board.id)
            
                
            for i in range(len(answer_list)):
                answer= answer_list[i].a.get('href')
                answer='http://easylaw.go.kr/CSP/'+answer
                tmp1=requests.get(answer)
                html = BS(tmp1.text, 'html.parser')
                real=html.select('ul.question > li.qa > div.q > div.ans')
                interest_area=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 >table.normal.st5 > tbody > tr > td.bdn > p > a   ')
                interest_rule=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 > table.normal.st5 > tbody > tr > td > p')
                h=''
                for r in real:
                    h=r.text
                
                
                F_board=Welfare_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.title=title_list[i].span.text
                F_board.save()
                for r in interest_area:
                    F_board=Welfare_Board.objects.get(id=id_list[i])
                    F_board.relevant_area=r.text
                    F_board.save()
                for r in interest_rule:
                    F_board=Welfare_Board.objects.get(id=id_list[i])
                    F_board.relevant_rule=r.text
                    F_board.catagory='복지'
                    F_board.save()
    F_boards=Welfare_Board.objects.all()
    paginator = Paginator(F_boards,10)
    page = request.GET.get('page')
    lb= paginator.get_page(page)
    cat_name='복지'

   
        
    return render(request,'detailBoard_list.html',{'F_boards':lb, 'cat_name':cat_name})

def estate_board(request):
   
    if  len(Estate_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=84&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(21):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            title_list=html.select('div.vote_list > ul.question > li.title ')
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Estate_Board()
                F_board.question=question
                F_board.save()
                id_list.append(F_board.id)
            
                
            for i in range(len(answer_list)):
                answer= answer_list[i].a.get('href')
                answer='http://easylaw.go.kr/CSP/'+answer
                tmp1=requests.get(answer) 
                html = BS(tmp1.text, 'html.parser')
                real=html.select('ul.question > li.qa > div.q > div.ans')
                interest_area=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 >table.normal.st5 > tbody > tr > td.bdn > p > a   ')
                interest_rule=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 > table.normal.st5 > tbody > tr > td > p')
                h=''
                for r in real:
                    h=r.text
                
                
                F_board=Estate_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.title=title_list[i].span.text
                F_board.save()
                for r in interest_area:
                    F_board=Estate_Board.objects.get(id=id_list[i])
                    F_board.relevant_area=r.text
                    F_board.save()
                for r in interest_rule:
                    F_board=Estate_Board.objects.get(id=id_list[i])
                    F_board.relevant_rule=r.text
                    F_board.catagory='부동산\임대차'
                    F_board.save()
    F_boards=Estate_Board.objects.all()
    paginator = Paginator(F_boards,10)
    page = request.GET.get('page')
    lb= paginator.get_page(page)
    cat_name='부동산\임대차'

        
    return render(request,'detailBoard_list.html',{'F_boards':lb, 'cat_name':cat_name})

def business_board(request):
   
    if  len(Business_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=83&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(9):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            title_list=html.select('div.vote_list > ul.question > li.title ')
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Business_Board()
                F_board.question=question
                F_board.save()
                id_list.append(F_board.id)
            
                
            for i in range(len(answer_list)):
                answer= answer_list[i].a.get('href')
                answer='http://easylaw.go.kr/CSP/'+answer
                tmp1=requests.get(answer)
                html = BS(tmp1.text, 'html.parser')
                real=html.select('ul.question > li.qa > div.q > div.ans')
                interest_area=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 >table.normal.st5 > tbody > tr > td.bdn > p > a   ')
                interest_rule=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 > table.normal.st5 > tbody > tr > td > p')
                h=''
                for r in real:
                    h=r.text
                
                
                F_board=Business_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.title=title_list[i].span.text
                F_board.save()
                for r in interest_area:
                    F_board=Business_Board.objects.get(id=id_list[i])
                    F_board.relevant_area=r.text
                    F_board.save()
                for r in interest_rule:
                    F_board=Business_Board.objects.get(id=id_list[i])
                    F_board.relevant_rule=r.text
                    F_board.catagory='사업'
                    F_board.save()
    F_boards=Business_Board.objects.all()
    paginator = Paginator(F_boards,10)
    page = request.GET.get('page')
    lb= paginator.get_page(page)
    cat_name='사업'
 
        
    return render(request,'detailBoard_list.html',{'F_boards':lb, 'cat_name':cat_name})

def crime_board(request):
   
    if  len(Crime_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=86&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(14):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            title_list=html.select('div.vote_list > ul.question > li.title ')
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Crime_Board()
                F_board.question=question
                F_board.save()
                id_list.append(F_board.id)
            
                
            for i in range(len(answer_list)):
                answer= answer_list[i].a.get('href')
                answer='http://easylaw.go.kr/CSP/'+answer
                tmp1=requests.get(answer)
                html = BS(tmp1.text, 'html.parser')
                real=html.select('ul.question > li.qa > div.q > div.ans')
                interest_area=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 >table.normal.st5 > tbody > tr > td.bdn > p > a   ')
                interest_rule=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 > table.normal.st5 > tbody > tr > td > p')
                h=''
                for r in real:
                    h=r.text
                
                
                F_board=Crime_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.title=title_list[i].span.text
                F_board.save()
                for r in interest_area:
                    F_board=Crime_Board.objects.get(id=id_list[i])
                    F_board.relevant_area=r.text
                    F_board.save()
                for r in interest_rule:
                    F_board=Crime_Board.objects.get(id=id_list[i])
                    F_board.relevant_rule=r.text
                    F_board.catagory='사회안전\범죄'
                    F_board.save()
    F_boards=Crime_Board.objects.all()
    paginator = Paginator(F_boards,10)
    page = request.GET.get('page')
    lb= paginator.get_page(page)
    cat_name='사회안전\범죄'

        
    return render(request,'detailBoard_list.html',{'F_boards':lb, 'cat_name':cat_name})

def client_board(request):
   
    if  len(Client_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=88&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(8):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            title_list=html.select('div.vote_list > ul.question > li.title ')
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Client_Board()
                F_board.question=question
                F_board.save()
                id_list.append(F_board.id)
            
                
            for i in range(len(answer_list)):
                answer= answer_list[i].a.get('href')
                answer='http://easylaw.go.kr/CSP/'+answer
                tmp1=requests.get(answer)
                html = BS(tmp1.text, 'html.parser')
                real=html.select('ul.question > li.qa > div.q > div.ans')
                interest_area=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 >table.normal.st5 > tbody > tr > td.bdn > p > a   ')
                interest_rule=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 > table.normal.st5 > tbody > tr > td > p')
                h=''
                for r in real:
                    h=r.text
                
                
                F_board=Client_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.title=title_list[i].span.text
                F_board.save()
                for r in interest_area:
                    F_board=Client_Board.objects.get(id=id_list[i])
                    F_board.relevant_area=r.text
                    F_board.save()
                for r in interest_rule:
                    F_board=Client_Board.objects.get(id=id_list[i])
                    F_board.relevant_rule=r.text
                    F_board.catagory='소비자'
                    F_board.save()
    F_boards=Client_Board.objects.all()
    paginator = Paginator(F_boards,10)
    page = request.GET.get('page')
    lb= paginator.get_page(page)
    cat_name='소비자'

        
    return render(request,'detailBoard_list.html',{'F_boards':lb, 'cat_name':cat_name})

def children_board(request):
   
    if  len(Children_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=89&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(18):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            title_list=html.select('div.vote_list > ul.question > li.title ')
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Children_Board()
                F_board.question=question
                F_board.save()
                id_list.append(F_board.id)
            
                
            for i in range(len(answer_list)):
                answer= answer_list[i].a.get('href')
                answer='http://easylaw.go.kr/CSP/'+answer
                tmp1=requests.get(answer)
                html = BS(tmp1.text, 'html.parser')
                real=html.select('ul.question > li.qa > div.q > div.ans')
                interest_area=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 >table.normal.st5 > tbody > tr > td.bdn > p > a   ')
                interest_rule=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 > table.normal.st5 > tbody > tr > td > p')
                h=''
                for r in real:
                    h=r.text
                
                
                F_board=Children_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.title=title_list[i].span.text
                F_board.save()
                for r in interest_area:
                    F_board=Children_Board.objects.get(id=id_list[i])
                    F_board.relevant_area=r.text
                    F_board.save()
                for r in interest_rule:
                    F_board=Children_Board.objects.get(id=id_list[i])
                    F_board.relevant_rule=r.text
                    F_board.catagory='아동 청소년\교육'
                    F_board.save()
    F_boards=Children_Board.objects.all()
    paginator = Paginator(F_boards,10)
    page = request.GET.get('page')
    lb= paginator.get_page(page)
    cat_name='아동 청소년\교육'

   
        
    return render(request,'detailBoard_list.html',{'F_boards':lb, 'cat_name':cat_name})

def information_board(request):
   
    if  len(Information_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=94&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(5):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            title_list=html.select('div.vote_list > ul.question > li.title ')
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Information_Board()
                F_board.question=question
                F_board.save()
                id_list.append(F_board.id)
            
                
            for i in range(len(answer_list)):
                answer= answer_list[i].a.get('href')
                answer='http://easylaw.go.kr/CSP/'+answer
                tmp1=requests.get(answer)
                html = BS(tmp1.text, 'html.parser')
                real=html.select('ul.question > li.qa > div.q > div.ans')
                interest_area=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 >table.normal.st5 > tbody > tr > td.bdn > p > a   ')
                interest_rule=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 > table.normal.st5 > tbody > tr > td > p')
                h=''
                for r in real:
                    h=r.text
                
                
                F_board=Information_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.title=title_list[i].span.text
                F_board.save()
                for r in interest_area:
                    F_board=Information_Board.objects.get(id=id_list[i])
                    F_board.relevant_area=r.text
                    F_board.save()
                for r in interest_rule:
                    F_board=Information_Board.objects.get(id=id_list[i])
                    F_board.relevant_rule=r.text
                    F_board.catagory='정보통신\기술'
                    F_board.save()
    F_boards=Information_Board.objects.all()
    paginator = Paginator(F_boards,10)
    page = request.GET.get('page')
    lb= paginator.get_page(page)
    cat_name='정보통신\기술'

        
    return render(request,'detailBoard_list.html',{'F_boards':lb, 'cat_name':cat_name})

def startup_board(request):
   
    if  len(Startup_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=91&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(19):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            title_list=html.select('div.vote_list > ul.question > li.title ')
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Startup_Board()
                F_board.question=question
                F_board.save()
                id_list.append(F_board.id)
            
                
            for i in range(len(answer_list)):
                answer= answer_list[i].a.get('href')
                answer='http://easylaw.go.kr/CSP/'+answer
                tmp1=requests.get(answer)
                html = BS(tmp1.text, 'html.parser')
                real=html.select('ul.question > li.qa > div.q > div.ans')
                interest_area=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 >table.normal.st5 > tbody > tr > td.bdn > p > a   ')
                interest_rule=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 > table.normal.st5 > tbody > tr > td > p')
                h=''
                for r in real:
                    h=r.text
                
                
                F_board=Startup_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.title=title_list[i].span.text
                F_board.save()
                for r in interest_area:
                    F_board=Startup_Board.objects.get(id=id_list[i])
                    F_board.relevant_area=r.text
                    F_board.save()
                for r in interest_rule:
                    F_board=Startup_Board.objects.get(id=id_list[i])
                    F_board.relevant_rule=r.text
                    F_board.catagory='창업'
                    F_board.save()
    F_boards=Startup_Board.objects.all()
    paginator = Paginator(F_boards,10)
    page = request.GET.get('page')
    lb= paginator.get_page(page)
    cat_name='창업'

        
    return render(request,'detailBoard_list.html',{'F_boards':lb, 'cat_name':cat_name})


def eco_board(request):
   
    if  len(Eco_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=96&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(6):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            title_list=html.select('div.vote_list > ul.question > li.title ')
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Eco_Board()
                F_board.question=question
                F_board.save()
                id_list.append(F_board.id)
            
                
            for i in range(len(answer_list)):
                answer= answer_list[i].a.get('href')
                answer='http://easylaw.go.kr/CSP/'+answer
                tmp1=requests.get(answer)
                html = BS(tmp1.text, 'html.parser')
                real=html.select('ul.question > li.qa > div.q > div.ans')
                interest_area=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 >table.normal.st5 > tbody > tr > td.bdn > p > a   ')
                interest_rule=html.select('html > body > div#maincontent > div#body.Wrap > div#contents.w760 > table.normal.st5 > tbody > tr > td > p')
                h=''
                for r in real:
                    h=r.text
                
                
                F_board=Eco_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.title=title_list[i].span.text
                F_board.save()
                for r in interest_area:
                    F_board=Eco_Board.objects.get(id=id_list[i])
                    F_board.relevant_area=r.text
                    F_board.save()
                for r in interest_rule:
                    F_board=Eco_Board.objects.get(id=id_list[i])
                    F_board.relevant_rule=r.text
                    F_board.catagory='환경\에너지'
                    F_board.save()
    F_boards=Eco_Board.objects.all()
    paginator = Paginator(F_boards,10)
    page = request.GET.get('page')
    lb= paginator.get_page(page)
    cat_name='환경\에너지'
   
        
    return render(request,'detailBoard_list.html',{'F_boards':lb, 'cat_name':cat_name})

def search(request):
    cat_name=request.POST['identity']
    title=request.POST['search_data']
    output=None
    error=''
    if cat_name == "가정법률":
        try:
            output=Family_Board.objects.get(title=title)

        except ObjectDoesNotExist:
            error="검색물이 존재하지 않습니다."
    elif cat_name == "교통\운전":
         try:
            output=Traffic_Board.objects.get(title=title)

         except ObjectDoesNotExist:
            error="검색물이 존재하지 않습니다."
    elif cat_name == "국가 및 지자체":
         try:
            output=Government_Board.objects.get(title=title)

         except ObjectDoesNotExist:
            error="검색물이 존재하지 않습니다."
 
    elif cat_name == "근로\노동":
         try:
            output=Labor_Board.objects.get(title=title)

         except ObjectDoesNotExist:
            error="검색물이 존재하지 않습니다."
    elif cat_name == "금융\금전":
         try:
            output=Financial_Board.objects.get(title=title)

         except ObjectDoesNotExist:
            error="검색물이 존재하지 않습니다."
    elif cat_name == "무역\출입국":
         try:
            output=Trade_Board.objects.get(title=title)

         except ObjectDoesNotExist:
            error="검색물이 존재하지 않습니다."
    elif cat_name == "문화\여가생활":
         try:
            output=Leisure.objects.get(title=title)

         except ObjectDoesNotExist:
            error="검색물이 존재하지 않습니다."
    elif cat_name == "민형사\소송":
         try:
            output=Lawsuit_Board.objects.get(title=title)

         except ObjectDoesNotExist:
            error="검색물이 존재하지 않습니다."
    elif cat_name == "복지":
         try:
            output=Welfare_Board.objects.get(title=title)

         except ObjectDoesNotExist:
            error="검색물이 존재하지 않습니다."
    elif cat_name == "부동산\임대차":
         try:
            output=Estate_Board.objects.get(title=title)

         except ObjectDoesNotExist:
            error="검색물이 존재하지 않습니다."
    elif cat_name == "사업":
         try:
            output=Business_Board.objects.get(title=title)

         except ObjectDoesNotExist:
            error="검색물이 존재하지 않습니다."
    elif cat_name == "사회안전\범죄":
         try:
            output=Crime_Board.objects.get(title=title)

         except ObjectDoesNotExist:
            error="검색물이 존재하지 않습니다."
    elif cat_name == "소비자":
         try:
            output=Client_Board.objects.get(title=title)

         except ObjectDoesNotExist:
            error="검색물이 존재하지 않습니다."
    elif cat_name == "아동 청소년\교육":
         try:
            output=Children_Board.objects.get(title=title)

         except ObjectDoesNotExist:
            error="검색물이 존재하지 않습니다."
    elif cat_name == "정보통신\기술":
         try:
            output=Information_Board.objects.get(title=title)

         except ObjectDoesNotExist:
            error="검색물이 존재하지 않습니다."
    elif cat_name == "창업":
         try:
            output=Startup_Board.objects.get(title=title)

         except ObjectDoesNotExist:
            error="검색물이 존재하지 않습니다."
    elif cat_name == "환경\에너지":
         try:
            output=Eco_Board.objects.get(title=title)

         except ObjectDoesNotExist:
            error="검색물이 존재하지 않습니다."
    elif cat_name == "국방\보훈":
        try:
            output=Army_Board.objects.get(title=title)

        except ObjectDoesNotExist:
            error="검색물이 존재하지 않습니다."
    return render(request,'detailBoard_list.html',{'output':output,'error':error,'cat_name': cat_name})

def board_detail(request,post_id,cat_name):
    board=None
    topic=cat_name
    
    if topic == "가정법률":
        board=Family_Board.objects.get(id=post_id)
    elif topic =="교통\운전":
        board=Traffic_Board.objects.get(id=post_id)
    elif topic == "국가 및 지자체":
        board=Government_Board.objects.get(id=post_id)
    elif topic == "근로\노동":
        board=Labor_Board.objects.get(id=post_id)
    elif topic == "금융\금전":
        board=Financial_Board.objects.get(id=post_id)
    elif topic == "무역\출입국":
        board=Trade_Board.objects.get(id=post_id)
    elif topic == "문화\여가생활":
        board=Leisure_Board.objects.get(id=post_id)
    elif topic == "민형사\소송":
        board=Lawsuit_Board.objects.get(id=post_id)
    elif topic == "복지":
        board=Welfare_Board.objects.get(id=post_id)
    elif topic == "부동산\임대차":
        board=Estate_Board.objects.get(id=post_id)
    elif topic == "사업":
        board=Business_Board.objects.get(id=post_id)
    elif topic == "사회안전\범죄":
        board=Crime_Board.objects.get(id=post_id)
    elif topic == "소비자":
        board=Consumer_Board.objects.get(id=post_id)
    elif topic == "아동 청소년\교육":
        board=Children_Board.objects.get(id=post_id)
    elif topic == "정보통신\기술":
        board=Information_Board.objects.get(id=post_id)
    elif topic == "창업":
        board=Startup_Board.objects.get(id=post_id)
    elif topic == "환경\에너지":
        board=Eco_Board.objects.get(id=post_id)
    elif topic == "국방\보훈":
        board=Army_Board.objects.get(id=post_id)
    cat_name=cat_name

    
    return render(request,'board_detail.html',{'board':board,'cat_name':cat_name})

def detail_scrap(request,post_id,cat_name):
    topic=cat_name

    post=None
    if topic == "가정법률":
        post=Family_Board.objects.get(id=post_id)
    elif topic =="교통\운전":
        post=Traffic_Board.objects.get(id=post_id)
    elif topic == "국가 및 지자체":
        post=Government_Board.objects.get(id=post_id)
    elif topic == "근로\노동":
        post=Labor_Board.objects.get(id=post_id)
    elif topic == "금융\금전":
        post=Financial_Board.objects.get(id=post_id)
    elif topic == "무역\출입국":
        post=Trade_Board.objects.get(id=post_id)
    elif topic == "문화\여가생활":
        post=Leisure_Board.objects.get(id=post_id)
    elif topic == "민형사\소송":
        post=Lawsuit_Board.objects.get(id=post_id)
    elif topic == "복지":
        post=Welfare_Board.objects.get(id=post_id)
    elif topic == "부동산\임대차":
        post=Estate_Board.objects.get(id=post_id)
    elif topic == "사업":
        post=Business_Board.objects.get(id=post_id)
    elif topic == "사회안전\범죄":
        post=Crime_Board.objects.get(id=post_id)
    elif topic == "소비자":
        post=Consumer_Board.objects.get(id=post_id)
    elif topic == "아동 청소년\교육":
        post=Children_Board.objects.get(id=post_id)
    elif topic == "정보통신\기술":
        post=Information_Board.objects.get(id=post_id)
    elif topic == "창업":
        post=Startup_Board.objects.get(id=post_id)
    elif topic == "환경\에너지":
        post=Eco_Board.objects.get(id=post_id)
    elif topic == "국방\보훈":
        post=Army_Board.objects.get(id=post_id)
    
    if post.scrap.filter(username=request.user.username).exists():
                post.scrap.remove(request.user)    
    else:
                post.scrap.add(request.user)
       
    post.save()
    return redirect('board_detail', post_id, cat_name )