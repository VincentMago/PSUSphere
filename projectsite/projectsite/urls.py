"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView
from studentorg.views import StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView
from studentorg.views import CollegeListView, CollegeCreateView, CollegeUpdateView, CollegeDeleteView
from studentorg.views import ProgramListView, ProgramCreateView, ProgramUpdateView, ProgramDeleteView
from studentorg.views import OrganizationMemberList, OrganizationMemberCreateView, OrganizationMemberUpdateView, OrganizationMemberDeleteView
from studentorg import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('organization_list', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add', OrganizationCreateView.as_view(), name='organization-add'),
    path("organization_list/<int:pk>", OrganizationUpdateView.as_view(), name='organization-update'),
    path("organization_list/<int:pk>/delete", OrganizationDeleteView.as_view(), name='organization-delete'),

    path('organization_member_list', OrganizationMemberList.as_view(), name='organization-member-list'),
    path('organization_member_list/add', OrganizationMemberCreateView.as_view(), name='organization-member-add'),
    path('organization_member_list/<int:pk>', OrganizationMemberUpdateView.as_view(), name='organization-member-update'),
    path('organization_member_list/<int:pk>/delete', OrganizationMemberDeleteView.as_view(), name='organization-member-delete'),


    path('student_list', StudentListView.as_view(), name='student-list'),
    path('student_list/add', StudentCreateView.as_view(), name='student-add'), 
    path("student_list/<int:pk>", StudentUpdateView.as_view(), name='student-update'),
    path("student_list/<int:pk>/delete", StudentDeleteView.as_view(), name='student-delete'),

    path('college_list', CollegeListView.as_view(), name='college-list'),
    path('college_list/add', CollegeCreateView.as_view(), name='college-add'),
    path("college_list/<int:pk>", CollegeUpdateView.as_view(), name='college-update'),
    path("college_list/<int:pk>/delete", CollegeDeleteView.as_view(), name='college-delete'),

    path('program_list', ProgramListView.as_view(), name='program-list'),
    path('program_list/add', ProgramCreateView.as_view(), name='program-add'),
    path("program_list/<int:pk>", ProgramUpdateView.as_view(), name='program-update'),
    path('program_list/<int:pk>/delete', ProgramDeleteView.as_view(), name='program-delete'),
]