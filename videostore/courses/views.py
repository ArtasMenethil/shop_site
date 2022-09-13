from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Course, Lesson, Comments
from .forms import CourseAddForm, CommentForm


def tarrifsPage(request):
    return render(request, 'courses/tarrifs.html', {'title': 'Тарифы на сайте'})


class HomePage(ListView):
    model = Course
    template_name = 'courses/home.html'
    context_object_name = 'courses'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница'
        return ctx


class CourseDetailPage(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(CourseDetailPage, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        ctx['title'] = course
        ctx['lessons'] = Lesson.objects.filter(course=course).order_by('number')
        return ctx


class LessonDetailPage(DetailView):
    model = Course
    template_name = 'courses/lesson_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(LessonDetailPage, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        lesson = list(Lesson.objects.filter(course=course).filter(slug=self.kwargs['lesson_slug']).values())
        comments = Comments.objects.filter(lesson_com=lesson[0]['id']).all()

        ctx['comments'] = comments
        ctx['commForm'] = CommentForm()

        ctx['title'] = lesson[0]['title']
        ctx['desc'] = lesson[0]['description']
        ctx['lesson'] = lesson
        return ctx

    def post(self, request, *args, **kwargs):
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        lesson = Lesson.objects.filter(course=course).filter(slug=self.kwargs['lesson_slug']).first()

        post = request.POST.copy()
        post['author_com'] = request.user
        post['lesson_com'] = lesson
        request.POST = post

        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()

        url = self.kwargs['slug'] + '/' + self.kwargs['lesson_slug']
        return redirect('course' + url)


class CourseAdd(CreateView):
    model = Course
    form_class = CourseAddForm
    template_name = 'courses/add_course.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(CourseAdd, self).get_context_data(**kwargs)
        ctx['title'] = 'Страница добавления курса'
        return ctx




