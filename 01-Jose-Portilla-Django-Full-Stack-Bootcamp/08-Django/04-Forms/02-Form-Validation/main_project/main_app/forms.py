from django import forms
from django.core import validators


# Custom Single Field Validate Method
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError('NAME NEEDS TO BE START WITH Z')


class BasicForm(forms.Form):
    # name = forms.CharField(validators=[check_for_z])

    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)

    # Validate Entire Form once
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")

    # Catch Bots with Built In Validation
    # botcatcher = forms.CharField(required=False,
    #                               widget=forms.HiddenInput,
    #                               validators=[validators.MaxLengthValidator(0)])
    #
    #
    # Catch Bots with Custom Single Field Clean method
    # botcatcher = forms.CharField(required=False,
    #                               widget=forms.HiddenInput)
    #
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT...")
    #     return botcatcher


