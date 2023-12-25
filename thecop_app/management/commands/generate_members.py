from django.core.management.base import BaseCommand
from faker import Faker
from thecop_app.models import Member, LocalAssembly, LocalAdmin
from thecop_app.logic import generate_member_id

fake = Faker()

class Command(BaseCommand):
    help = 'Generate members'

    def handle(self, *args, **kwargs):
        first_names = [
            ""
        ]
        for _ in range(200):
            gender = fake.random_element(['Male', 'Female'])
            date_of_birth = fake.date_of_birth(minimum_age=5, maximum_age=90)
            phone = fake.phone_number()
            phone2 = fake.phone_number()
            email = fake.email()
            address = fake.address()

            # Assuming you have a LocalAssembly object, replace 'your_local_assembly_object' with the instance
            local_assembly = LocalAssembly.objects.get(pk='LO11111')

            member = Member.objects.create(
                id=generate_member_id(LocalAdmin.objects.get(pk='LA111111')),
                local_assembly=local_assembly,
                name=fake.name(),
                gender=gender,
                date_of_birth=date_of_birth,
                phone=phone,
                phone2=phone2,
                email=email,
                address=address,
                password=phone  # Default password set to phone number
            )

            self.stdout.write(self.style.SUCCESS(f'Successfully created member {member.id}'))

        self.stdout.write(self.style.SUCCESS('Successfully generated 200 members'))
