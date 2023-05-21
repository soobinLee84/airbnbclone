from django.contrib import admin
from .models import Reiview


@admin.register(Reiview)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = ("rating",)
