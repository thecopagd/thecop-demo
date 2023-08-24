from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..logic import *
from ..models import *
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    context = {
        "countries": Nation.objects.all(),
        "admins": NationalAdmin.objects.all(),
        "locals_total": LocalAssembly.objects.all().count(),
        "districts_total": District.objects.all().count(),
        "areas_total": Area.objects.all().count(),
        "nations_total": Nation.objects.all().count(),
        "members_total": Member.objects.all().count(),

    }
    return render(request, 'thecop_app/pentAdmin/home.html', context)


def nations(request):
    context = {
        "countries": Nation.objects.all(),
        "admins": NationalAdmin.objects.all(),
        "locals_total": LocalAssembly.objects.all().count(),
        "districts_total": District.objects.all().count(),
        "areas_total": Area.objects.all().count(),
        "nations_total": Nation.objects.all().count(),
        "members_total": Member.objects.all().count(),
    }
    return render(request, 'thecop_app/pentAdmin/nations.html', context)


def admins(request):
    context = {
        "countries": Nation.objects.all(),
        "admins": NationalAdmin.objects.all(),
        "locals_total": LocalAssembly.objects.all().count(),
        "districts_total": District.objects.all().count(),
        "areas_total": Area.objects.all().count(),
        "nations_total": Nation.objects.all().count(),
        "members_total": Member.objects.all().count(),

    }
    return render(request, 'thecop_app/pentAdmin/admins.html', context)


def members(request):
    context = {
        "countries": Nation.objects.all(),
        "admins": NationalAdmin.objects.all(),
        "locals_total": LocalAssembly.objects.all().count(),
        "districts_total": District.objects.all().count(),
        "areas_total": Area.objects.all().count(),
        "nations_total": Nation.objects.all().count(),
        "members_total": Member.objects.all().count(),
        "members": Member.objects.all()

    }
    return render(request, 'thecop_app/pentAdmin/members.html', context)


def signup(request):
    if request.method == "POST":
        phone = request.POST["phone"]
        email = request.POST["email"]
        password = request.POST["password"]

        new_admin = PentecostAdmin(
            id=generate_cop_admin_id(phone),
            email=email,
            password=password,
            phone=phone
        )

        new_admin.save()

        return redirect("copAdmin_home")
    return render(request, 'thecop_app/pentAdmin/copadmin_signup.html')


def login(request):
    if request.method == "POST":
        ep = request.POST["ep"]
        _id = request.POST["id"]
        password = request.POST["password"]

        try:
            admin = PentecostAdmin.objects.get(pk=_id)
            if ep == admin.email or ep == admin.phone:
                if admin.password == password:
                    return redirect("copAdmin_home")
                else:
                    return HttpResponse("Fail")
            else:
                return HttpResponse("Fail")
        except ObjectDoesNotExist:
            return HttpResponse("Fail")

    return render(request, 'thecop_app/pentAdmin/copadmin_login.html')


def add_nation(request):
    if request.method == 'POST':
        country = request.POST['country']

        new_country = Nation(
            id=generate_nation_id(country),
            country=country
        )

        new_country.save()

        return redirect("copAdmin_home")

    return render(request, 'thecop_app/pentAdmin/addnation.html')


def add_nation_admin(request):
    context = {
        "countries": Nation.objects.all(),
    }

    if request.method == 'POST':
        nation = request.POST['nation']
        phone = request.POST['phone']
        email = request.POST['email']

        new_national_admin = NationalAdmin(
            id=generate_national_admin_id(nation, phone),
            phone=phone,
            email=email,
            password=phone,
            nation=Nation.objects.get(pk=nation)
        )

        new_national_admin.save()

        return redirect("copAdmin_home")

    return render(request, 'thecop_app/pentAdmin/addnationadmin.html', context)
