from django.contrib import admin
from .models import Movie, Gener

class MembershipInline(admin.TabularInline):
    model = Movie.gener.through


class GenreAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]
class MovieAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]
    exclude = ('gener',)


admin.site.register(Gener,GenreAdmin)
admin.site.register(Movie,MovieAdmin)

# Register your models here.
