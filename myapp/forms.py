from django import forms
from .models import Login,Home,Registration
import random
class formz(forms.ModelForm):
    username = forms.CharField(max_length=150)
    # phone = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'container'}))
    class Meta:
        model = Login
        fields = ['username','password']

class formz2(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # phon=forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'container'}))
    # address=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'container'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'container'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'container'}))

    class Meta:
        model = Registration
        fields = ['name','email','password','confirm_password']
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")
class formz3(forms.ModelForm):
    si_number=forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    count = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    member_id = forms.IntegerField(initial=lambda: random.randint(1000, 9999),
                                       widget=forms.NumberInput(attrs={'class': 'container'}))
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    left_customer = forms.IntegerField(initial=lambda: random.randint(0, 20),
                                       widget=forms.NumberInput(attrs={'class': 'container'}))
    right_customer = forms.IntegerField(initial=lambda: random.randint(0, 20),
                                        widget=forms.NumberInput(attrs={'class': 'container'}))
    amount = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'container'}), required=False)
    # customer=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    rebirth = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'container'}))
    # position_counter=forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'container'}))

    class Meta:
        model = Home
        # fields = '__all__'
        fields = ['si_number','count','member_id','username', 'left_customer', 'right_customer', 'amount', 'rebirth']