from django import forms
from .models import Login,Home
class login_form(forms.ModelForm):
    user_name = forms.CharField(max_length=150)
    # ph = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'container'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'container'}))
    class Meta:
        model = Login
        fields = ['user_name','password']

class home_form(forms.ModelForm):
    mobile_number = forms.CharField(max_length=15)
    member_id = forms.CharField(max_length=50)
    left_customer = forms.IntegerField(initial=0)
    right_customer = forms.IntegerField(initial=0)
    amount = forms.FloatField(initial=0)
    rebirth = forms.BooleanField(initial=False)
    income = forms.FloatField(initial=0)
    count = forms.IntegerField()
    si_no = forms.IntegerField()
    # formatted_date = forms.DateInput(attrs={'type': 'date'})
    formatted_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        # model = CustomUser
        model = Home
        fields = ['mobile_number', 'member_id','left_customer','right_customer','amount','rebirth','income','count','si_no','formatted_date']
