from django import forms

from .models import Group


class GroupBaseForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'name',
            'start_date',
            'end_date',
        ]

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }


class GroupCreateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        pass


class GroupUpdateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        exclude = [
            'start_date',
        ]
