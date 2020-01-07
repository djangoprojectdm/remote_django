from django import forms


class registrationform(forms.Form):
    firstname = forms.CharField(
        label="enter your first name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your first name'

            }
        )
    )
    lastname = forms.CharField(
        label="enter your last name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your last name'

            }
        )
    )
    username = forms.CharField(
        label="enter your username",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your username'

            }
        )
    )
    password = forms.CharField(
        label="enter your password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your password'

            }
        )
    )
    mobile = forms.CharField(
        label="enter your mobile number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your mobile number'

            }
        )
    )
    email = forms.EmailField(
        label="enter your email",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your email'

            }
        )
    )

    gender = forms.CharField(
        label="enter your gender",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your gender'

            }
        )
    )
    date_of_birth=forms.DateField(
        label="enter your dob",
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your DOB'

            }
        )
    )


class loginform(forms.Form):
    username = forms.CharField(
        label="enter your user name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your user name'

            }
        )
    )
    password = forms.CharField(
        label="enter your password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your password'

            }
        )
    )
