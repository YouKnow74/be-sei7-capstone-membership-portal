from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import ValidationError
from django.utils import timezone
from random import randint
from django.conf import settings


martial_Status = (
    ('Married','Married'),
    ('Single','Single'),
)

status = (
    (0,'Pending'),
    (1,'Active'),
    (2,'Hidden'),
)

# interests = (
#     ('1', 'Organization & Effectiveness'),
#     ('2', 'Projects & Construction'),
#     ('3', 'Banking & Finance'),
#     ('4', 'Hospitality, Leisure & Tourism'),
#     ('5', 'ICT'),
#     ('6', 'Legal'),
#     ('7', 'Women in Business'),
#     ('8', 'Young Professionals'), 
# )

class Interest(models.Model):
    interest = models.CharField(max_length=50)
    def __str__(self):
        return self.interest

features = (
    ("B", "Benefits"),
    ("E", "Events"),
    ("N", "Newsletters"),
)

status=(
    (0,'Pending'),
    (1,'Active'),
    (2,'Hidden'),
)
class Country(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=20)
    nationality_name = models.CharField(max_length=40)
    flag = models.CharField(max_length=200)
    capital = models.CharField(max_length=200)
    currency = models.CharField(max_length=100)
    currency_sign = models.CharField(max_length=20)
    country_code = models.CharField(max_length=5)
    listed = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Countries'
        ordering = ['name']
        
    # def get_country_nationality(self):
    #     return self.
class PlanFeature(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

# Yousif Added the model plan
class Plan(models.Model):
    name =models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    member_number = models.IntegerField()
    # features = models.CharField(max_length=1, choices=features, default=features[0][0])
    plan_feature = models.ManyToManyField(PlanFeature)

    status = models.BooleanField(default=True)
    # PlanFeature = models.ManyToManyField(PlanFeature)

    def __str__(self):
        return  f'{self.name}'

class Organization(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    logo = models.ImageField(upload_to='fs_business_mvt/static/uploads/', default="")
    cr_number = models.CharField(max_length=20, blank=False, null=False)
    phone_number = models.CharField(max_length=100, blank=False, null=False)
    email_address = models.EmailField(max_length=100, blank=False, null=False)
    sector = models.CharField(max_length=100, blank=False, null=False)
    website = models.CharField(max_length=100)
    address_one = models.CharField(max_length=100) #,blank=False, null=False
    address_two = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=False, null=False)
    country = models.ForeignKey(Country, on_delete = models.DO_NOTHING, blank=False, null=False,db_index=False,db_constraint=False, default=837)
    zip_code = models.IntegerField(blank=False, null=False)
    content_info = models.TextField(max_length=250, blank=False, null=False)
    # interests = models.CharField(max_length=1, choices=interests, default=interests[0][0])
    interests = models.ManyToManyField(Interest)
    status = models.IntegerField(choices=status,default=status[0][0])

    plan = models.ForeignKey(Plan, on_delete = models.DO_NOTHING, unique=False, default=1)
    # longname = models.CharField(max_length=100, blank=True, null=True)

    # assistant = models.ForeignKey(User , on_delete=models.DO_NOTHING)
    # admin = models.ForeignKey(User , on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'fs_business_mvt/static/uploads',default = "",blank=False,null=False)
    dob = models.DateField('Date of Birth')
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    phoneNumber = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 100)
    # phoneNumber = models.CharField(max_length= 30, default = "")
    # TO BE ADDED WHEN THE SALUTAION DATA IS AVAILABLE / comment by : Hussain
    # salutation = models.OneToOneField(Salutation,on_delete=models.CASCADE)
    martial = models.CharField(
        choices = martial_Status,
        default = ""
        )
    # nationality = models.CharField(choices = Country)
    nationality = models.ForeignKey(Country, on_delete = models.DO_NOTHING,default = 837)
    # , related_name="%(app_label)s_%(class)s_nationality_name",
    # related_query_name="%(app_label)s_%(class)ss_nationality_name" 
    # ,default = 837, related_name="nationality_namee"
    gender = models.CharField(choices = (('Male','Male'),('Female','Female')))
    organization = models.ForeignKey(Organization, on_delete = models.CASCADE)
    role = models.IntegerField(
        default=4,
        validators = [
            MaxValueValidator(4),
            MinValueValidator(1)
        ]
    )
    job_title = models.CharField(max_length = 100)
    status = models.IntegerField(
        choices = status,null=False,blank=False,
        default = status[0][0]
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    # @property
    # def nationality_value(self):
    #     print("Hello ",self.nationality.nationality_name)
    #     return self.nationality.nationality_name
    
    # def __str__(self):
    #     print("sssss", self.nationality.nationality_name)
    #     return str(self.nationality.nationality_name)
    
    
    
    # class Meta:
    #     permissions = (("change_org_name_"))
    

class Benefit(models.Model):
    organization = models.ForeignKey(Organization, on_delete = models.CASCADE)
    title = models.CharField(max_length = 250, null = False)
    description = models.CharField(max_length = 500, null = False)
    created_date = models.DateField(auto_now = True)
    expiry_date = models.DateField()
    # Register user to the benefit once they have used it
    used_by_user = models.ManyToManyField(Profile, related_name = 'used_benefit', blank = True)
    status = models.IntegerField(
        choices = status,
        default = status[0][0]
    )

    def __str__(self):
        return  f'{self.title} by {self.organization}'
    
    # Validating that the expiry date is always greater than (or equal?) to the current date
    # https://docs.djangoproject.com/en/4.2/ref/models/instances/#django.db.models.Model.clean
    def clean(self):
        if self.expiry_date < timezone.now().date():
            raise ValidationError({'expiry_date': 'Expiry date cannot be older than today.'})

    def assign_to_user(self, user):
        '''
        Call this function to add a user to the current benefit list once they redeem the benefit so they can't redeem it again.
        '''
        if user not in self.used_by_user.all():
            self.used_by_user.add(user)
            self.save()
        else:
            print('user already exist')
            raise ValidationError("Benefit has already been used by this user.")


class Event(models.Model):
    # Benefit().clean()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=100)
    sponsor = models.ForeignKey(Organization, on_delete = models.CASCADE, default=1)
    start_date = models.DateTimeField('Event Start Date')
    end_date = models.DateTimeField('Event End Date')
    attendees = models.ManyToManyField(Profile)

    def assign_to_user(self, user):
        '''
        Call this function to add a user to the current event list.
        '''
        if user not in self.attendees.all():
            self.attendees.add(user)
            self.save()
        else:
            raise ValidationError("User is already registered in this event.")

    def __str__(self):
        return self.title
    # def __str__(self):
    #     return f'{self.title}'

    # def clean(self):
    #     if self.start_date < datetime.datetime.now():
    #         raise ValidationError({'start_date': 'Start date can not be before today.'})
    #     elif self.end_date < self.start_date:
    #         raise ValidationError({'end_date': 'end date before the start date.'})

        

# class TestModel(models.Model):
#     name = models.CharField(max_length=200)

