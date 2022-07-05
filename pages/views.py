from django.shortcuts import render
from user_agents import parse
from .models import Project, Skill


def get_context(request):
    mobile = False
    if hasattr(request, 'META'):
        user_agent = request.META.get('HTTP_USER_AGENT', '')

        if not isinstance(user_agent, str):
            user_agent = user_agent.decode('utf-8', 'ignore')

        mobile = parse(user_agent).is_mobile

    return {"mobile": mobile}


def get_projects(request):
    if request.GET.get("search", None) is not None:
        return {"projects": Project.objects.filter(tags__contains=request.GET.get("search"))}

    return {"projects": Project.objects.all()}


def get_skills(request):
    return {"skills": Skill.objects.all()}


def index(request):
    return render(request, 'index.html', context=get_context(request))


def resume(request):
    return render(request, 'resume.html', context=get_context(request))


def about(request):
    context = get_context(request) | get_skills(request)
    return render(request, 'about.html', context=context)


def projects(request):
    context = get_context(request) | get_projects(request)
    return render(request, 'projects.html', context=context)
