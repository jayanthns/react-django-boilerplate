from django.contrib import admin
from django import forms

from accounts.models import Account


# Register your models here.
from django.contrib.auth.hashers import make_password


class AccountForm(forms.ModelForm):
    password = forms.CharField()

    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'firstname', 'lastname', 'is_staff']

    def save(self, commit=True):
        # do something with self.cleaned_data['temp_id']
        account = super(AccountForm, self).save(commit=commit)
        account.set_password(self.cleaned_data['password'])
        account.save()
        return account

class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'firstname', 'lastname', 'is_staff')
    # fields = ('username', 'email', 'password', 'firstname', 'lastname', 'is_staff')
    form = AccountForm

admin.site.register(Account, AccountAdmin)
