# -*- coding: utf-8 -*-
"""
Admin for the omniforms app
"""
from __future__ import unicode_literals
from django.contrib import admin
from django.conf.urls import url
from django.contrib.contenttypes.admin import GenericTabularInline
from omniforms.admin_forms import OmniModelFormAdminForm
from omniforms.admin_views import OmniModelFormAddFieldView, OmniModelFormCreateFieldView, OmniModelFormPreviewView
from omniforms.admin_views import OmniModelFormAddHandlerView, OmniModelFormCreateHandlerView
from omniforms.models import OmniModelForm, OmniField, OmniFormHandler


class OmniFieldAdmin(GenericTabularInline):
    """
    Generic admin for OmniField models
    """
    model = OmniField
    extra = 0
    max_num = 0
    fields = ('name', 'order',)
    readonly_fields = ('name',)


class OmniHandlerAdmin(GenericTabularInline):
    """
    Generic admin for OmniFormHandler models
    """
    model = OmniFormHandler
    extra = 0
    max_num = 0
    fields = ('name', 'order',)
    readonly_fields = ('name',)


class OmniModelFormAdmin(admin.ModelAdmin):
    """
    Admin class for OmniModelForm model instances
    """
    inlines = [OmniFieldAdmin, OmniHandlerAdmin]
    form = OmniModelFormAdminForm

    def get_readonly_fields(self, request, obj=None):
        """
        Method for getting readonly fields for the admin class form
        Content Type can only be set at the point of creation so make it
        readonly if we're editing a persisted model instance

        :param request: Http Request instance
        :type request: django.http.HttpRequest

        :param obj: Model instance
        :type obj: omniforms.models.OmniModelForm

        :return: tuple of readonly field names
        """
        readonly_fields = super(OmniModelFormAdmin, self).get_readonly_fields(request, obj=obj)
        if obj and obj.pk:
            readonly_fields += ('content_type',)
        return readonly_fields

    def get_urls(self):
        """
        Method for getting urls for the admin class
        Adds extra urls for managing fields on the OmniModelForm instance

        :return: list of urls
        """
        return [
            url(
                r'^(.+)/preview/$',
                self.admin_site.admin_view(OmniModelFormPreviewView.as_view(admin_site=self)),
                name='omniforms_omnimodelform_preview'
            ),
            url(
                r'^(.+)/add-field/$',
                self.admin_site.admin_view(OmniModelFormAddFieldView.as_view(admin_site=self)),
                name='omniforms_omnimodelform_addfield'
            ),
            url(
                r'^(.+)/add-field/(.+)/$',
                self.admin_site.admin_view(OmniModelFormCreateFieldView.as_view(admin_site=self)),
                name='omniforms_omnimodelform_createfield'
            ),
            url(
                r'^(.+)/add-handler/$',
                self.admin_site.admin_view(OmniModelFormAddHandlerView.as_view(admin_site=self)),
                name='omniforms_omnimodelform_addhandler'
            ),
            url(
                r'^(.+)/add-handler/(.+)/$',
                self.admin_site.admin_view(OmniModelFormCreateHandlerView.as_view(admin_site=self)),
                name='omniforms_omnimodelform_createhandler'
            ),
        ] + super(OmniModelFormAdmin, self).get_urls()


admin.site.register(OmniModelForm, OmniModelFormAdmin)
