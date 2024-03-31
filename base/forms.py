from typing import Any
from django.forms import ModelForm,TextInput,EmailInput
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(ModelForm):
    class Meta:
        model=User
        fields=['email','password']
class RegistrationForm(UserCreationForm):
    email=forms.EmailField(max_length=100,required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2= forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('email','username',)
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("email must be in @gmail.com domain")
        return email
    def clean(self) :
        cleaned_data=super().clean()
        password1=cleaned_data.get('password1')
        password2=cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("The two passwords don't match")
"""
By default, UserCreationForm includes the following fields from the User model:

username
password1
password2

The email field, although it's part of the User model, isn't included in the default UserCreationForm. If you want to include the email field in the registration form, you need to explicitly specify it in the fields attribute of the Meta class.

Therefore, in the UserForm, only the email and password fields from the User model will be included in the form. Similarly, in the RegistrationForm, the email and username fields from the User model will be included along with the custom email field that you've defined explicitly in the form class.

In both forms, the fields attribute in the Meta class specifies which fields from the associated model (User model in this case) should be included in the form.

Therefore, in the UserForm, only the email and password fields from the User model will be included in the form. Similarly, in the RegistrationForm, the email and username fields from the User model will be included along with the custom email field that you've defined explicitly in the form class.

So, th
In Django, form validation can be specified within the form itself. When you create a Django form, you have the option to define custom validation logic for individual fields or for the form as a whole.

Here's how validation can be specified in Django forms:

Field-specific validation:
You can define validation logic specific to each field in your form by overriding the clean_<fieldname>() method for that field. For example, if you want to validate the email field, you can define a method named clean_email() in your form class.

python
Copy code
class MyForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Your validation logic here
        if not email.endswith('@example.com'):
            raise forms.ValidationError("Email must be from example.com domain.")
        return email
Form-level validation:
You can also define validation logic that involves multiple fields or the form as a whole by overriding the clean() method in your form class.

python
Copy code
class MyForm(forms.Form):
    password = forms.CharField()
    confirm_password = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
In this example, the clean() method checks if the passwords match and raises a ValidationError if they don't.

ModelForm validation:
If you're using a ModelForm to create or update model instances, Django also performs model-specific validation automatically. This includes checking for field constraints specified in the model's models.py file, such as max_length, unique, etc.

When the form is submitted, Django automatically calls the appropriate validation methods. If any validation errors occur, they are stored in the form's errors attribute, and the form is considered invalid. Django provides built-in error handling mechanisms to display these errors in templates.

By defining validation logic within your forms, you can ensure that user input meets your application's requirements before processing it further or saving it to the database.



User
how do i print the errors in the views.py once raised in the forms.py

ChatGPT
In Django, when form validation fails and errors are raised in the forms.py file, you can access these errors in your views.py file and handle them accordingly. Here's how you can do it:

Assuming you have a form defined in forms.py:

python
Copy code
# forms.py
from django import forms

class MyForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise forms.ValidationError("Email must be from example.com domain.")
        return email
Now, in your views.py file, where you handle the form submission:

python
Copy code
# views.py
from django.shortcuts import render
from .forms import MyForm

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the valid form data
            email = form.cleaned_data['email']
            # Do something with the email
        else:
            # Form is invalid, handle errors
            errors = form.errors
            # You can now use 'errors' dictionary to access validation errors
            # and render them in your template, or handle them in any other way you prefer
            return render(request, 'my_template.html', {'form': form, 'errors': errors})
    else:
        form = MyForm()
    
    return render(request, 'my_template.html', {'form': form})
In the above example, if the form validation fails (i.e., if the email doesn't end with '@example.com' in this case), a ValidationError will be raised in the clean_email() method of the form.

In the view function my_view, when the form is not valid (form.is_valid() returns False), you can access the validation errors using form.errors. You can then pass these errors to your template context and render them to the user to show what went wrong with the submitted form data.

In your template (my_template.html), you can iterate over the errors dictionary and display the errors for each field. For example:

html
Copy code
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>

{% if errors %}
    <ul>
    {% for field, error_list in errors.items %}
        <li>{{ field }}: {{ error_list }}</li>
    {% endfor %}
    </ul>
{% endif %}
This will display the validation errors for each field in your form. Make sure to replace 'my_template.html' with the actual path to your template file.


widget=forms.PasswordInput: This part specifies the widget that should be used to render the field in the HTML form. In this case, PasswordInput is a widget provided by Django that renders an HTML input element with the type set to "password". This means that characters entered into this field will be masked to prevent them from being displayed as plain text.











"""