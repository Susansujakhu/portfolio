from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from users.forms import ContactForm
from users.models import Education, WorkHistory, Project, Trainings, Skill
from django.contrib import messages

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    user_detail = User.objects.get(username = 'susansujakhu')
    educations = Education.objects.filter(user_name_id = user_detail.id)
    works = WorkHistory.objects.filter(user_name_id = user_detail.id)
    projects = Project.objects.filter(user_name_id = user_detail.id).order_by('-start_date')
    training = Trainings.objects.filter(user_name_id = user_detail.id)
    skills = Skill.objects.filter(user_name_id = user_detail.id).order_by('priority')

    form = ContactForm(request.POST or None)

    context = {
        'user_detail' : user_detail,
        'educations' : educations,
        'works' : works,
        'projects' : projects,
        'training' : training,
        'skills' : skills,
        'form' : form
    }
    if form.is_valid():
        name = form.cleaned_data.get('name')
        subject = form.cleaned_data.get('subject')
        email = form.cleaned_data.get('email')
        message = "From "+email+"\n"+form.cleaned_data.get('message')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['sushansujakhu14@gmail.com', ]
        send_mail( subject, message, email_from, recipient_list )

        form.save()
        messages.success(request, f'✔️ You message has been sent. Thank You {name}')
        return redirect(reverse('resume:index') + '#contact')

    return render(request, 'resume/index.html', context)