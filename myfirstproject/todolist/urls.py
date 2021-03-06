from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [

    # tasks url
    path('tasks/', views.tasks_index, name="tasks.index"),
    path('tasks/create', views.tasks_create, name="tasks.create"),
    path('tasks/store', views.tasks_store, name="tasks.store"),
    path('tasks/edit/<int:note_id>', views.tasks_edit, name="tasks.edit"),
    path('tasks/show/<int:note_id>', views.tasks_show, name="tasks.show"),
    path('tasks/delete/<int:note_id>', views.tasks_delete, name="tasks.delete"),
    path('tasks/update', views.tasks_update, name="tasks.update"),

    # api response
    path('api/v1/note', views.note_index_api, name="api.note.index"),
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
    path('users/profile/ajax', views.user_profile_ajax, name="up.ajax"),
    path('users/create', views.user_create, name="users.create"),
    path('users/register', views.user_register, name="users.register"),
    path('users/login', views.user_login, name="users.login"),
    path('users/logout', views.user_logout, name="users.logout"),

    # send email
    path('send-email/', views.send_email, name="send.email")

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