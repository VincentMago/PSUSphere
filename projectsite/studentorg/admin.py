from django.contrib import admin

# Register your models here.
from .models import College, Program, Organization, Student, OrgMember


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ("college_name", "created_at", "updated_at")
    search_fields = ("college_name",)


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("prog_name", "college", "created_at")
    search_fields = ("prog_name", "college__college_name")


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "college", "description", "created_at")
    search_fields = ("name", "college__college_name")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "lastname", "firstname", "middlename", "program")
    search_fields = ("lastname", "firstname", "student_id")


@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ("student", "organization", "date_joined")
    search_fields = ("student__lastname", "student__firstname")