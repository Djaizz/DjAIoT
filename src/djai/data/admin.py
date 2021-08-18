from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import site

from .models import (
    DataSchema,
    NamedJSONDataSet, NamedNumPyArray, NamedPandasDataFrame,
    NamedCSVDataSet, NamedParquetDataSet, NamedTFRecordDataSet
)


@register(DataSchema, site=site)
class DataSchemaAdmin(ModelAdmin):
    show_full_result_count = False

    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(NamedJSONDataSet, site=site)
class NamedJSONDataSetAdmin(ModelAdmin):
    show_full_result_count = False

    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(NamedNumPyArray, site=site)
class NamedNumPyArrayAdmin(ModelAdmin):
    show_full_result_count = False

    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(NamedPandasDataFrame, site=site)
class NamedPandasDataFrameAdmin(ModelAdmin):
    show_full_result_count = False

    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(NamedCSVDataSet, site=site)
class NamedCSVDataSetAdmin(ModelAdmin):
    show_full_result_count = False

    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(NamedParquetDataSet, site=site)
class NamedParquetDataSetAdmin(ModelAdmin):
    show_full_result_count = False

    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)


@register(NamedTFRecordDataSet, site=site)
class NamedTFRecordDataSetAdmin(ModelAdmin):
    show_full_result_count = False

    def changeform_view(self, *args, **kwargs):
        return super().changeform_view(*args, **kwargs)

    def changelist_view(self, *args, **kwargs):
        return super().changelist_view(*args, **kwargs)
