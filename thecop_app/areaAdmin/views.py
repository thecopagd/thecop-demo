from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..logic import *
from ..models import *
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    active_admin = AreaAdmin.objects.get(pk=request.session.get('area_admin_id'))

    context = {
        "admins": DistrictAdmin.objects.all(),
        "admin": active_admin,
        "announcements": active_admin.area.areaannouncement_set.all(),
        "events": active_admin.area.areaevent_set.all()
    }
    return render(request, 'thecop_app/areaAdmin/home.html', context)


def districts(request):
    active_admin = AreaAdmin.objects.get(pk=request.session.get('area_admin_id'))

    context = {
        "admins": DistrictAdmin.objects.all(),
        "admin": active_admin,
        "announcements": active_admin.area.areaannouncement_set.all(),
        "events": active_admin.area.areaevent_set.all()
    }
    return render(request, 'thecop_app/areaAdmin/districts.html', context)


def admins(request):
    active_admin = AreaAdmin.objects.get(pk=request.session.get('area_admin_id'))

    context = {
        "admins": DistrictAdmin.objects.all(),
        "admin": active_admin,
        "announcements": active_admin.area.areaannouncement_set.all(),
        "events": active_admin.area.areaevent_set.all()
    }
    return render(request, 'thecop_app/areaAdmin/admins.html', context)


def members(request):
    active_admin = AreaAdmin.objects.get(pk=request.session.get('area_admin_id'))

    context = {
        "admins": DistrictAdmin.objects.all(),
        "admin": active_admin,
        "announcements": active_admin.area.areaannouncement_set.all(),
        "events": active_admin.area.areaevent_set.all()
    }
    return render(request, 'thecop_app/areaAdmin/members.html', context)


def login(request):
    context = {
        "countries": Nation.objects.all(),
        "areas": Area.objects.all()
    }

    if request.method == "POST":
        ep = request.POST["ep"]
        _id = request.POST["id"]
        password = request.POST["password"]
        nation = request.POST['nation']
        area = request.POST['area']

        try:
            admin = Nation.objects.get(pk=nation).area_set.get(pk=area).areaadmin_set.get(pk=_id)
            if ep == admin.email or ep == admin.phone:
                if admin.password == password:
                    request.session['area_admin_id'] = admin.id
                    return redirect("areaAdmin_home")
                else:
                    return HttpResponse("Fail")
            else:
                return HttpResponse("Fail")
        except ObjectDoesNotExist:
            return HttpResponse("Fail")

    return render(request, 'thecop_app/areaAdmin/login.html', context)


def add_district(request):
    active_admin = AreaAdmin.objects.get(pk=request.session.get('area_admin_id'))
    context = {
        'admin': active_admin
    }
    if request.method == 'POST':
        district_name = request.POST['district_name']
        location = request.POST['location']

        new_district = District(
            id=generate_district_id(admin=active_admin),
            area=active_admin.area,
            name=district_name,
            location=location
        )

        new_district.save()

        return redirect("areaAdmin_home")

    return render(request, 'thecop_app/areaAdmin/add_district.html', context)


def add_district_admin(request):
    active_admin = AreaAdmin.objects.get(pk=request.session.get('area_admin_id'))
    context = {
        "admin": active_admin,
    }

    if request.method == 'POST':
        district_id = request.POST['district_id']
        phone = request.POST['phone']
        email = request.POST['email']

        new_district_admin = DistrictAdmin(
            id=generate_district_admin_id(admin=active_admin, district_id=district_id),
            phone=phone,
            email=email,
            password=phone,
            district=District.objects.get(pk=district_id)
        )

        new_district_admin.save()

        return redirect("areaAdmin_home")

    return render(request, 'thecop_app/areaAdmin/add_district_admin.html', context)


def add_announcement(request):
    active_admin = AreaAdmin.objects.get(pk=request.session.get('area_admin_id'))

    if request.method == 'POST':
        text = request.POST['text']

        active_admin.add_announcement(text)

        return redirect("areaAdmin_home")

    context = {
        "admin": active_admin
    }
    return render(request, "thecop_app/areaAdmin/add_announcement.html", context)


def add_event(request):
    active_admin = AreaAdmin.objects.get(pk=request.session.get('area_admin_id'))

    if request.method == 'POST':
        name = request.POST['name']
        start = request.POST['start']
        end = request.POST['end']
        venue = request.POST['venue']
        description = request.POST['description']

        active_admin.add_event(name=name, start=start, end=end, description=description, venue=venue)

        return redirect("areaAdmin_home")

    return render(request, "thecop_app/areaAdmin/add_event.html")
