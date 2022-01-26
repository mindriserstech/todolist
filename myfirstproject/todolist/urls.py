from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    # urls - note
    #path('note/', views.note, name="note.index"),
    path('note-add/', views.note_insert, name="note.add"),

    # urls - note - code refractor
    path('note/', views.note_index, name="note.index"),
    path('note/create', views.note_create, name="note.create"),
    path('note/update', views.note_update, name="note.update"),
    path('note/show/<int:note_id>', views.note_show, name="note.show"),
    path('note/edit/<int:note_id>', views.note_edit, name="note.edit"),
    path('note/delete/<int:note_id>', views.note_delete, name="note.delete"),

    # index.html
    # ORM 
    # 1. index - display whole datalist
    # 2. store - store data in DB
    # 3. create - create form
    # 4. show - display single data by id
    # 5. edit - display edit (single) data by id 
    # 6. delete - delete data by id
    # 7. update - update data by id
]