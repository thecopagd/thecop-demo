from thecop_app.models import *
import random
import string
from django.core.exceptions import ObjectDoesNotExist



def generate_cop_admin_id(phone):
    prefix = "CAD"
    suffix = str(PentecostAdmin.objects.count() + 1)
    mid = str(phone[-3] + phone[-2] + phone[-1])

    return str(prefix + mid + suffix).upper()


def generate_nation_id(country):
    prefix = str(country[0] + country[1])
    suffix = str(Nation.objects.count() + 1)

    return str(prefix + suffix).upper()


def generate_national_admin_id(nation_id, phone):
    prefix = str(nation_id)
    mid = str(NationalAdmin.objects.filter(nation_id=nation_id).count() + 1)
    suffix = str(phone[-3] + phone[-2] + phone[-1])

    return str(prefix + mid + suffix).upper()


def generate_area_id(nation_id):
    nations_list = list(Nation.objects.all())
    nation = Nation.objects.get(pk=nation_id)
    indexx = nations_list.index(nation) + 1

    prefix = str("AR")
    mid = str(indexx)
    suffix = str(Area.objects.filter(nation=nation_id).count() + 1)

    return str(prefix + mid + suffix).upper()


def generate_area_admin_id(area_id):
    prefix = str("AD" + area_id[2:])
    suffix = str(AreaAdmin.objects.filter(area=area_id).count() + 1)

    return str(prefix + suffix).upper()


def generate_district_id(admin: AreaAdmin):
    prefix = str("DS" + admin.area.nation.id[2:] + admin.area.id[2:])
    suffix = str(District.objects.filter(area=admin.area.id).count() + 1)

    return str(prefix + suffix).upper()


def generate_district_admin_id(admin: AreaAdmin, district_id):
    prefix = str("DA" + district_id[2:])
    suffix = str(admin.area.district_set.get(pk=district_id).districtadmin_set.count() + 1)
    return str(prefix + suffix).upper()


def generate_local_id(admin: DistrictAdmin):
    prefix = str("LO" + admin.district.id[2:])
    suffix = str(LocalAssembly.objects.filter(district=admin.district.id).count() + 1)
    return str(prefix + suffix).upper()


def generate_local_admin_id(admin: DistrictAdmin, local_id):
    prefix = str("LA" + local_id[2:])
    suffix = str(admin.district.localassembly_set.get(pk=local_id).localadmin_set.count() + 1)
    return str(prefix + suffix).upper()


def generate_ministry_id():
    prefix = "MIN"
    suffix = str(Ministry.objects.count() + 1)
    return str(prefix + suffix).upper()


def generate_member_id(admin: LocalAdmin):
    prefix = str("MEM-")
    mid = str(admin.local_assembly.id[2:])
    suffix = str(admin.local_assembly.member_set.count() + 1)
    result = mid + suffix
    result = "-".join(result[i:i + 3] for i in range(0, len(result), 3))

    return str(prefix + result).upper()



