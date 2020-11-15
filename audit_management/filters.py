from django import forms
import django_filters
from .models import*
from django.utils.translation import gettext as _

class ExpenseFilter(django_filters.FilterSet):
    class Meta:
        model = Expense
        fields = ('audit_Objection_Title', 'fiscal_year',)
        labels = {
                    'audit_Objection_Title': _('আপত্তির শিরোনাম:'),
                    'fiscal_year': _('অর্থ বছর'),
                    }
