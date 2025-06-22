from django.shortcuts import render
from user_agents import parse
from projects.models import Project, Skill, SkillCategory
from bread.bread import Bread


def get_context(request):
    mobile = False
    if hasattr(request, 'META'):
        user_agent = request.META.get('HTTP_USER_AGENT', '')

        if not isinstance(user_agent, str):
            user_agent = user_agent.decode('utf-8', 'ignore')

        mobile = parse(user_agent).is_mobile

    page = request.path

    return {"mobile": mobile, "page": page}


def get_projects(request):
    if request.GET.get("search", None) is not None:
        return {"projects": sorted(list(Project.objects.filter(tags__contains=request.GET.get("search"))))}

    return {"projects": sorted(list(Project.objects.all()))}


def get_skills(request):
    return {"skills": sorted(list(Skill.objects.all()))}


def get_skill_categories(request):
    return {"categories": sorted(list(SkillCategory.objects.all()))}


def get_bread_values(request):
    loaves = 2
    rolls = 0

    try:
        if request.GET.get("loaves") is not None:
            loaves = int(request.GET.get("loaves"))

        if request.GET.get("rolls") is not None:
            rolls = int(request.GET.get("rolls"))
    except ValueError:
        pass

    bread_values = Bread(loaves, rolls)
    return {"bread": bread_values.get_display_values()}


def index(request):
    return render(request, 'index.html', context=get_context(request))


def resume(request):
    return render(request, 'resume.html', context=get_context(request))


def about(request):
    context = get_context(request) | get_skills(request) | get_skill_categories(request)
    return render(request, 'about.html', context=context)


def projects(request):
    context = get_context(request) | get_projects(request)
    return render(request, 'projects.html', context=context)


def bread(request):
    context = get_context(request) | get_bread_values(request)
    return render(request, 'bread.html', context=context)
