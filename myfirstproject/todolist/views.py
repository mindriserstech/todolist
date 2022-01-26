from django.contrib import admin

from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar

#importing forms
from todolist.form import UserTaskForm
from todolist.form import AssignedTaskDescForm
from todolist.form import UserNoteForm
from todolist.form import PersonalTaskForm

# importing models
from todolist.models import UserNote

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

def user_task(request):
    userTask = UserTaskForm
    return render(request, "index.html", {'form':userTask})

# loads the note index page
def note(request):
    note = UserNoteForm

    # method one by creating object and retreiving data
    un1 = UserNote
    un1.objects.all()
    # method two creating object and retrieving data at the time
    un2 = UserNote.objects.all()
    
    return render(request, 'note.html', {'form': note, "obj1": un1, "obj2": un2})

# stores the note data to database
def note_insert(request):
    template = 'note.html'

    # creating object of form
    note = UserNoteForm
        
    # filtering request method
    if request.method == "POST":
        # filtering request data
        title = request.POST.get('note_title')
        desc = request.POST.get('note_description')
        add_at = request.POST.get('note_added_at')
        
        un = UserNote(note_title=title, \
            note_description=desc, \
                note_added_at=add_at)
        un.save()
        # success message
        msg = "Success"
        # sending response to request
        return render(request, template, {'form': note, 'msg': msg, 'data': un})
        # else:
        #     msg = 'Fail'
        #     return render(request, template, {'form': note, 'msg': msg})
    else:
        msg = "Something went wrong"
        return render(request, template, {'form': note, 'msg': msg})

# note - refractor
# note index - this method display all list of notes
def note_index(request):
    user_note = UserNote.objects.all()
    return render(request, 'notes/index.html', {"data":user_note})

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
