from django.contrib import admin

from tree_menu_app.models import TreeMenu, MenuItem


@admin.register(TreeMenu)
class TreeMenuAdmin(admin.ModelAdmin):
    pass


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    pass
