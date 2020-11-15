from django import forms
from .models import Upkoron

from django.utils import formats
# from multiupload.fields import MultiFileField
from django.utils.translation import gettext as _


class UpkoronForm(forms.ModelForm):


    # first = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)
    class Meta:
        model = Upkoron
        #localized_fields = ('audit_period_start',)
        #fields = '__all__'

        fields = ( 'serviece_name', 'serviece_receiver',
    'current_serviece_delivery_method',
    'current_serviece_delivery_problems',
    'affected_people',
    'innovative_idea_title',
    'solution_process',
    'solution_process_map',
    'nobelness_in_idea',
    'equipments',
    'background_works_required',
    'tcv',
    'others_advantage',
    'resource_map',
    'implementation_team',

    'targeted_people_to_receive_advantage',
    'pilotting_activities',
    'risk_feared',
    'details_of_the_owner',)



        labels = {

    'serviece_name' :  _('১। ক.চিহ্নিত সেবার নাম	: (এখানে আইডিয়াটির শিরোনাম হবে না। অফিসের যে সেবা বা সেবাসমূহকে কেন্দ্র করে আইডিয়াটি নেয়া হয়েছে, তার নাম হবে):'),
    'serviece_receiver':   _('১। খ. সেবা গ্রহণকারী কারা?:'),
    'current_serviece_delivery_method':   _('২।ক. সেবাটি বর্তমানে কিভাবে দেয়া হয়? ( বিবরণ: বুলেট পয়েন্ট আকারে লেখা যেতে পারে/ অথবা প্রসেস ম্যাপ আকারে দেয়া যেতে পারে)'),
    'current_serviece_delivery_problems':   _('২। 	খ. চিহ্নিত সেবা প্রদান করার ক্ষেত্রে/প্রাপ্তির ক্ষেত্রে বিদ্যমান সমস্যা ও কারণ সম্পর্কে বিবৃতি (Where,  who, how much, what and why?)	:'),
    'affected_people':   _('৩। 	সমস্যার ভুক্তভোগী কারা?:'),
    'innovative_idea_title':   _('৪) 	সমস্যা সমাধানে প্রদত্ত আইডিয়াটির শিরোনামঃ:'),
    'solution_process':   _('৫। সমাধান প্রক্রিয়া ক.আইডিয়ার বিবরণ  (আবেদন পূর্ব হতে সেবা দেয়ার পর  পর্যন্ত যা যা করা হবে, তার বিস্তারিত বিবরণ প্যারাগ্রাফ আকারে লিখতে হবে।)'),
    'solution_process_map':   _('৫।(খ) নতুন প্রসেস ম্যাপঃ কাস্টমারের নিকট একটি সেবা যেভাবে পৌঁছে দেয়া হবে, তা বুলেট পয়েন্ট আকারে ধারাবাহিক ভাবে লিখতে হবে।)'),
    'nobelness_in_idea':   _('৫। গ.উদ্যোগটির মধ্যে নতুনত্ব কি (যা বিদ্যমান আইন / সার্কুলার / নীতিমালায় বলা হয়নি?)?'),
    'equipments':   _('৫। ঘ) উদ্যোগটি বাস্তবায়ন করার জন্য নতুন কী কী হার্ডওয়্যার / সরঞ্জামাদি / অবকাঠামো লাগবে?'),
    'background_works_required':   _('৫। ঙ) উদ্যোগটি বাস্তবায়ন করার জন্য নতুন কী কী ব্যাকগ্রাউন্ড ওয়ার্ক করতে হবে? (সফটওয়্যার তৈরী, ডাটাবেইজ তৈরী,এসএমএস বান্ডিল ক্রয় ইত্যাদি)। '),
    'tcv':   _('৬) 	প্রত্যাশিত ফলাফল(TCV) '),
    'others_advantage':   _('অন্যান্য সুবিধা (অনেক উদ্যোগ এর সুফল টিসিভি দিয়ে বুঝানো যাবে না অথবা টিসিভিতে পরিবর্তন ছাড়াও অন্যান্য দৃশ্যমান সুবিধা থাকতে পারে। এসব কিছুর বিবরণ এখানে লিখতে হবে।)'),
    'resource_map':   _('৭) রিসোর্স ম্যাপঃ'),
    'implementation_team':   _('৮)	বাস্তবায়নকারী টিমঃ (উদ্যোগটির পাইলট বাস্তবায়ন করার জন্য প্রতিটি অফিসে যে টিম গঠন করা প্রয়োজন):'),

    'targeted_people_to_receive_advantage':   _('৯)  সুবিধাভোগীর ধরণ ও  সংখ্যা (পাইলটিং এলাকা): '),
    'pilotting_activities':   _('১০। আইডিয়া পাইলট করার জন্য প্রয়োজনীয় কার্যক্রম:'),
    'risk_feared':   _('১১) ঝুঁকি:'),
    'details_of_the_owner':   _('১২. আইডিয়া প্রদানকারীর বিস্তারিত:'),

                }
        # help_texts = {
        #             'fiscal_year': _('উদাহরণঃ ২০১১-১২'),
        #         }





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
