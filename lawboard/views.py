from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.utils import timezone
from django.core.paginator import Paginator
from detail_board.models import *


def lawboardList(request):
    lawboards_list = LawBoard.objects.all()
    lawboards_list.reverse()
    paginator = Paginator(lawboards_list,7)
    page = request.GET.get('page')
    lb= paginator.get_page(page)
    return render(request, 'lawboard_list.html', {'lawboards': lb})

def lawboardFilter(request):
    lawboards_list = LawBoard.objects.all()
    search_mode = request.POST.get('search_mode')
    search_data = request.POST.get('search_data')
    filter_result = []
    if search_mode == 'title' :
        for lb in lawboards_list:
            if search_data in lb.title :
                filter_result.append(lb)
    elif search_mode == 'body':
        for lb in lawboards_list:
            if search_data in lb.body :
                filter_result.append(lb)
    
    lawboards = filter_result
    #페이지네이터
    paginator = Paginator(lawboards,15)
    page = request.GET.get('page')
    paginator2 = paginator.get_page(page)

    return render(request, 'lawboard_list.html', {'lawboards':paginator2})


def lawboardNew(request):
    scrapped_family=request.user.family_scrap.all()
    scrapped_traffic=request.user.traffic_scrap.all()
    scrapped_government=request.user.government_scrap.all()
    scrapped_army=request.user.army_scrap.all()
    scrapped_labor=request.user.labor_scrap.all()
    scrapped_financial=request.user.financial_scrap.all()
    scrapped_trade=request.user.trade_scrap.all()
    scrapped_leisure=request.user.leisure_scrap.all()
    scrapped_lawsuit=request.user.lawsuit_scrap.all()
    scrapped_welfare=request.user.welfare_scrap.all()
    scrapped_estate=request.user.estate_scrap.all()
    scrapped_business=request.user.business_scrap.all()
    scrapped_crime=request.user.crime_scrap.all()
    scrapped_client=request.user.client_scrap.all()
    scrapped_children = request.user.children_scrap.all()
    scrapped_information=request.user.information_scrap.all()
    scrapped_startup=request.user.startup_scrap.all()
    scrapped_eco=request.user.eco_scrap.all()


    scrapped_family.union(scrapped_traffic)
    scrapped_family.union(scrapped_government)
    scrapped_family.union(scrapped_army)
    scrapped_family.union(scrapped_labor)
    scrapped_family.union(scrapped_financial)
    scrapped_family.union(scrapped_trade)
    scrapped_family.union(scrapped_leisure)
    scrapped_family.union(scrapped_lawsuit)
    scrapped_family.union(scrapped_welfare)
    scrapped_family.union(scrapped_estate)
    scrapped_family.union(scrapped_business)
    scrapped_family.union(scrapped_crime)
    scrapped_family.union(scrapped_client)
    scrapped_family.union(scrapped_information)
    scrapped_family.union(scrapped_startup)
    scrapped_family.union(scrapped_eco)
    scrapped_family.union(scrapped_children)
    tmp = scrapped_family
    print(tmp)

    return render(request, 'lawboard_new.html', {'tmp':tmp})

def lawboardCreate(request):
    scrapped_family=request.user.family_scrap.all()
    scrapped_traffic=request.user.traffic_scrap.all()
    scrapped_government=request.user.government_scrap.all()
    scrapped_army=request.user.army_scrap.all()
    scrapped_labor=request.user.labor_scrap.all()
    scrapped_financial=request.user.financial_scrap.all()
    scrapped_trade=request.user.trade_scrap.all()
    scrapped_leisure=request.user.leisure_scrap.all()
    scrapped_lawsuit=request.user.lawsuit_scrap.all()
    scrapped_welfare=request.user.welfare_scrap.all()
    scrapped_estate=request.user.estate_scrap.all()
    scrapped_business=request.user.business_scrap.all()
    scrapped_crime=request.user.crime_scrap.all()
    scrapped_client=request.user.client_scrap.all()
    scrapped_children = request.user.children_scrap.all()
    scrapped_information=request.user.information_scrap.all()
    scrapped_startup=request.user.startup_scrap.all()
    scrapped_eco=request.user.eco_scrap.all()


    scrapped_family.union(scrapped_traffic)
    scrapped_family.union(scrapped_government)
    scrapped_family.union(scrapped_army)
    scrapped_family.union(scrapped_labor)
    scrapped_family.union(scrapped_financial)
    scrapped_family.union(scrapped_trade)
    scrapped_family.union(scrapped_leisure)
    scrapped_family.union(scrapped_lawsuit)
    scrapped_family.union(scrapped_welfare)
    scrapped_family.union(scrapped_estate)
    scrapped_family.union(scrapped_business)
    scrapped_family.union(scrapped_crime)
    scrapped_family.union(scrapped_client)
    scrapped_family.union(scrapped_information)
    scrapped_family.union(scrapped_startup)
    scrapped_family.union(scrapped_eco)
    scrapped_family.union(scrapped_children)
    tmp = scrapped_family
 


   
    
    btitle = request.POST['bring']
    tmp1=None
    for i in tmp:
       
        if i.title == btitle :
           tmp1=i
           
    new_lb = LawBoard()
    new_lb.title = request.POST['title']
    new_lb.pub_date = timezone.datetime.now()
    new_lb.writer = request.user
    new_lb.catagory=tmp1.catagory
    new_lb.scrap_id=tmp1.id
    new_lb.body = request.POST['body']
    new_lb.save()
    return redirect('lb_list')

def lawboardEdit(request, lb_id):
    scrapped_family=request.user.family_scrap.all()
    scrapped_traffic=request.user.traffic_scrap.all()
    scrapped_government=request.user.government_scrap.all()
    scrapped_army=request.user.army_scrap.all()
    scrapped_labor=request.user.labor_scrap.all()
    scrapped_financial=request.user.financial_scrap.all()
    scrapped_trade=request.user.trade_scrap.all()
    scrapped_leisure=request.user.leisure_scrap.all()
    scrapped_lawsuit=request.user.lawsuit_scrap.all()
    scrapped_welfare=request.user.welfare_scrap.all()
    scrapped_estate=request.user.estate_scrap.all()
    scrapped_business=request.user.business_scrap.all()
    scrapped_crime=request.user.crime_scrap.all()
    scrapped_client=request.user.client_scrap.all()
    scrapped_children = request.user.children_scrap.all()
    scrapped_information=request.user.information_scrap.all()
    scrapped_startup=request.user.startup_scrap.all()
    scrapped_eco=request.user.eco_scrap.all()


    scrapped_family.union(scrapped_traffic)
    scrapped_family.union(scrapped_government)
    scrapped_family.union(scrapped_army)
    scrapped_family.union(scrapped_labor)
    scrapped_family.union(scrapped_financial)
    scrapped_family.union(scrapped_trade)
    scrapped_family.union(scrapped_leisure)
    scrapped_family.union(scrapped_lawsuit)
    scrapped_family.union(scrapped_welfare)
    scrapped_family.union(scrapped_estate)
    scrapped_family.union(scrapped_business)
    scrapped_family.union(scrapped_crime)
    scrapped_family.union(scrapped_client)
    scrapped_family.union(scrapped_information)
    scrapped_family.union(scrapped_startup)
    scrapped_family.union(scrapped_eco)
    scrapped_family.union(scrapped_children)
    tmp = scrapped_family
    edit_lb = LawBoard.objects.get(id = lb_id)
    return render(request,'lawboard_edit.html',{'lb': edit_lb, 'tmp':tmp })

def lawboardUpdate(request, lb_id):
    update_lb = LawBoard.objects.get(id = lb_id)
    update_lb.title = request.POST['title']
    update_lb.pub_date = timezone.datetime.now()
    update_lb.scrap_law = request.POST['bring']
    update_lb.cat = request.POST['cat']
    update_lb.body = request.POST['body']
    update_lb.save()
    return redirect('lb_list')

def lawboardDetail(request, lb_id):
    detail_lb = get_object_or_404(LawBoard,id=lb_id)
    comment_lb = LB_comment.objects.filter(lbcomment= lb_id )
    scrap_count = detail_lb.total_scrap()
    board=None
    topic=detail_lb.catagory
    if topic == "가정법률":
        board=Family_Board.objects.get(id=lb_id)
    elif topic =="교통\운전":
        board=Traffic_Board.objects.get(id=lb_id)
    elif topic == "국가 및 지자체":
        board=Government_Board.objects.get(id=lb_id)
    elif topic == "근로\노동":
        board=Labor_Board.objects.get(id=lb_id)
    elif topic == "금융\금전":
        board=Financial_Board.objects.get(id=lb_id)
    elif topic == "무역\출입국":
        board=Trade_Board.objects.get(id=lb_id)
    elif topic == "문화\여가생활":
        board=Leisure_Board.objects.get(id=lb_id)
    elif topic == "민형사\소송":
        board=Lawsuit_Board.objects.get(id=lb_id)
    elif topic == "복지":
        board=Welfare_Board.objects.get(id=lb_id)
    elif topic == "부동산\임대차":
        board=Estate_Board.objects.get(id=lb_id)
    elif topic == "사업":
        board=Business_Board.objects.get(id=lb_id)
    elif topic == "사회안전\범죄":
        board=Crime_Board.objects.get(id=lb_id)
    elif topic == "소비자":
        board=Consumer_Board.objects.get(id=lb_id)
    elif topic == "아동 청소년\교육":
        board=Children_Board.objects.get(id=lb_id)
    elif topic == "정보통신\기술":
        board=Information_Board.objects.get(id=lb_id)
    elif topic == "창업":
        board=Startup_Board.objects.get(id=lb_id)
    elif topic == "환경\에너지":
        board=Eco_Board.objects.get(id=lb_id)
    elif topic == "국방\보훈":
        board=Army_Board.objects.get(id=lb_id)
    return render(request, 'lawboard_detail.html',{'ib':board,'lb':detail_lb, 'comments':comment_lb , 'scrap_count':scrap_count})

def lawboardDelete(request, lb_id):
    delete_lb = LawBoard.objects.get(id=lb_id)
    delete_lb.delete()
    return redirect('lb_list')


def meetingboardList(request):
    meetingboards= MeetingBoard.objects.all()
    meetingboards.reverse()
    paginator = Paginator(meetingboards,7)
    page = request.GET.get('page')
    paginator2 = paginator.get_page(page)
    return render(request, 'Meetingboard_list.html', {'meetingboards':paginator2})

def meetingboardNew(request):
    return render(request, 'meetingboard_new.html')

def meetingboardCreate(request):
    new_mb = MeetingBoard()
    new_mb.title = request.POST['title']
    new_mb.pub_date = timezone.datetime.now()
    new_mb.writer = request.user
    new_mb.body = request.POST['body']
    new_mb.law = request.POST['law']
    new_mb.save()
    return redirect('mb_list')

def meetingboardEdit(request, mb_id):
    edit_mb = MeetingBoard.objects.get(id = mb_id)
    return render(request,'meetingboard_edit.html',{'mb': edit_mb})

def meetingboardUpdate(request, mb_id):
    update_mb = MeetingBoard.objects.get(id = mb_id)
    update_mb.title = request.POST['title']
    update_mb.body = request.POST['body']
    update_mb.law = request.POST['law']
    update_mb.save()
    return redirect('mb_list')

def meetingboardDetail(request, mb_id):
    detail_mb = MeetingBoard.objects.get(id=mb_id)
    comment_mb = MB_comment.objects.filter(mbcomment= mb_id )
    return render(request, 'meetingboard_detail.html',{'mb':detail_mb, 'comments':comment_mb})

def meetingboardDelete(request, mb_id):
    delete_mb = MeetingBoard.objects.get(id=mb_id)
    delete_mb.delete()
    return redirect('mb_list')

def lawboardScrap(request, pk):
    scraped_law = get_object_or_404(LawBoard,pk=pk)
    scraped_law.scrap.add(request.user)
    scraped_law.save()
    return redirect('lb_list')

def lawboardCommentNew(request,lb_id):
    comment = LB_comment()
    user = request.user
    comment.comment_writer = get_object_or_404(User , username= user)
    comment.comment_content = request.POST['content']
    comment.lbcomment = get_object_or_404(LawBoard, pk = lb_id)
    comment.save()
    return redirect('lb_detail',lb_id)

def lawboardCommentDelete(request, comment_id):
    delete_comment = LB_comment.objects.get(id=comment_id )
    delete_comment.delete()
    return redirect('/lawboard/lawboard/'+str(delete_comment.lbcomment.id))

def meetingboardCommentNew(request,mb_id):
    comment = MB_comment()
    user = request.user
    comment.comment_writer = get_object_or_404(User , username= user)
    comment.comment_content = request.POST['content']
    comment.mbcomment = get_object_or_404(MeetingBoard, pk = mb_id)
    comment.save()
    return redirect('mb_detail',mb_id)

def meetingboardCommentDelete(request, comment_id):
    delete_comment = MB_comment.objects.get(id=comment_id )
    delete_comment.delete()
    return redirect('/lawboard/meetingboard/'+str(delete_comment.mbcomment.id))

