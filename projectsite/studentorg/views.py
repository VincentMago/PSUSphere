from multiprocessing import context
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember, Student, College, Program
from studentorg.forms import OrganizationForm, CollegeForm, ProgramForm, StudentForm, OrganizationMemberForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Student, Organization, OrgMember


class HomePageView(LoginRequiredMixin, ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"


def dashboard(request):
    return render(request, 'home.html')

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5


class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

class OrganizationMemberList(ListView):
    model = OrgMember
    context_object_name = 'organization_members'
    template_name = 'orgmember_list.html'
    paginate_by = 5


class OrganizationMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrganizationMemberForm
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('organization-member-list')

class OrganizationMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrganizationMemberForm
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('organization-member-list')

class OrganizationMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgmember_del.html'
    success_url = reverse_lazy('organization-member-list')

class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'student_list.html'
    paginate_by = 5

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')

class CollegeListView(ListView):
    model = College
    context_object_name = 'colleges'
    template_name = 'college_list.html'
    paginate_by = 5

class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_form.html'
    success_url = reverse_lazy('college-list')


class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_form.html'
    success_url = reverse_lazy('college-list')

class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')

class ProgramListView(ListView):
    model = Program
    context_object_name = 'programs'
    template_name = 'program_list.html'
    paginate_by = 5


class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_form.html'
    success_url = reverse_lazy('program-list')


class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_form.html'
    success_url = reverse_lazy('program-list')

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')
# Create your views here.
