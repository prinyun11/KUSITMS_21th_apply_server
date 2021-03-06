from django.contrib.admin.decorators import register
from django.contrib.admin import ModelAdmin
from apps.apply.models import ApplyForm, SNSImage


@register(ApplyForm)
class ApplyFormAdmin(ModelAdmin):
    autocomplete_fields = ['user']


@register(SNSImage)
class SNSImageAdmin(ModelAdmin):
    pass
