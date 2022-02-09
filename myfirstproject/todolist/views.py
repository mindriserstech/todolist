from tempfile import template
from django.contrib import admin

from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar
import json
from todolist.form import UserProfileForm
#importing forms
from todolist.form import UserTaskForm
from todolist.form import AssignedTaskDescForm
from todolist.form import UserNoteForm
from todolist.form import PersonalTaskForm
from todolist.form import UserRegistrationForm
from todolist.form import UserLoginForm

# importing models
from todolist.models import UserNote
from todolist.models import User

# Create your views here.
def index(request, year=date.today().year, month=date.today().month):
    title = "This is a title"
    year = int(year)
    month = int(month)

    if year < 1999 or year > 2099:
        year = date.today().year
    
    month_name = calendar.month_name[month]

    cal = HTMLCalendar().formatmonth(year, month)

    title = "Current Month: " + month_name
    data = {'title':title, 'cal': cal , 'month': month}
    return render(request, "base.html", data)

# note - refractor
# note index - this method display all list of notes
def note_ajax_index(request):
    user_note = UserNote.objects.all()
    result = dict()
    for i in user_note:
        result.update({
            'title': "TITLE",
            'desc': "DESC",
        })
    return HttpResponse(request, json.dumps(result))

def note_index(request):
    user_note = UserNote.objects.all()
    return render(request, 'notes/index.html', {"notelist":user_note})

# note create - this method loads form and stores data of note
def note_create(request):
    if request.method == "POST":
        title = request.POST.get('note_title')
        desc = request.POST.get('note_description')
        added_at = request.POST.get('note_added_at')

        un = UserNote(note_title=title,\
            note_description=desc,\
            note_added_at=added_at)
        un.save()
        msg = "Successfully stored"
        user_note = UserNote.objects.all()
        return render(request, 'notes/index.html', {'msg':msg, 'data':user_note})
    else:
        note = UserNoteForm
        msg = "Request abort. Unauthorized url request"
        return render(request, 'notes/create.html', {'msg':msg, 'form':note})

def note_show(request, note_id):
    user_note = UserNote.objects.get(id=note_id)
    return render(request, 'notes/show.html', {'data': user_note})

def note_edit(request, note_id):
    user_edit = UserNote.objects.get(id=note_id)
    return render(request, 'notes/edit.html', {'data': user_edit})

def note_update(request):
    note_id = request.POST.get('id')
    if request.method == "POST":
        # data fetch by id
        note = UserNote.objects.get(id=note_id)
        note.note_title = request.POST.get('note_title')
        note.note_description = request.POST.get('note_description')
        note.note_added_at = request.POST.get('note_added_at')
        note.save()
        msg = "Successfully updated"
        user_note = UserNote.objects.all()
        return render(request, 'notes/index.html', {'data': user_note, 'msg': msg})
    else:
        msg = "Something went wrong"
        user_edit = UserNote.objects.get(id=note_id)
        return render(request, 'notes/edit.html', {'data': user_edit, 'msg': msg})

def note_delete(request, note_id):
    # creating object by id and deleting the object
    note = UserNote.objects.get(id=note_id)
    note.delete()
    
    # fetching remaining data and returning back to index page with data
    un = UserNote.objects.all()
    return render(request, 'notes/index.html', {'data': un, 'msg': "Successfully deleted"})

# user
def user_create(request):
    userForm = UserRegistrationForm 
    return render(request, 'users/create.html', {'form': userForm})

def user_index(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'users/index.html', {'username': username})
    else:
        template = 'users/login.html'
        ul = UserLoginForm
        msg = "Please login to access"
        context = {'form':ul, 'msg': msg}
        return render(request, template, context)

def user_register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        contact = request.POST.get('contact')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User(first_name=first_name, last_name=last_name, contact=contact, \
            username=username, password=password)
        user.save()

        # setting session
        request.session['username'] = username

        # checking session key if exist
        if request.session.has_key('username'):
            # getting session value
            uname = request.session['username']
            return render(request, 'users/index.html', {'username': uname})
    else:
        userForm = UserRegistrationForm 
        return render(request, 'users/create.html', {'form': userForm})

def user_login(request):
    template = 'users/login.html'
    form = UserLoginForm
    context = {'form':form}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username=username)
        if password == user.password:
            request.session['username'] = user.username
            if request.session.has_key('username'):
                uname = request.session['username']
                return render(request, 'users/index.html', {'username': uname})
        else:
            return render(request, template, context)
    else:
        return render(request, template, context)

def user_profile(request):
    if request.session.has_key('username'):
        username = request.session['username']
        user = User.objects.get(username=username)
        form = UserProfileForm
        if request.method == "POST":
            formSave = UserProfileForm(request.POST, request.FILES)
            if formSave.is_valid():
                formSave.save()
                return render(request, 'users/show.html', {'form': form, 'data': user})
        else:
            return render(request, 'users/show.html', {'form': form, 'data': user})
    else:
        formLogin = UserLoginForm
        return render(request, 'users/login.html', {'form': formLogin, 'msg': "please login to access"})

def user_logout(request):
    template = 'users/login.html'
    ul = UserLoginForm
    msg = "Please login to access"
    context = {'form':ul, 'msg': msg}
    if request.session.has_key('username'):
        del request.session['username']
        return render(request, template, context)
    else:
        return render(request, template, context)