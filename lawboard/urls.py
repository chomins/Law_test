from django.urls import path
from . import views

urlpatterns = [
    path('lawboard', views.lawboardList , name="lb_list"),
    path('lawboard/new', views.lawboardNew , name="lb_new"),
    path('lawboard/create', views.lawboardCreate , name="lb_create"),
    path('lawboard/edit/<int:lb_id>', views.lawboardEdit , name="lb_edit"),
    path('lawboard/update/<int:lb_id>', views.lawboardUpdate , name="lb_update"),
    path('lawboard/<int:lb_id>', views.lawboardDetail, name="lb_detail"),
    path('lawboard/delete/<int:lb_id>', views.lawboardDelete, name="lb_delete"),
    path('lawboard/filter', views.lawboardFilter, name="lb_filter"),
    path('lawboard/new_comment/<int:lb_id>', views.lawboardCommentNew, name="lb_comment"),
    path('lawboard/delete_comment/<int:comment_id>', views.lawboardCommentDelete, name="lb_commentd"),
    path('lawboard/scrap/<int:pk>',views.lawboardScrap, name="lb_scrap"),

    path('meetingboard', views.meetingboardList , name="mb_list"),
    path('meetingboard/new', views.meetingboardNew , name="mb_new"),
    path('meetingboard/create', views.meetingboardCreate , name="mb_create"),
    path('meetingboard/edit/<int:mb_id>', views.meetingboardEdit , name="mb_edit"),
    path('meetingboard/update/<int:mb_id>', views.meetingboardUpdate , name="mb_update"),
    path('meetingboard/<int:mb_id>', views.meetingboardDetail, name="mb_detail"),
    path('meetingboard/delete/<int:mb_id>', views.meetingboardDelete, name="mb_delete"),
    path('meetingboard/new_comment/<int:mb_id>',views.meetingboardCommentNew, name="mb_comment"),
    path('meetingboard/delete_comment/<int:comment_id>', views.meetingboardCommentDelete, name="mb_commentd"),

    

    
]