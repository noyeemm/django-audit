from django import forms
from .models import Expense, FileUpload
from bootstrap_datepicker_plus import DatePickerInput, YearPickerInput, DateTimePickerInput, TimePickerInput
from django.utils import formats
# from multiupload.fields import MultiFileField
from django.utils.translation import gettext as _


class ExpenseForm(forms.ModelForm):


    # first = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)
    class Meta:
        model = Expense
        #localized_fields = ('audit_period_start',)
        #fields = '__all__'

        fields = ( 'fiscal_year', 'audit_year', 'audit_period_start','audit_period_end', 'para_no', 'para_type', 'present_objection_status', 'finished_date', 'finished_letter_no', 'audit_Objection_Title', 'amount',
                 'amount_in_word', 'cause_of_objection', 'description_of_objetion', 'recommendation', 'action', 'issued_letter_no','issued_letter_date',
                  'last_reply_no','last_reply_date',  'comments',) #'FileUpload.file_description', 'FileUpload.ocument', ) #//'auditor_comment',
        labels = {
            'audit_period_start': _('নিরীক্ষা শুরুর তারিখ:'),
         }
        labels = {
                    'fiscal_year': _('অর্থ বছর'),
                    'audit_year': _('নিরীক্ষা বছর'),
                    'audit_period_start': _('নিরীক্ষা শুরুর তারিখ'),
                    'audit_period_end': _('নিরীক্ষা সমাপ্তির তারিখ:'),
                    'para_no': _('অনুচ্ছেদ নং:'),
                    'para_type': _('অনুচ্ছেদের ধরণ:'),
                    'present_objection_status': _('আপত্তির বর্তমান অবস্থা:'),
                    'finished_date': _('নিষ্পন্নের তারিখ:'),
                    'finished_letter_no': _('নিষ্পন্নের জারি পত্র নং:'),
                    'audit_Objection_Title': _('আপত্তির শিরোনাম:'),
                    'amount': _('জড়িত টাকার পরিমান (অংকে)'),
                    'amount_in_word': _('কথায়:'),
                    'cause_of_objection': _('আপত্তির কারণ:'),
                    'description_of_objetion': _('আপত্তির বিবরণ:'),
                    'recommendation': _('নিরীক্ষার সুপারিশ:'),
                    'action': _('শাখা / কার্যালয়ের জবাব / গৃহীত ব্যবস্থাদি:'),
                    'issued_letter_no': _('জারি পত্র নং:'),
                    'issued_letter_date': _('জারি পত্রের তারিখ:'),
                    'last_reply_no': _('সর্বশেষ জবাব প্রেরণের নম্বর:'),
                    'last_reply_date': _('সর্বশেষ জবাব প্রেরণের তারিখ'),

                    'formset.file_description': _('সংযুক্ত ডকুমেন্টের বর্ণনা'),
                    'formset.document': _('প্রয়োজনীয় ডকুমেন্ট সংযুক্তি'),
                    'comments': _('মন্তব্য:'),



                }
        help_texts = {
                    'fiscal_year': _('উদাহরণঃ ২০১১-১২'),
                }


        widgets = {
            #'audit_period_start': DatePickerInput(options={"format": "YYYY-6-30", "locale":"bn", }),
            'audit_period_start': DatePickerInput(format='%Y-%m-%d'),
            #default date-format %m/%d/%Y will be used
            'audit_period_end': DatePickerInput(format='%Y-%m-%d'),
            'issued_letter_date': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
            'last_reply_date': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
            # 'audit_period_end': DatePickerInput(options={"format": 'YYYY-6-30', "locale":"bn", }),
            # 'issued_letter_date': DatePickerInput(options={"format": "YYYY-mm-dd", "locale":"bn", }), # specify date-frmat
            #'last_reply_date': DatePickerInput(options={'format': '%Y-%m-%d', 'locale':'bn', }), # specify date-frmat
        }


# accounts.forms.py

from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

from .models import User
from django.contrib.auth.models import User

User = get_user_model()



class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'branch', 'branch_code', 'region', 'division')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin',  'staff', 'branch',
        'branch_code', 'region', 'division')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class LoginForm(forms.Form):
        username = forms.EmailField(label='Email')
        password = forms.CharField(widget=forms.PasswordInput)
