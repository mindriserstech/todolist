from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    # urls - note - code refractor
    path('note/', views.note_index, name="note.index"),
    path('note/ajax', views.note_ajax_index, name="note.ajax"),
    path('note/create', views.note_create, name="note.create"),
    path('note/update', views.note_update, name="note.update"),
    path('note/show/<int:note_id>', views.note_show, name="note.show"),
    path('note/edit/<int:note_id>', views.note_edit, name="note.edit"),
    path('note/delete/<int:note_id>', views.note_delete, name="note.delete"),

    # urls - users
    path('users/', views.user_index, name="users.index"),
    path('users/profile', views.user_profile, name="users.profile"),
    path('users/create', views.user_create, name="users.create"),
    path('users/register', views.user_register, name="users.register"),
    path('users/login', views.user_login, name="users.login"),
    path('users/logout', views.user_logout, name="users.logout")

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