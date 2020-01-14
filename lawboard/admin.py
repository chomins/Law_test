from django.contrib import admin
from .models import LawBoard, MeetingBoard

# Register your models here.
admin.site.register(LawBoard)
admin.site.register(MeetingBoard)
