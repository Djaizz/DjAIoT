from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import site

from silk.profiling.profiler import silk_profile

from .models import (
    SKLModel,
    KerasModel, TFModel, TorchModel
)


@register(SKLModel, site=site)
class SKLModelAdmin(ModelAdmin):
    show_full_result_count = False

    @silk_profile(name=f'{__module__}: {SKLModel._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(name=f'{__module__}: {SKLModel._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(KerasModel, site=site)
class KerasModelAdmin(ModelAdmin):
    show_full_result_count = False

    @silk_profile(name=f'{__module__}: {KerasModel._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(
        name=f'{__module__}: {KerasModel._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(TFModel, site=site)
class TFModelAdmin(ModelAdmin):
    show_full_result_count = False

    @silk_profile(name=f'{__module__}: {TFModel._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(
        name=f'{__module__}: {TFModel._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(TorchModel, site=site)
class TorchModelAdmin(ModelAdmin):
    show_full_result_count = False

    @silk_profile(
        name=f'{__module__}: {TorchModel._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    @silk_profile(
        name=f'{__module__}: {TorchModel._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)
