from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from schoolapp.models import Department, Course


class RegistrationForm(UserCreationForm):


    class Meta:
        model = User
        fields = ['username']





class StudentForm(forms.Form):
    name = forms.CharField(label='Name')
    dob = forms.DateField(label='DOB',widget=forms.DateInput(attrs={'type': 'date'}))
    age = forms.IntegerField(label='Age')
    GENDER_CHOICES = [('male', 'Male'),
                      ('female', 'Female'),
                      ('other', 'Other'),
                      ]
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, widget=forms.RadioSelect)
    phone_number = forms.CharField(label='Phone Number', max_length=10)
    email = forms.EmailField(label='Mail ID')
    address = forms.CharField(label='Address', widget=forms.Textarea)
    department = forms.ModelChoiceField(label='Department', queryset=Department.objects.all())
    course = forms.ModelChoiceField(label='Course', queryset=Course.objects.none())
    purpose_choices = [('enquiry', 'Enquiry'),
                       ('place_order', 'Place Order'),
                       ('return', 'Return')
                       ]
    purpose = forms.ChoiceField(label='Purpose', choices=purpose_choices, widget=forms.Select)
    materials_provided = forms.MultipleChoiceField(
        choices=[('paper', 'Exam papers'), ('books', 'Books'), ('stationery', 'Stationery')],
        widget=forms.CheckboxSelectMultiple,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.all()
        self.fields['department'].widget.attrs.update({'id': 'department-dropdown'})
        self.fields['course'].widget.attrs.update({'id': 'course-dropdown'})

