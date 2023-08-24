from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..logic import *
from ..models import *
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    active_nation = Nation.objects.get(pk=request.session.get('national_admin_nation_id'))
    announcements = active_nation.nationalannouncement_set.all()
    events = active_nation.nationalevent_set.all()
    authors = active_nation.author_set.all()

    context = {
        "areas": Area.objects.filter(nation=active_nation),
        "active_nation": active_nation,
        "admins": AreaAdmin.objects.filter(area__nation=active_nation),
        "announcements": announcements,
        "events": events,
        "authors": authors,
        "members_total": active_nation.get_members_total()
    }
    return render(request, 'thecop_app/nationalAdmin/home.html', context)


def areas(request):
    active_nation = Nation.objects.get(pk=request.session.get('national_admin_nation_id'))
    announcements = active_nation.nationalannouncement_set.all()
    events = active_nation.nationalevent_set.all()
    authors = active_nation.author_set.all()

    context = {
        "areas": Area.objects.filter(nation=active_nation),
        "active_nation": active_nation,
        "admins": AreaAdmin.objects.filter(area__nation=active_nation),
        "announcements": announcements,
        "events": events,
        "authors": authors,
        "members_total": active_nation.get_members_total()
    }
    return render(request, 'thecop_app/nationalAdmin/areas.html', context)


def admins(request):
    active_nation = Nation.objects.get(pk=request.session.get('national_admin_nation_id'))
    announcements = active_nation.nationalannouncement_set.all()
    events = active_nation.nationalevent_set.all()
    authors = active_nation.author_set.all()

    context = {
        "areas": Area.objects.filter(nation=active_nation),
        "active_nation": active_nation,
        "admins": AreaAdmin.objects.filter(area__nation=active_nation),
        "announcements": announcements,
        "events": events,
        "authors": authors,
        "members_total": active_nation.get_members_total()
    }
    return render(request, 'thecop_app/nationalAdmin/admins.html', context)


def members(request):
    active_nation = Nation.objects.get(pk=request.session.get('national_admin_nation_id'))
    announcements = active_nation.nationalannouncement_set.all()
    events = active_nation.nationalevent_set.all()
    authors = active_nation.author_set.all()

    context = {
        "areas": Area.objects.filter(nation=active_nation),
        "active_nation": active_nation,
        "admins": AreaAdmin.objects.filter(area__nation=active_nation),
        "announcements": announcements,
        "events": events,
        "authors": authors,
        "members_total": active_nation.get_members_total()
    }
    return render(request, 'thecop_app/nationalAdmin/members.html', context)


def login(request):
    context = {
        "countries": Nation.objects.all(),
    }
    if request.method == "POST":
        ep = request.POST["ep"]
        _id = request.POST["id"]
        password = request.POST["password"]
        nation = request.POST['nation']

        try:
            admin = NationalAdmin.objects.filter(nation=nation).get(pk=_id)
            if ep == admin.email or ep == admin.phone:
                if admin.password == password:
                    request.session['national_admin_nation_id'] = nation
                    request.session['active_admin_id'] = _id
                    return redirect("nationalAdmin_home")
                else:
                    return HttpResponse("Fail")
            else:
                return HttpResponse("Fail")
        except ObjectDoesNotExist:
            return HttpResponse("Fail")

    return render(request, 'thecop_app/nationalAdmin/login.html', context)


def add_area(request):
    active_nation = request.session.get('national_admin_nation_id')

    context = {
        "countries": Nation.objects.all(),
        "active_nation": Nation.objects.get(pk=active_nation),
    }
    if request.method == 'POST':
        nation = request.POST['nation']
        area_name = request.POST['area_name']
        location = request.POST['location']

        new_area = Area(
            id=generate_area_id(nation_id=nation),
            nation=Nation.objects.get(pk=nation),
            name=area_name,
            location=location
        )

        new_area.save()

        return redirect("nationalAdmin_home")

    return render(request, 'thecop_app/nationalAdmin/add_area.html', context)


def add_area_admin(request):
    active_nation = request.session.get('national_admin_nation_id')
    context = {
        "areas": Area.objects.filter(nation=active_nation),
    }

    if request.method == 'POST':
        area = request.POST['area']
        phone = request.POST['phone']
        email = request.POST['email']

        new_area_admin = AreaAdmin(
            id=generate_area_admin_id(area),
            phone=phone,
            email=email,
            password=phone,
            area=Area.objects.get(pk=area)
        )

        new_area_admin.save()

        return redirect("nationalAdmin_home")

    return render(request, 'thecop_app/nationalAdmin/add_area_admin.html', context)


def add_announcement(request):
    active_nation = Nation.objects.get(pk=request.session.get('national_admin_nation_id'))
    active_admin = NationalAdmin.objects.filter(nation=active_nation).get(pk=request.session.get("active_admin_id"))
    if request.method == 'POST':
        text = request.POST['text']

        active_admin.add_announcement(text)

        return redirect("nationalAdmin_home")

    context = {
        "nation": active_nation,
        "admin": active_admin
    }
    return render(request, "thecop_app/nationalAdmin/add_announcement.html", context)


def add_event(request):
    active_nation = Nation.objects.get(pk=request.session.get('national_admin_nation_id'))
    active_admin = NationalAdmin.objects.filter(nation=active_nation).get(pk=request.session.get("active_admin_id"))

    if request.method == 'POST':
        name = request.POST['name']
        start = request.POST['start']
        end = request.POST['end']
        venue = request.POST['venue']
        description = request.POST['description']

        active_admin.add_event(name=name, start=start, end=end, description=description, venue=venue)

        return redirect("nationalAdmin_home")

    return render(request, "thecop_app/nationalAdmin/add_event.html")


def add_author(request):
    active_nation = Nation.objects.get(pk=request.session.get('national_admin_nation_id'))
    active_admin = NationalAdmin.objects.filter(nation=active_nation).get(pk=request.session.get("active_admin_id"))

    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']

        active_admin.add_author(name=name, phone=phone)
        return redirect("nationalAdmin_home")

    return render(request, "thecop_app/nationalAdmin/add_author.html")
