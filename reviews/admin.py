from django.contrib import admin
from .models import Reiview


class WorldFilter(admin.SimpleListFilter):
    title = "Filter by words!"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("bad", "Bad"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word == "good":
            return reviews.filter(rating__gte=3)
        elif word == "bad":
            return reviews.filter(rating__lt=3)
        else:
            return reviews


@admin.register(Reiview)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        WorldFilter,
        "rating",
        "user__is_host",
        "room__category",
    )
