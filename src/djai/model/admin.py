from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import site

from .models import (
    SKLModel,
    KerasModel, TFModel, TorchModel
)


@register(SKLModel, site=site)
class SKLModelAdmin(ModelAdmin):
    show_full_result_count = False

    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(KerasModel, site=site)
class KerasModelAdmin(ModelAdmin):
    show_full_result_count = False

    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(TFModel, site=site)
class TFModelAdmin(ModelAdmin):
    show_full_result_count = False

    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(TorchModel, site=site)
class TorchModelAdmin(ModelAdmin):
    show_full_result_count = False

    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)
