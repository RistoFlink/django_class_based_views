from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from classroom.models import Teacher
from classroom.forms import ContactForm

# Create your views here.

class HomeView(TemplateView):
    template_name = "classroom/home.html"

class ThanksView(TemplateView):
    template_name = "classroom/thanks.html"

class TeacherCreateView(CreateView):
    model = Teacher
    #model_form.html
    #.save()
    fields = "__all__"
    success_url = reverse_lazy("classroom:thanks")

class TeacherListView(ListView):
    #looks for a template model_list.html
    model = Teacher
    queryset = Teacher.objects.order_by("first_name")
    context_object_name = "teacher_list"

class TeacherDetailView(DetailView):
    #RETURN ONLY ONE MODEL ENTRY PK
    #looks for model_detail.html
    model = Teacher
    #PK -> {{ teacher }}

class TeacherUpdateView(UpdateView):
    #shares mode_form.html with CreateView
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy("classroom:list_teacher")

class TeacherDeleteView(DeleteView):
    #sends back a form with a confirm deletion button
    #default template name: model_confirm_delete.html
    model = Teacher
    success_url = reverse_lazy("classroom:list_teacher")

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "classroom/contact.html"

    # where to go after a succesful post? URL not a template file!
    success_url = reverse_lazy("classroom:thanks")
    # what to do with the form?
    def form_valid(self, form):
        print(form.cleaned_data)
        #similar to ContactForm(request.POST)
        return super().form_valid(form)