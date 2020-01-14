from django.contrib import admin
from .models import LawBoard, MeetingBoard , LB_comment

# Register your models here.
admin.site.register(LawBoard)
admin.site.register(MeetingBoard)
admin.site.register(LB_comment)
