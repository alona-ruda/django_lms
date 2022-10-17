from django import forms
from django_filters import FilterSet

from .models import Student


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            # '__all__',
            'first_name',
            'last_name',
            'birthday',
            'email',
            'phone',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    def clean(self):
        pass

    def clean_birthday(self):
        value = self.cleaned_data.get('birthday')

        return value

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name').title()

        return value

    def clean_last_name(self):
        value = self.cleaned_data.get('last_name').title()

        return value

    def clean_phone(self):
        number = self.cleaned_data.get('phone')
        correct_symbols = '+-()0123456789'
        value = ''
        for i in number:
            if i in correct_symbols:
                value += i

        return value



class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            # '__all__',
            'first_name',
            'last_name',
            'birthday',
            'phone',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }


class StudentFilterForm(FilterSet):
    class Meta:
        model = Student
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith']
        }