import email
from tempfile import template
from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar
import json

from todolist.form import UserProfileForm
from django.core.mail import send_mail as sm

#  json response
from django.http import JsonResponse
from django.core import serializers

#importing forms
from todolist.form import UserTaskForm, AssignedTaskDescForm, UserNoteForm, PersonalTaskForm, UserRegistrationForm, UserLoginForm

# importing models
from todolist.models import UserNote
from todolist.models import User, UserTask

# task CRUD
# index (display list), create (form), store (data store), edit (data edit), update (data update), delete (data delete),
# show (data show by id)
def tasks_index(request):
    context = UserTask.objects.all()
    return render(request, 'tasks/index.html', {'data': context, 'msg' : 'Success'})

def tasks_create(request):
    tf = UserTaskForm()
    return render(request, 'tasks/create.html', {'form': tf})

def tasks_store(request):
    tf = UserTaskForm()
    if request.method == "POST":
        try:
            ut = UserTask(task_title=request.POST.get('task_title'),\
                task_description=request.POST.get('task_description'),\
                    task_assigned_at=request.POST.get('task_assigned_at'), \
                        task_accomplish_date=request.POST.get('task_accomplish_date'), \
                            task_assigned_by=request.POST.get('task_assigned_by'), \
                                task_progress_status=request.POST.get('task_progress_status'), \
                                    task_assigned_to=request.POST.get('task_assigned_to'))
            ut.save()
            context = UserTask.objects.all()
            return render(request, 'tasks/index.html', {'data': context, 'msg' : 'Success'})
        except:
            return render(request, 'tasks/create.html', {'form': tf, 'msg' : 'Something went wrong'})
    else:
        return render(request, 'tasks/create.html', {'form': tf, 'msg' : 'Something went wrong'})


def tasks_edit(request):
    return render()

def tasks_update(request):
    return render()

def tasks_delete(request):
    return render()

def tasks_show(request):
    return render()
# api functions
def note_index_api(request):
    if request.headers:
        if request.method == "GET":
            # data = UserNote.objects.all()
            data = dict(
                {
                    "note_title": "This is note title",
                    "note_desc": "This is desc",
                    "note_added_at": "2022-02-20",
                }
            )
            api_response = {
                'status_code': 200,
                'message': "Fetched Successfully",
                'data': data,
                'error': []
            }

            return JsonResponse(api_response)
        else:
            api_response = {
                'status_code': 405,
                'message': "Method not allowed",
                'data': [],
                'error': {
                    'code': 405,
                    'message': 'Must be GET request'
                }
            }
            return JsonResponse(api_response)
    else:
        api_response = {
            'status_code': 503,
            'message': "Serivce Not Available",
            'data': [],
            'error': {
                'code': 503, 
                'message': 'Serivce Not Available'
            }
        }
        return JsonResponse(api_response)

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
    result = serializers.serialize("json", UserNote.objects.all())
    return HttpResponse(result)

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

# send email
def send_email(request):
    # to take request from post method
    
    # res = sm(
    #     subject = request.POST.get('subject'),
    #     message = request.POST.get('message'),
    #     from_email = 'c4crypt@gmail.com',
    #     recipient_list = [request.POST.get('receiver_email')],
    #     fail_silently = False,
    # )

    res = sm(
        subject = 'Gmail Email Send Test',
        message = 'Here is the message we are send you to test our gmail send message',
        from_email = 'c4crypt@gmail.com',
        recipient_list = ['sandesh@cac.edu.au'],
        fail_silently = False,
        # fail_silently takes boolean value. If set False it will raise smtplib.STMPException if the error
        # occurs while sending the email
    )
    return HttpResponse(request, "Email send sucess" + str(res))

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

def user_profile_ajax(request):
    # profile = User.objects.get(username=request.session['username'])
    # username = request.session['username']
    data = serializers.serialize('json', User.objects.all())
    return HttpResponse(data)

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