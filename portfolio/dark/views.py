from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.models import User
from users.models import Education,Project, Trainings, WorkHistory


# Create your views here.
def index(request):
    user_detail = User.objects.get(username = 'susansujakhu')
    educations = Education.objects.filter(user_name_id = user_detail.id)
    works = WorkHistory.objects.filter(user_name_id = user_detail.id)
    projects = Project.objects.filter(user_name_id = user_detail.id)
    training = Trainings.objects.filter(user_name_id = user_detail.id)
    context = {
        'user_detail' : user_detail,
        'educations' : educations,
        'works' : works,
        'projects' : projects,
        'training' : training
    }
    return render(request, 'dark/index.html', context)
