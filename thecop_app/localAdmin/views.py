from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..logic import *
from ..models import *
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    active_admin = LocalAdmin.objects.get(pk=request.session.get('local_admin_id'))

    context = {
        "members": Member.objects.all(),
        "admin": active_admin,
        "announcements": active_admin.local_assembly.localannouncement_set.all(),
        "events": active_admin.local_assembly.localevent_set.all()
    }
    return render(request, 'thecop_app/localAdmin/home.html', context)


def members(request):
    active_admin = LocalAdmin.objects.get(pk=request.session.get('local_admin_id'))

    context = {
        "members": Member.objects.all(),
        "admin": active_admin,
        "announcements": active_admin.local_assembly.localannouncement_set.all(),
        "events": active_admin.local_assembly.localevent_set.all()
    }
    return render(request, 'thecop_app/localAdmin/members.html', context)


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
        local = request.POST['local']

        try:
            admin = Nation.objects.get(pk=nation).area_set.get(pk=area).district_set.get(
                pk=district).localassembly_set.get(pk=local).localadmin_set.get(pk=_id)

            if ep == admin.email or ep == admin.phone:
                if admin.password == password:
                    request.session['local_admin_id'] = admin.id
                    return redirect("localAdmin_home")
                else:
                    return HttpResponse("Fail")
            else:
                return HttpResponse("Fail")
        except ObjectDoesNotExist:
            return HttpResponse("Fail")

    return render(request, 'thecop_app/localAdmin/login.html', context)


def add_member(request):
    active_admin = LocalAdmin.objects.get(pk=request.session.get('local_admin_id'))
    context = {
        'admin': active_admin
    }

    if request.method == 'POST':
        name = request.POST["name"]
        gender = request.POST["gender"]
        dob = request.POST["dob"]
        phone = request.POST['phone']
        phone2 = request.POST['phone2']
        email = request.POST['email']
        address = request.POST['address']

        new_member = Member(
            id=generate_member_id(admin=active_admin),
            local_assembly=active_admin.local_assembly,
            name=name,
            gender=gender,
            date_of_birth=dob,
            phone=phone,
            phone2=phone2,
            email=email,
            address=address,
            password=phone
        )

        new_member.save()

        return redirect('localAdmin_home')

    return render(request, 'thecop_app/localAdmin/add_member.html', context)


def add_announcement(request):
    active_admin = LocalAdmin.objects.get(pk=request.session.get('local_admin_id'))
    if request.method == 'POST':
        text = request.POST['text']

        active_admin.add_announcement(text)

        return redirect("localAdmin_home")

    context = {
        "nation": active_admin.local_assembly.district.area.nation,
        "admin": active_admin
    }
    return render(request, "thecop_app/localAdmin/add_announcement.html", context)


def add_event(request):
    active_admin = LocalAdmin.objects.get(pk=request.session.get('local_admin_id'))

    if request.method == 'POST':
        name = request.POST['name']
        start = request.POST['start']
        end = request.POST['end']
        venue = request.POST['venue']
        description = request.POST['description']

        active_admin.add_event(name=name, start=start, end=end, description=description, venue=venue)

        return redirect("localAdmin_home")

    return render(request, "thecop_app/localAdmin/add_event.html")
