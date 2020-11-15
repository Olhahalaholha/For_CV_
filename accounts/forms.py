from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation



class RegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
   

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password1", "password2"]


    def clean_username(self):
    	pass


    # def clean_password2(self):
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError(
    #             self.error_messages['пароли_не_совпадают'],
    #             code='пароли_не_совпадают',)
    #     return cleaned_data

    # def _post_clean(self):
    #     super()._post_clean()
    #     # Validate the password after self.instance is updated with form data
    #     # by super().
    #     password = self.cleaned_data.get('password2')
    #     if password:
    #         try:
    #             password_validation.validate_password(password, self.instance)
    #         except forms.ValidationError as error:
    #             self.add_error('password2', error)

    # def clean(self):    	
    # 	password1 = self.cleaned_data['password1']
    # 	password2 = self.cleaned_data['password2']
    # 	cleaned_data = super(RegisterForm, self).clean()
    # 	if password1 and password2 and password1 != password2:
    # 		form.название_поля.errors: возвращает ошибки валидации, связанные с полем
    # 		errors = {'password2' : ValidationError('Введені паролі не співпадають', code = 'password_mismatch')}
    # 		raise ValidationError(errors)


    def clean_email(self):
    	pass
    	# email = self.cleaned_data["email"]
    	# try:
    	# 	user = get_user_model().objects.get(email=email)
    	# 	raise forms.ValidationError("This email address already exists.")
    	# except get_user_model().DoesNotExist:
    	# 	return email


