from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..logic import *
from ..models import *
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone


def home(request):
    if request.session.get("member_id") is None:
        return redirect("member_login")
    else:
        try:
            member = Member.objects.get(pk=request.session.get("member_id"))

            upcoming_events = []

            current_datetime = timezone.now()

            for event in NationalEvent.objects.filter(start__gte=current_datetime).order_by('start'):
                upcoming_events.append(event)
            for event in AreaEvent.objects.filter(start__gte=current_datetime).order_by('start'):
                upcoming_events.append(event)
            for event in DistrictEvent.objects.filter(start__gte=current_datetime).order_by('start'):
                upcoming_events.append(event)
            for event in LocalEvent.objects.filter(start__gte=current_datetime).order_by('start'):
                upcoming_events.append(event)

            context = {
                "member": member,
                "upcoming_events": upcoming_events
            }
            return render(request, "thecop_app/member/home.html", context)
        except ObjectDoesNotExist:
            return redirect("member_login")
    return redirect("member_login")


def login(request):
    context = {
        "countries": Nation.objects.all()
    }

    if request.method == "POST":
        ep = request.POST["ep"]
        _id = request.POST["id"]
        password = request.POST["password"]
        nation = request.POST['nation']
        area = request.POST['area']
        district = request.POST['district']
        local = request.POST['local']

        try:
            member = Nation.objects.get(pk=nation).area_set.get(pk=area).district_set.get(
                pk=district).localassembly_set.get(pk=local).member_set.get(pk=_id)

            if ep == member.email or ep == member.phone:
                if member.password == password:
                    request.session['member_id'] = member.id
                    return redirect("member_home")
                else:
                    return HttpResponse("Fail")
            else:
                return HttpResponse("Fail")
        except ObjectDoesNotExist:
            return HttpResponse("Fail")

    return render(request, "thecop_app/member/login.html", context)


def me(request):
    active_member = Member.objects.get(pk=request.session.get("member_id"))
    context = {
        "member": active_member
    }
    return render(request, "thecop_app/member/me.html", context)


def headlines(request):
    active_member = Member.objects.get(pk=request.session.get("member_id"))
    recent_articles = Article.objects.order_by('-date_created')[:4]

    context = {
        "member": active_member,
        "recent_articles": recent_articles
    }
    return render(request, "thecop_app/member/headlines.html", context)


def read_art(request, art_id):
    active_member = Member.objects.get(pk=request.session.get("member_id"))
    recent_articles = Article.objects.order_by('-date_created')[:6]
    article = Article.objects.get(pk=art_id)
    context = {
        "member": active_member,
        "recent_articles": recent_articles,
        "article": article
    }
    return render(request, "thecop_app/member/article.html", context)
