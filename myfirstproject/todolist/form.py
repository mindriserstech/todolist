from django import forms
from django.db.models import fields
from todolist.models import UserProfile
from todolist.models import User
from todolist.models import UserTask
from todolist.models import AssignedTaskDescription
from todolist.models import PersonalTask
from todolist.models import UserNote

class UserTaskForm(forms.ModelForm):
    class Meta:
        model = UserTask
        fields = "__all__"

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)

class AssignedTaskDescForm(forms.ModelForm):
    class Meta:
        model = AssignedTaskDescription
        fields = "__all__"

class PersonalTaskForm(forms.ModelForm):
    class Meta:
        model = PersonalTask
        fields = "__all__"

class UserNoteForm(forms.ModelForm):
    class Meta:
        model = UserNote
        fields = "__all__"