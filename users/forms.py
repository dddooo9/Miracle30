from django import forms
from allauth.account.forms import SignupForm

class MyCustomSignupForm(SignupForm):
    nickname = forms.CharField(max_length=10, label='닉네임', widget=forms.TextInput(attrs={'placeholder': '닉네임'}))

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.profile.nickname = self.cleaned_data['nickname']
        user.save()
        return user
