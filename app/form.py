from django import forms
from .models import Host

class HostForm(forms.ModelForm):

    class Meta:
        model = Host
	fields = ('ip', 'name', 'application', 'remark')
        widgets = {
          'ip': forms.TextInput(attrs={'class': 'form-control'}),
          'name': forms.TextInput(attrs={'class': 'form-control'}),
          'application': forms.TextInput(attrs={'class': 'form-control'}),
          'remark': forms.TextInput(attrs={'class': 'form-control'}),
        }
