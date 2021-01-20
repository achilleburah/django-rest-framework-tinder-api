from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import CustomUser, MatchedUser, MatchRequest
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class CustomUserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'genre', 'bio', 'password', 'picture', 'location', 'is_admin', 'is_staff']


    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = '__all__'

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'first_name', 'last_name', 'genre', 'bio', 'picture', 'location', 'is_admin', 'is_staff')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ( 'first_name', 'last_name', 'genre', 'bio', 'picture', 'location',)}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', )}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'genre', 'bio', 'password', 'picture', 'location', 'is_admin', 'is_staff')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


    def get_matches(self, obj):
        return " - ".join([p.first_name for p in obj.matches.all()])


class RequestAdmin(admin.ModelAdmin):
  fields = ['sender', 'receiver']
  list_display = ('sender', 'receiver')



admin.site.register(CustomUser, UserAdmin)
admin.site.register(MatchRequest, RequestAdmin)

admin.site.unregister(Group)
