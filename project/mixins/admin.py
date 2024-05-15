from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    base_readonly_fields = ("created", "creator", "edited", "editor")

    def get_readonly_fields(self, request, obj=None):
        if self.readonly_fields:
            return self.readonly_fields + self.base_readonly_fields
        else:
            return self.base_readonly_fields

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.creator = request.user
        obj.editor = request.user
        super().save_model(request, obj, form, change)
