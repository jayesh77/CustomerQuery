from django.contrib import admin

# Register your models here.
from query.models import querydata,customerdata

admin.site.register(querydata)
admin.site.register(customerdata)