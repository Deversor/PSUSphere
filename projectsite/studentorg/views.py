from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.forms import OrganizationForm, OrgMemberForm, StudentForm
from django.urls import reverse_lazy
from studentorg.models import Organization, Student, OrgMember
from django.db.models import Q
from django.utils import timezone
class HomePageView(ListView):
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

#ORGLIST  
class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

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

#ORGMEMBER
class OrgMemberList(ListView):
    model = OrgMember
    context_object_name = 'orgmember'
    template_name = 'orgmember_list.html'
    paginate_by = 5

class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgmember_del.html'
    success_url = reverse_lazy('orgmember-list')

#STUDENT
class StudentList(ListView):
    model = Student
    context_object_name = 'student'
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