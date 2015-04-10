from django.contrib import admin
from snet.models import User_Bio, Wall, User, Post

class WallInline(admin.TabularInline):
    model = Wall
    extra = 1

class PostInline(admin.TabularInline):
	model = Post

class UserBioInline(admin.TabularInline):
    model = User_Bio

class UserAdmin(admin.ModelAdmin):
    inlines = [UserBioInline]


#    list_filter = ['age']

class UserBioAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Age', {'fields': ['age']}),
        ('Date Joined', {'fields':['date_join']})
    ]
    inlines = [PostInline]
    list_filter = ['age']


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(User_Bio, UserBioAdmin)
