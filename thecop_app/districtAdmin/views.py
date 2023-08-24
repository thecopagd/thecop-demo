from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..logic import *
from ..models import *
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    active_admin = DistrictAdmin.objects.get(pk=request.session.get('district_admin_id'))
    context = {
        "admins": DistrictAdmin.objects.all(),
        "admin": active_admin,
        "announcements": active_admin.district.districtannouncement_set.all(),
        "events": active_admin.district.districtevent_set.all()
    }
    return render(request, 'thecop_app/districtAdmin/home.html', context)


def locals(request):
    active_admin = DistrictAdmin.objects.get(pk=request.session.get('district_admin_id'))
    context = {
        "admins": DistrictAdmin.objects.all(),
        "admin": active_admin,
        "announcements": active_admin.district.districtannouncement_set.all(),
        "events": active_admin.district.districtevent_set.all()
    }
    return render(request, 'thecop_app/districtAdmin/locals.html', context)


def admins(request):
    active_admin = DistrictAdmin.objects.get(pk=request.session.get('district_admin_id'))
    context = {
        "admins": DistrictAdmin.objects.all(),
        "admin": active_admin,
        "announcements": active_admin.district.districtannouncement_set.all(),
        "events": active_admin.district.districtevent_set.all()
    }
    return render(request, 'thecop_app/districtAdmin/admins.html', context)


def members(request):
    active_admin = DistrictAdmin.objects.get(pk=request.session.get('district_admin_id'))
    context = {
        "admins": DistrictAdmin.objects.all(),
        "admin": active_admin,
        "announcements": active_admin.district.districtannouncement_set.all(),
        "events": active_admin.district.districtevent_set.all()
    }
    return render(request, 'thecop_app/districtAdmin/members.html', context)


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
        district = request.POST['district']

        try:
            admin = Nation.objects.get(pk=nation).area_set.get(pk=area).district_set.get(
                pk=district).districtadmin_set.get(pk=_id)

            if ep == admin.email or ep == admin.phone:
                if admin.password == password:
                    request.session['district_admin_id'] = admin.id
                    return redirect("districtAdmin_home")
                else:
                    return HttpResponse("Fail")
            else:
                return HttpResponse("Fail")
        except ObjectDoesNotExist:
            return HttpResponse("Fail")

    return render(request, 'thecop_app/districtAdmin/login.html', context)


def add_local(request):
    active_admin = DistrictAdmin.objects.get(pk=request.session.get('district_admin_id'))
    context = {
        'admin': active_admin
    }
    if request.method == 'POST':
        local_name = request.POST['local_name']
        location = request.POST['location']

        new_local = LocalAssembly(
            id=generate_local_id(admin=active_admin),
            district=active_admin.district,
            name=local_name,
            location=location
        )

        new_local.save()

        return redirect("districtAdmin_home")

    return render(request, 'thecop_app/districtAdmin/add_local.html', context)


def add_local_admin(request):
    active_admin = DistrictAdmin.objects.get(pk=request.session.get('district_admin_id'))
    context = {
        "admin": active_admin,
    }

    if request.method == 'POST':
        local_id = request.POST['local_id']
        phone = request.POST['phone']
        email = request.POST['email']

        new_local_admin = LocalAdmin(
            id=generate_local_admin_id(admin=active_admin, local_id=local_id),
            phone=phone,
            email=email,
            password=phone,
            local_assembly=LocalAssembly.objects.get(pk=local_id)
        )

        new_local_admin.save()

        return redirect("districtAdmin_home")

    return render(request, 'thecop_app/districtAdmin/add_local_admin.html', context)


def add_announcement(request):
    active_admin = DistrictAdmin.objects.get(pk=request.session.get('district_admin_id'))
    if request.method == 'POST':
        text = request.POST['text']

        active_admin.add_announcement(text)

        return redirect("districtAdmin_home")

    context = {
        "nation": active_admin.district.area.nation,
        "admin": active_admin
    }
    return render(request, "thecop_app/districtAdmin/add_announcement.html", context)


def add_event(request):
    active_admin = DistrictAdmin.objects.get(pk=request.session.get('district_admin_id'))

    if request.method == 'POST':
        name = request.POST['name']
        start = request.POST['start']
        end = request.POST['end']
        venue = request.POST['venue']
        description = request.POST['description']

        active_admin.add_event(name=name, start=start, end=end, description=description, venue=venue)

        return redirect("districtAdmin_home")

    return render(request, "thecop_app/districtAdmin/add_event.html")
