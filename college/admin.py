from django.contrib import admin
from college.models import Branch, Notice, Student, Assignment, Results, Attendance, Feedback

admin.site.register(Branch)

class NoticeAdmin(admin.ModelAdmin):
    list_filter = ["branch", "crdate"]
    list_display = ["subject" , "branch", "crdate"]
    search_fields = ["subject", "message"]
admin.site.register(Notice, NoticeAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_filter = ["branch", "sem", "skills"]
    list_display = ["name" , "branch", "sem", "phone_no"]
    search_fields = ["name", "branch", "rn"]
admin.site.register(Student, StudentAdmin)

class Feedbackadmin(admin.ModelAdmin):
    list_display = ["name", "subject", "message", "user"]
    list_filter = ["name", "user", "subject"]
admin.site.register(Feedback, Feedbackadmin)


class AssignmentAdmin(admin.ModelAdmin):
    list_filter = ["branch", "crdate", "duedate"]
    list_display = ["subject" , "branch", "crdate", "duedate"]
    search_fields = ["subject", "message"]
admin.site.register(Assignment, AssignmentAdmin)

class ResultAdmin(admin.ModelAdmin):
    list_filter = ["subject", "marks"]
    list_display = ["subject","student", "marks"]
    search_fields = ["subject","student"]
admin.site.register(Results, ResultAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    list_filter = ["subject","attend"]
    list_display = ["subject" , "student", "total_classes", "attend"]
    search_fields = ["subject" , "student"]
admin.site.register(Attendance, AttendanceAdmin)
