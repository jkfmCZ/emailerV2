from django import forms
from .models import Emails, Contacts, Message

class EmailsForm(forms.ModelForm):
    class Meta:
        model = Emails
        fields = ['email', 'token', 'host', 'port']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'border p-2 w-full'}),
            'token': forms.TextInput(attrs={'class': 'border p-2 w-full'}),
            'host': forms.TextInput(attrs={'class': 'border p-2 w-full'}),
            'port': forms.NumberInput(attrs={'class': 'border p-2 w-full'}),
        }


class ContactsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # vyndáme user z kwargs
        super().__init__(*args, **kwargs)  # zavoláme rodičovský konstruktor

        if user:
            # omezíme queryset pro message, aby uživatel viděl jen svoje zprávy
            self.fields['message'].queryset = Message.objects.filter(user=user)

    class Meta:
            model = Contacts
            fields  = ["name", "company", "email", "contacted", "message"]
            widgets = {
                'name': forms.TextInput(attrs={
                'placeholder': 'address subject(Mr. Jelínek)',
                'class': 'border rounded px-2 py-1'
            }),
                'company': forms.TextInput(attrs={
                'placeholder': 'enter a company name',
                'class': 'border rounded px-2 py-1'
            }),
                'email':  forms.EmailInput(attrs={
                'placeholder': 'enter email adress (email@domena.cz)',
                'class': 'border rounded px-2 py-1'
            }),
                'contacted': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
                'message': forms.Select(attrs={
                    'class': 'border rounded px-2 py-1'
            }),
            }

class MessageForm(forms.ModelForm):
     class Meta:
          model = Message
          fields = ["message", "name", "subject"]
          widgets = {
                'name': forms.TextInput(attrs={
                'placeholder': 'enter a message´s name (for it guy)',
                'class': 'border rounded px-2 py-1'
            }),
                'message': forms.Textarea(attrs={
                'placeholder': 'enter a message you want to send (Dear SUBJECT, We are happy to invite you and your company COMPANY to our event...).',
                'class': 'border rounded px-2 py-1 h-32 lg:h-32'
            }),
                'subject': forms.TextInput(attrs={
                'placeholder': 'enter a message you want to send.',
                'class': 'border rounded px-2 py-1'
            }),
          }