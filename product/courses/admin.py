from django.contrib import admin
from courses.models import Course,Group


class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','author','start_date','price']

admin.site.register(Course,CourseAdmin)
    

class GroupsAdmin(admin.ModelAdmin):
    list_display = ['group_name','free_seats']
    
    pass
admin.site.register(Group,GroupsAdmin)