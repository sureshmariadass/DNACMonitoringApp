from django.db import models


# Create your models here.

from django.core.exceptions import ValidationError, ImproperlyConfigured
from django.core.validators import MaxValueValidator, validate_comma_separated_integer_list
from django.utils.timezone import now
from django.conf import settings
from django.utils.translation import ugettext as _
from model_utils.managers import InheritanceManager
from django.utils import timezone

class DeviceDetails(models.Model):

    device_name = models.CharField(verbose_name=_("Device Name"),max_length=250, blank=True,null =True)
    management_ip = models.CharField(verbose_name=_("Management ip"),max_length=250, blank=True, null=True)
    device_family = models.CharField(verbose_name=_("Device Family"),max_length=350, blank=True,null=True)
    software_version = models.CharField(verbose_name=_("Software Version"),max_length=350, blank=True,null=True)
    communication_state = models.CharField(verbose_name=_("Communication State"),max_length=350, blank=True,null=True)
    collection_status = models.CharField(verbose_name=_("Collection Status"),max_length=350, blank=True,null=True)
    seriel_no= models.CharField(verbose_name=_("Seriel No"),max_length=350, blank=True,null=True)
    overall_helth = models.CharField(verbose_name=_("Overall Health"),max_length=350, blank=True,null=True) 
    cpu_score = models.IntegerField(verbose_name=_("CPU Score"),max_length=350, blank=True,null=True)
    cpu=models.FloatField(verbose_name=_("CPU"),max_length=350, blank=True,null=True)   
    memory_score=models.IntegerField(verbose_name=_("Memory Score"),max_length=350, blank=True,null=True)
    memory=models.FloatField(verbose_name=_("memory"),max_length=350, blank=True,null=True)

    start_date=models.DateTimeField(default=timezone.now,null=True, blank=True,verbose_name=("Start Date"))

