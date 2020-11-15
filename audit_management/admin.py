from django.contrib import admin
from .models import Expense
# Register your models here.
admin.site.register(Expense)



from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    #model = User

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email',  'active', 'staff', 'admin', 'branch',
    'branch_code', 'region', 'division',)
    list_filter = ('admin','staff', 'active', 'branch_code', 'region', 'division',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Branch info', {'fields': ('branch', 'branch_code', 'region', 'division')}),
        ('Permissions', {'fields': ('admin','staff', 'active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email','branch', 'branch_code', 'region', 'division',)
    ordering = ('email','branch', 'branch_code', 'region', 'division',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)



# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
