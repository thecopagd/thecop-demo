from django.db import models
from datetime import datetime
from django.utils.timezone import make_aware


# Create your models here.


def convert_to_date_obj(date: str):
    date_obj = datetime.strptime(date, "%m/%d/%Y")
    new_date_obj = date_obj.strftime("%Y-%m-%d")
    new_date_obj = datetime.strptime(new_date_obj, "%Y-%m-%d")
    new_date_obj = make_aware(new_date_obj)
    return new_date_obj


class PentecostAdmin(models.Model):
    id = models.TextField(primary_key=True)
    password = models.TextField()
    phone = models.TextField()
    email = models.TextField()


class Nation(models.Model):
    id = models.TextField(primary_key=True)
    country = models.TextField()

    def get_members_total(self):
        total = 0
        for i in Member.objects.all():
            if i.local_assembly.district.area.nation == self:
                total = total + 1
        return total

    def get_district_total(self):
        total = 0
        for i in District.objects.all():
            if i.area.nation == self:
                total = total + 1
        return total

    def get_local_total(self):
        total = 0
        for i in LocalAssembly.objects.all():
            if i.district.area.nation == self:
                total = total + 1
        return total

    def get_members(self):
        members = []
        for i in Member.objects.all():
            if i.local_assembly.district.area.nation == self:
                members.append(i)

        return members


class NationalAdmin(models.Model):
    id = models.TextField(primary_key=True)
    phone = models.TextField()
    email = models.TextField()
    password = models.TextField()
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)

    def add_announcement(self, text):
        ed = f"ann{self.nation.id[2:]}{self.nation.nationalannouncement_set.all().count() + 1}"
        new = NationalAnnouncement(
            id=ed,
            text=text,
            nation=self.nation
        )
        new.save()

    def add_event(self, name, start, end, description, venue):
        ed = f"EV{self.nation.id[2:]}{self.nation.nationalevent_set.all().count() + 1}"
        new = NationalEvent(
            id=ed,
            start=start,
            end=end,
            name=name,
            description=description,
            venue=venue,
            nation=self.nation,
        )
        new.save()

    def add_author(self, name, phone):
        iid = str(f"AU{self.nation.id[2:]}{self.nation.author_set.all().count() + 1}")

        new = Author(
            name=name,
            password=phone,
            nation=self.nation,
            phone=phone,
            id=iid
        )

        new.save()


class Area(models.Model):
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)
    id = models.TextField(primary_key=True)
    name = models.TextField()
    location = models.TextField()

    def get_local_total(self):
        total = 0
        for i in LocalAssembly.objects.all():
            if i.district.area == self:
                total = total + 1
        return total

    def get_members_total(self):
        total = 0
        for i in Member.objects.all():
            if i.local_assembly.district.area == self:
                total = total + 1
        return total

    def get_members(self):
        members = []
        for i in Member.objects.all():
            if i.local_assembly.district.area == self:
                members.append(i)

        return members

    def get_district_admins(self):
        admins = []
        for i in DistrictAdmin.objects.all():
            if i.district.area == self:
                admins.append(i)

        return admins


class AreaAdmin(models.Model):
    id = models.TextField(primary_key=True)
    phone = models.TextField()
    email = models.TextField()
    password = models.TextField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def add_announcement(self, text):
        ed = f"ann{self.area.id[2:]}{self.area.areaannouncement_set.all().count() + 1}"
        new = AreaAnnouncement(
            id=ed,
            text=text,
            area=self.area
        )
        new.save()

    def add_event(self, name, start, end, description, venue):
        ed = f"AEV{self.area.id[2:]}{self.area.areaevent_set.all().count() + 1}"
        new = AreaEvent(
            id=ed,
            start=start,
            end=end,
            name=name,
            description=description,
            venue=venue,
            area=self.area,
        )
        new.save()


class District(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    id = models.TextField(primary_key=True)
    name = models.TextField()
    location = models.TextField()

    def get_local_total(self):
        total = 0
        for i in LocalAssembly.objects.all():
            if i.district == self:
                total = total + 1
        return total

    def get_members_total(self):
        total = 0
        for i in Member.objects.all():
            if i.local_assembly.district == self:
                total = total + 1
        return total

    def get_members(self):
        members = []
        for i in Member.objects.all():
            if i.local_assembly.district == self:
                members.append(i)

        return members

    def get_local_admins(self):
        admins = []
        for i in LocalAdmin.objects.all():
            if i.local_assembly.district == self:
                admins.append(i)

        return admins


class DistrictAdmin(models.Model):
    id = models.TextField(primary_key=True)
    phone = models.TextField()
    email = models.TextField()
    password = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def add_announcement(self, text):
        ed = f"ann{self.district.id[2:]}{self.district.districtannouncement_set.all().count() + 1}"
        new = DistrictAnnouncement(
            id=ed,
            text=text,
            district=self.district
        )
        new.save()

    def add_event(self, name, start, end, description, venue):
        ed = f"DEV{self.district.id[2:]}{self.district.districtevent_set.all().count() + 1}"
        new = DistrictEvent(
            id=ed,
            start=start,
            end=end,
            name=name,
            description=description,
            venue=venue,
            district=self.district,
        )
        new.save()


class LocalAssembly(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    id = models.TextField(primary_key=True)
    name = models.TextField()
    location = models.TextField()


class LocalAdmin(models.Model):
    id = models.TextField(primary_key=True)
    phone = models.TextField()
    email = models.TextField()
    password = models.TextField()
    local_assembly = models.ForeignKey(LocalAssembly, on_delete=models.CASCADE)

    def add_announcement(self, text):
        ed = f"ann{self.local_assembly.id[2:]}{self.local_assembly.localannouncement_set.all().count() + 1}"
        new = LocalAnnouncement(
            id=ed,
            text=text,
            local=self.local_assembly
        )
        new.save()

    def add_event(self, name, start, end, description, venue):
        ed = f"LEV{self.local_assembly.id[2:]}{self.local_assembly.localevent_set.all().count() + 1}"
        new = LocalEvent(
            id=ed,
            start=start,
            end=end,
            name=name,
            description=description,
            venue=venue,
            local=self.local_assembly,
        )
        new.save()


class Ministry(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()
    max_age = models.PositiveIntegerField()
    min_age = models.PositiveIntegerField()


class Member(models.Model):
    id = models.TextField(primary_key=True)
    local_assembly = models.ForeignKey(LocalAssembly, on_delete=models.CASCADE)
    name = models.TextField()
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField(default="2004-02-18")
    phone = models.TextField()
    phone2 = models.TextField()
    email = models.TextField()
    address = models.TextField()
    password = models.TextField(default=phone)

    def get_national_announcements(self):
        return self.local_assembly.district.area.nation.nationalannouncement_set.all()

    def get_area_announcements(self):
        return self.local_assembly.district.area.areaannouncement_set.all()

    def get_district_announcements(self):
        return self.local_assembly.district.districtannouncement_set.all()

    def get_local_announcements(self):
        return self.local_assembly.district.area.areaannouncement_set.all()


class Author(models.Model):
    id = models.TextField(primary_key=True)
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)
    name = models.TextField()
    phone = models.TextField()
    password = models.TextField(default=phone)


class LocalAnnouncement(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    date = models.DateField(auto_now=True)
    text = models.TextField()
    local = models.ForeignKey(LocalAssembly, on_delete=models.CASCADE)


class DistrictAnnouncement(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    date = models.DateField(auto_now=True)
    text = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)


class AreaAnnouncement(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    date = models.DateField(auto_now=True)
    text = models.TextField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE)


class NationalAnnouncement(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    date = models.DateField(auto_now=True)
    text = models.TextField()
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)


class NationalEvent(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    start = models.DateField()
    end = models.DateField(default=datetime.now)
    name = models.CharField(max_length=100)
    description = models.TextField()
    venue = models.CharField(max_length=100, default="")
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="events/", default="events/default_event.jpg")

    def get_month(self):
        months = ["", "Jan", "Feb", "March", "April", "May", "June", "July", "August", "Sept", "Oct", "Nov",
                  "Dec"]
        return months[self.start.month]


class AreaEvent(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    start = models.DateField()
    end = models.DateField(default=datetime.now)
    name = models.CharField(max_length=100)
    description = models.TextField()
    venue = models.CharField(max_length=100, default="")
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="events/", default="events/default_event.jpg")

    def get_month(self):
        months = ["", "Jan", "Feb", "March", "April", "May", "June", "July", "August", "Sept", "Oct", "Nov",
                  "Dec"]
        return months[self.start.month]


class DistrictEvent(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    end = models.DateField(default=datetime.now)
    start = models.DateField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    venue = models.CharField(max_length=100, default="")
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="events/", default="events/default_event.jpg")

    def get_month(self):
        months = ["", "Jan", "Feb", "March", "April", "May", "June", "July", "August", "Sept", "Oct", "Nov",
                  "Dec"]
        return months[self.start.month]


class LocalEvent(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    start = models.DateField()
    end = models.DateField(default=datetime.now)
    name = models.CharField(max_length=100)
    description = models.TextField()
    venue = models.CharField(max_length=100, default="")
    local = models.ForeignKey(LocalAssembly, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="events/", default="events/default_event.jpg")

    def get_month(self):
        months = ["", "Jan", "Feb", "March", "April", "May", "June", "July", "August", "Sept", "Oct", "Nov",
                  "Dec"]
        return months[self.start.month]


class Songs(models.Model):
    lyrics = models.TextField()
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    title = models.CharField(max_length=100, default="Lyrics")



