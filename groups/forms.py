from django import forms

from .models import Group


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            # '__all__'
            'name_of_group',
            'start_date',
            'group_description',
        ]


class UpdateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'name_of_group',
            'start_date',
            'group_description',
        ]
