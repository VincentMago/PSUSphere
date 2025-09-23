from multiprocessing import context
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember, Student, College, Program
from studentorg.forms import OrganizationForm, CollegeForm, ProgramForm, StudentForm, OrganizationMemberForm
from django.urls import reverse_lazy
from django.db.models import Q 
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(LoginRequiredMixin, ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_students"] = Student.objects.count()

        today = timezone.now().date()
        count = (
        OrgMember.objects.filter(
            date_joined__year=today.year
        )
        .values("student")
        .distinct()
        .count()
        )
        context["students_joined_this_year"] = count
        return context

def dashboard(request):
    return render(request, 'home.html')

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5
    ordering = ["college__college_name","name"]

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
        return qs

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

    def get_ordering(self):
        allowed = ["student__lastname", "organization__name", "date_joined"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "student__lastname"
    
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
            Q(student__lastname__icontains=query) |
            Q(student__firstname__icontains=query) |
            Q(organization__name__icontains=query)
        )
        return qs

class OrganizationMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrganizationMemberForm
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('organization-member-list')

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
            Q(student__lastname__icontains=query) |
            Q(student__firstname__icontains=query) |
            Q(organization__name__icontains=query)
        )
        return qs

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

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
            Q(lastname__icontains=query) |
            Q(firstname__icontains=query) |
            Q(student_id__icontains=query)
        )
        return qs

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

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
            Q(college_name__icontains=query)
        )
        return qs

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

    def get_ordering(self):
        allowed = ["prog_name", "college__college_name"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "prog_name"

class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_form.html'
    success_url = reverse_lazy('program-list')

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
            Q(prog_name__icontains=query) |
            Q(college__college_name__icontains=query)
        )
        return qs

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
