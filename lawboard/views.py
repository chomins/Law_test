from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.utils import timezone
from django.core.paginator import Paginator


def lawboardList(request):
    lawboards_list = LawBoard.objects.all()
    paginator = Paginator(lawboards_list,3)
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
    paginator = Paginator(lawboards,7)
    page = request.GET.get('page')
    paginator2 = paginator.get_page(page)

    return render(request, 'lawboard_list.html', {'lawboards':paginator2})


def lawboardNew(request):
    return render(request, 'lawboard_new.html')

def lawboardCreate(request):
    new_lb = LawBoard()
    new_lb.title = request.POST['title']
    new_lb.pub_date = timezone.datetime.now()
    new_lb.writer = request.user
    new_lb.body = request.POST['body']
    new_lb.save()
    return redirect('lb_list')

def lawboardEdit(request, lb_id):
    edit_lb = LawBoard.objects.get(id = lb_id)
    return render(request,'lawboard_edit.html',{'lb': edit_lb})

def lawboardUpdate(request, lb_id):
    update_lb = LawBoard.objects.get(id = lb_id)
    update_lb.title = request.POST['title']
    update_lb.body = request.POST['body']
    update_lb.save()
    return redirect('lb_list')

def lawboardDetail(request, lb_id):
    detail_lb = get_object_or_404(LawBoard,id=lb_id)
    comment_lb = LB_comment.objects.filter(lbcomment= lb_id )
    return render(request, 'lawboard_detail.html',{'lb':detail_lb, 'comments':comment_lb})

def lawboardDelete(request, lb_id):
    delete_lb = LawBoard.objects.get(id=lb_id)
    delete_lb.delete()
    return redirect('lb_list')


def meetingboardList(request):
    meetingboards= MeetingBoard.objects.all()
    return render(request, 'Meetingboard_list.html', {'meetingboards': meetingboards})

def meetingboardNew(request):
    return render(request, 'meetingboard_new.html')

def meetingboardCreate(request):
    new_mb = MeetingBoard()
    new_mb.title = request.POST['title']
    new_mb.pub_date = timezone.datetime.now()
    new_mb.writer = request.user
    new_mb.body = request.POST['body']
    new_mb.save()

    return redirect('mb_list')

def meetingboardEdit(request, mb_id):
    edit_mb = MeetingBoard.objects.get(id = mb_id)
    return render(request,'meetingboard_edit.html',{'mb': edit_mb})

def meetingboardUpdate(request, mb_id):
    update_mb = MeetingBoard.objects.get(id = mb_id)
    update_mb.title = request.POST['title']
    update_mb.body = request.POST['body']
    update_mb.save()
    return redirect('mb_list')

def meetingboardDetail(request, lb_id):
    detail_mb = MeetingBoard.objects.get(id=mb_id)
    return render(request, 'meetingboard_detail.html',{'lb':detail_mb})

def meetingboardDelete(request, lb_id):
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



