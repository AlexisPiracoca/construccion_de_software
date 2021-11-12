from django.contrib import admin
from characters.models import Character, Universe

# Register your models here.
@admin.register(Character)

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','date_of_birth')
    list_display_links = ('id','name')

@admin.register(Universe)

class UniverseAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','foundation')
    list_display_links = ('id','name')
