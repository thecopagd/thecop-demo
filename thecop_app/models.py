import random
import string

from django.db import models
from datetime import datetime
from django.utils.timezone import make_aware
from datetime import date

# Create your models here.

today = date.today()


def convert_to_date_obj(date: str):
    date_obj = datetime.strptime(date, "%m/%d/%Y")
    new_date_obj = date_obj.strftime("%Y-%m-%d")
    new_date_obj = datetime.strptime(new_date_obj, "%Y-%m-%d")
    new_date_obj = make_aware(new_date_obj)
    return new_date_obj


def generate_article_id():
    num = str(Article.objects.count())
    length = 6
    random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    # Store the result in a variable called "random_string"
    random_string = num + random_chars
    random.shuffle(list(random_string))

    char_list = list(random_string)
    random.shuffle(char_list)
    shuffled_string = ''.join(char_list)

    return shuffled_string


def global_get_adults(level):
    adult_min_age = 36
    adult_min_birthdate = today.replace(year=today.year - adult_min_age)

    if type(level) is Nation:
        adults = Member.objects.filter(date_of_birth__lte=adult_min_birthdate, local_assembly__district__area__nation=level)
        adults_men = Member.objects.filter(date_of_birth__lte=adult_min_birthdate, gender="Male",
                                           local_assembly__district__area__nation=level)
        adults_women = Member.objects.filter(date_of_birth__lte=adult_min_birthdate, gender="Female",
                                             local_assembly__district__area__nation=level)

        return [adults, adults_men, adults_women]

    if type(level) is Area:
        adults = Member.objects.filter(date_of_birth__lte=adult_min_birthdate,
                                       local_assembly__district__area=level)
        adults_men = Member.objects.filter(date_of_birth__lte=adult_min_birthdate, gender="Male",
                                           local_assembly__district__area=level)
        adults_women = Member.objects.filter(date_of_birth__lte=adult_min_birthdate, gender="Female",
                                             local_assembly__district__area=level)

        return [adults, adults_men, adults_women]

    if type(level) is District:
        adults = Member.objects.filter(date_of_birth__lte=adult_min_birthdate,
                                       local_assembly__district=level)
        adults_men = Member.objects.filter(date_of_birth__lte=adult_min_birthdate, gender="Male",
                                           local_assembly__district=level)
        adults_women = Member.objects.filter(date_of_birth__lte=adult_min_birthdate, gender="Female",
                                             local_assembly__district=level)

        return [adults, adults_men, adults_women]

    if type(level) is LocalAssembly:
        adults = Member.objects.filter(date_of_birth__lte=adult_min_birthdate,
                                       local_assembly=level)
        adults_men = Member.objects.filter(date_of_birth__lte=adult_min_birthdate, gender="Male",
                                           local_assembly=level)
        adults_women = Member.objects.filter(date_of_birth__lte=adult_min_birthdate, gender="Female",
                                             local_assembly=level)

        return [adults, adults_men, adults_women]


def global_get_adults_count(level):
    return [level.get_adults()[0].count(), level.get_adults()[1].count(), level.get_adults()[2].count()]


def global_get_youth(level):
    adult_min_age = 36
    adult_min_birthdate = today.replace(year=today.year - adult_min_age)
    youth_max_age = 13
    youth_max_birthdate = today.replace(year=today.year - youth_max_age)

    if type(level) is Nation:
        youths = Member.objects.filter(
            date_of_birth__gt=adult_min_birthdate, date_of_birth__lte=youth_max_birthdate,
            local_assembly__district__area__nation=level
        )
        youths_male = Member.objects.filter(
            date_of_birth__gt=adult_min_birthdate, date_of_birth__lte=youth_max_birthdate, gender="Male",
            local_assembly__district__area__nation=level
        )
        youths_female = Member.objects.filter(
            date_of_birth__gt=adult_min_birthdate, date_of_birth__lte=youth_max_birthdate, gender="Female",
            local_assembly__district__area__nation=level
        )
        return [youths, youths_male, youths_female]

    if type(level) is Area:
        youths = Member.objects.filter(
            date_of_birth__gt=adult_min_birthdate, date_of_birth__lte=youth_max_birthdate,
            local_assembly__district__area=level
        )
        youths_male = Member.objects.filter(
            date_of_birth__gt=adult_min_birthdate, date_of_birth__lte=youth_max_birthdate, gender="Male",
            local_assembly__district__area=level
        )
        youths_female = Member.objects.filter(
            date_of_birth__gt=adult_min_birthdate, date_of_birth__lte=youth_max_birthdate, gender="Female",
            local_assembly__district__area=level
        )
        return [youths, youths_male, youths_female]

    if type(level) is District:
        youths = Member.objects.filter(
            date_of_birth__gt=adult_min_birthdate, date_of_birth__lte=youth_max_birthdate,
            local_assembly__district=level
        )
        youths_male = Member.objects.filter(
            date_of_birth__gt=adult_min_birthdate, date_of_birth__lte=youth_max_birthdate, gender="Male",
            local_assembly__district=level
        )
        youths_female = Member.objects.filter(
            date_of_birth__gt=adult_min_birthdate, date_of_birth__lte=youth_max_birthdate, gender="Female",
            local_assembly__district=level
        )
        return [youths, youths_male, youths_female]

    if type(level) is LocalAssembly:
        youths = Member.objects.filter(
            date_of_birth__gt=adult_min_birthdate, date_of_birth__lte=youth_max_birthdate,
            local_assembly=level
        )
        youths_male = Member.objects.filter(
            date_of_birth__gt=adult_min_birthdate, date_of_birth__lte=youth_max_birthdate, gender="Male",
            local_assembly=level
        )
        youths_female = Member.objects.filter(
            date_of_birth__gt=adult_min_birthdate, date_of_birth__lte=youth_max_birthdate, gender="Female",
            local_assembly=level
        )
        return [youths, youths_male, youths_female]


def global_get_youth_count(level):
    return [level.get_youth()[0].count(), level.get_youth()[1].count(), level.get_youth()[2].count()]


def global_get_children(level):
    youth_max_age = 13
    youth_max_birthdate = today.replace(year=today.year - youth_max_age)
    child_max_age = 12
    child_max_birthdate = today.replace(year=today.year - child_max_age)
    if type(level) is Nation:
        children = Member.objects.filter(date_of_birth__gt=youth_max_birthdate,
                                         local_assembly__district__area__nation=level)
        children_male = Member.objects.filter(date_of_birth__gt=youth_max_birthdate, gender="Male",
                                              local_assembly__district__area__nation=level)
        children_female = Member.objects.filter(date_of_birth__gt=youth_max_birthdate, gender="Female",
                                                local_assembly__district__area__nation=level)

        return [children, children_male, children_female]

    if type(level) is Area:
        children = Member.objects.filter(date_of_birth__gt=youth_max_birthdate,
                                         local_assembly__district__area=level)
        children_male = Member.objects.filter(date_of_birth__gt=youth_max_birthdate, gender="Male",
                                              local_assembly__district__area=level)
        children_female = Member.objects.filter(date_of_birth__gt=youth_max_birthdate, gender="Female",
                                                local_assembly__district__area=level)

        return [children, children_male, children_female]

    if type(level) is District:
        children = Member.objects.filter(date_of_birth__gt=youth_max_birthdate,
                                         local_assembly__district=level)
        children_male = Member.objects.filter(date_of_birth__gt=youth_max_birthdate, gender="Male",
                                              local_assembly__district=level)
        children_female = Member.objects.filter(date_of_birth__gt=youth_max_birthdate, gender="Female",
                                                local_assembly__district=level)

        return [children, children_male, children_female]

    if type(level) is LocalAssembly:
        children = Member.objects.filter(date_of_birth__gt=youth_max_birthdate,
                                         local_assembly=level)
        children_male = Member.objects.filter(date_of_birth__gt=youth_max_birthdate, gender="Male",
                                              local_assembly=level)
        children_female = Member.objects.filter(date_of_birth__gt=youth_max_birthdate, gender="Female",
                                                local_assembly=level)

        return [children, children_male, children_female]


def global_get_children_count(level):
    return [level.get_children()[0].count(), level.get_children()[1].count(), level.get_children()[2].count()]


class PentecostAdmin(models.Model):
    id = models.TextField(primary_key=True)
    password = models.TextField()
    phone = models.TextField()
    email = models.TextField()

    def get_adults(self):
        adult_min_age = 36
        adult_min_birthdate = today.replace(year=today.year - adult_min_age)
        adults = Member.objects.filter(date_of_birth__lte=adult_min_birthdate)
        adults_men = Member.objects.filter(date_of_birth__lte=adult_min_birthdate, gender="Male")
        adults_women = Member.objects.filter(date_of_birth__lte=adult_min_birthdate, gender="Female")
        return [adults, adults_men, adults_women]

    def get_adults_count(self):
        return [self.get_adults()[0].count(), self.get_adults()[1].count(), self.get_adults()[2].count()]

    def get_youth(self):
        adult_min_age = 36
        adult_min_birthdate = today.replace(year=today.year - adult_min_age)
        youth_max_age = 13
        youth_max_birthdate = today.replace(year=today.year - youth_max_age)
        youths = Member.objects.filter(
            date_of_birth__gt=adult_min_birthdate, date_of_birth__lte=youth_max_birthdate
        )
        youths_male = Member.objects.filter(
            date_of_birth__gt=adult_min_birthdate, date_of_birth__lte=youth_max_birthdate, gender="Male"
        )
        youths_female = Member.objects.filter(
            date_of_birth__gt=adult_min_birthdate, date_of_birth__lte=youth_max_birthdate, gender="Female"
        )
        return [youths, youths_male, youths_female]

    def get_youth_count(self):
        return [self.get_youth()[0].count(), self.get_youth()[1].count(), self.get_youth()[2].count()]

    def get_children(self):
        youth_max_age = 13
        youth_max_birthdate = today.replace(year=today.year - youth_max_age)
        child_max_age = 12
        child_max_birthdate = today.replace(year=today.year - child_max_age)
        children = Member.objects.filter(date_of_birth__gt=youth_max_birthdate)
        children_male = Member.objects.filter(date_of_birth__gt=youth_max_birthdate, gender="Male")
        children_female = Member.objects.filter(date_of_birth__gt=youth_max_birthdate, gender="Female")

        return [children, children_male, children_female]

    def get_children_count(self):
        return [self.get_children()[0].count(), self.get_children()[1].count(), self.get_children()[2].count()]


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

    def get_announcements(self):
        return self.nationalannouncement_set.all()

    def get_adults(self):
        return global_get_adults(self)

    def get_adults_count(self):
        return global_get_adults_count(self)

    def get_youth(self):
        return global_get_youth(self)

    def get_youth_count(self):
        return global_get_youth_count(self)

    def get_children(self):
        return global_get_children(self)

    def get_children_count(self):
        return global_get_children_count(self)


class NationalAdmin(models.Model):
    id = models.TextField(primary_key=True)
    phone = models.TextField()
    email = models.TextField()
    password = models.TextField()
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)

    def add_announcement(self, text):
        if self.nation.nationalannouncement_set.count() == 0:
            ed = f"ann{self.nation.id[2:]}1"
        else:
            ed = f"ann{self.nation.id[2:]}{int(self.nation.nationalannouncement_set.order_by('-id')[0].id[-1]) + 1}"
        new = NationalAnnouncement(
            id=ed,
            text=text,
            nation=self.nation
        )
        new.save()

    def delete_announcement(self, id):
        self.nation.nationalannouncement_set.get(pk=id).delete()

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

    def get_adults(self):
        return global_get_adults(self)

    def get_adults_count(self):
        return global_get_adults_count(self)

    def get_youth(self):
        return global_get_youth(self)

    def get_youth_count(self):
        return global_get_youth_count(self)

    def get_children(self):
        return global_get_children(self)

    def get_children_count(self):
        return global_get_children_count(self)


class AreaAdmin(models.Model):
    id = models.TextField(primary_key=True)
    phone = models.TextField()
    email = models.TextField()
    password = models.TextField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def add_announcement(self, text):
        if self.area.areaannouncement_set.count() == 0:
            ed = f"ann{self.area.id[2:]}1"
        else:
            ed = f"ann{self.area.id[2:]}{int(self.area.areaannouncement_set.order_by('-id')[0].id[-1]) + 1}"
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

    def get_adults(self):
        return global_get_adults(self)

    def get_adults_count(self):
        return global_get_adults_count(self)

    def get_youth(self):
        return global_get_youth(self)

    def get_youth_count(self):
        return global_get_youth_count(self)

    def get_children(self):
        return global_get_children(self)

    def get_children_count(self):
        return global_get_children_count(self)


class DistrictAdmin(models.Model):
    id = models.TextField(primary_key=True)
    phone = models.TextField()
    email = models.TextField()
    password = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def add_announcement(self, text):
        if self.district.districtannouncement_set.count() == 0:
            ed = f"ann{self.district.id[2:]}1"
        else:
            ed = f"ann{self.district.id[2:]}{int(self.district.districtannouncement_set.order_by('-id')[0].id[-1]) + 1}"
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

    def get_announcements(self):
        return self.localannouncement_set.all()

    def get_adults(self):
        return global_get_adults(self)

    def get_adults_count(self):
        return global_get_adults_count(self)

    def get_youth(self):
        return global_get_youth(self)

    def get_youth_count(self):
        return global_get_youth_count(self)

    def get_children(self):
        return global_get_children(self)

    def get_children_count(self):
        return global_get_children_count(self)


class LocalAdmin(models.Model):
    id = models.TextField(primary_key=True)
    phone = models.TextField()
    email = models.TextField()
    password = models.TextField()
    local_assembly = models.ForeignKey(LocalAssembly, on_delete=models.CASCADE)

    def add_announcement(self, text):

        if self.local_assembly.localannouncement_set.count() == 0:
            ed = f"ann{self.local_assembly.id[2:]}1"

        else:
            ed = f"ann{self.local_assembly.id[2:]}{int(self.local_assembly.localannouncement_set.order_by('-id')[0].id[-1]) + 1}"

        new = LocalAnnouncement(
            id=ed,
            text=text,
            local=self.local_assembly,
        )
        new.save()

    def delete_announcement(self, id):
        self.local_assembly.localannouncement_set.get(pk=id).delete()

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

    def get_age(self):
        age = today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age


class Author(models.Model):
    id = models.TextField(primary_key=True)
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)
    name = models.TextField()
    phone = models.TextField()
    password = models.TextField(default=phone)

    def add_article(self, img, head, body, brief):
        art_id = generate_article_id()
        print(art_id)
        new_article = Article(
            img=img, head=head, body=body, brief=brief, id=art_id, date_created=datetime.now()
        )
        new_article.save()


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


class Article(models.Model):
    img = models.ImageField(upload_to='article_imgs')
    id = models.CharField(primary_key=True, auto_created=False, max_length=100)
    head = models.CharField(max_length=500)
    brief = models.CharField(max_length=500, default="")
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
