from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from .forms import RegisterUserForm, LoginUserForm, CourseForm
from .models import Course, User, Profile


# Create your views here.
def index(request):
    template_name = "courses/index.html"
    context = {

    }
    return render(request, template_name, context)


def control_page(request):
    template_name = "courses/control.html"
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('control')
    course_list = Course.objects.all()
    paginator = Paginator(course_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'object_list': Course.objects.all(),
        'form': CourseForm(),
        'page_obj': page_obj,
    }

    return render(request, template_name, context)


def update_page(request, pk):
    course = Course.objects.get(id=pk)
    template_name = "courses/update.html"
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('control')

    context = {
        'form': CourseForm(instance=course),
        'course': course
    }

    return render(request, template_name, context)


def delete_page(request, pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return redirect('control')


class AllCoursesView(ListView):
    model = Course
    paginate_by = 5
    template_name = "courses/catalog.html"


class LearnCoursesView(ListView):
    model = Course
    paginate_by = 15
    template_name = "courses/learn.html"


class DetailCourseView(DetailView):
    model = Course
    template_name = "courses/detail.html"


def subscribe(request, pk):
    course = Course.objects.get(id=pk)
    request.user.profile.courses.add(course)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def unsubscribe(request, pk):
    course = Course.objects.get(id=pk)
    request.user.profile.courses.remove(course)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "courses/register.html"
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "courses/login.html"
    success_url = reverse_lazy('index')
