from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember

# Task A - CollegeAdmin [cite: 816]
@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ("college_name", "created_at", "updated_at") # [cite: 819]
    search_fields = ("college_name",) # [cite: 821]
    list_filter = ("created_at",) # [cite: 822]

# Task B - ProgramAdmin [cite: 825]
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("prog_name", "college") # [cite: 827]
    search_fields = ("prog_name", "college__college_name") # [cite: 829]
    list_filter = ("college",) # [cite: 831]

# Task C - OrganizationAdmin [cite: 834]
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "college", "description") # [cite: 837]
    search_fields = ("name", "description") # [cite: 839]
    list_filter = ("college",) # [cite: 841]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "lastname", "firstname", "middlename", "program") # [cite: 644-645]
    search_fields = ("lastname", "firstname") # [cite: 646]

@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ("student", "get_member_program", "organization", "date_joined") # [cite: 649]
    search_fields = ("student__lastname", "student__firstname") # [cite: 650, 655]

    def get_member_program(self, obj):
        try:
            return obj.student.program
        except:
            return None #