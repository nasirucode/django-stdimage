from django.contrib import admin

from . import models

admin.site.register(models.AdminDeleteModel)
admin.site.register(models.AdminUpdateModel)
admin.site.register(models.ResizeCropModel)
admin.site.register(models.ResizeModel)
admin.site.register(models.SimpleModel)
admin.site.register(models.ThumbnailModel)
admin.site.register(models.MaxSizeModel)
admin.site.register(models.MinSizeModel)
admin.site.register(models.ForceMinSizeModel)
