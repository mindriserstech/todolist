from django import forms
from django.db.models import fields
from todolist.models import UserTask
from todolist.models import AssignedTaskDescription
from todolist.models import PersonalTask
from todolist.models import UserNote

class UserTaskForm(forms.ModelForm):
    class Meta:
        model = UserTask
        fields = "__all__"

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