from django import newforms as forms

class LoginForm(forms.Form):
	which_form = forms.CharField(widget=forms.HiddenInput, initial="login")
	login_email = forms.EmailField(label="Email")
	login_password = forms.CharField(widget=forms.PasswordInput, label="Password", error_messages={'required': 'Please enter your password'})

class SignUpForm(forms.Form):
	which_form = forms.CharField(widget=forms.HiddenInput, initial="signup")
	signup_email = forms.EmailField(label="Email")
	signup_first_name = forms.CharField(label="First Name")
	signup_last_name = forms.CharField(label="Last Name")
	signup_password = forms.CharField(widget=forms.PasswordInput,label="Password")
	signup_password_confirm = forms.CharField(widget=forms.PasswordInput,label="Verify Password")