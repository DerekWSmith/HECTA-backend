from django.contrib import admin

from .models import GameResult


class GameResultAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "person_name",
        "person_gender",
    ]


admin.site.register(GameResult, GameResultAdmin)
