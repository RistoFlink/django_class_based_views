from django.urls import path
from .views import HomeView, ThanksView, ContactFormView, TeacherCreateView, TeacherListView, TeacherDetailView, TeacherUpdateView, TeacherDeleteView

app_name = "classroom"
# domain.com/classroom
urlpatterns = [
    path("", HomeView.as_view(), name="home"), #path expect a function
    path("thanks/", ThanksView.as_view(), name="thanks"),
    path("contact/", ContactFormView.as_view(), name="contact"),
    path("create_teacher/", TeacherCreateView.as_view(), name="create_teacher"),
    path("list_teacher", TeacherListView.as_view(), name="list_teacher"),
    path("teacher_detail/<int:pk>", TeacherDetailView.as_view(), name="teacher_detail"),
    path("teacher_update/<int:pk>", TeacherUpdateView.as_view(), name="teacher_update"),
    path("teacher_delete/<int:pk>", TeacherDeleteView.as_view()),
]