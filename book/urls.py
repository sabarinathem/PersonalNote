from django.urls import path
from book import views
app_name="book"
urlpatterns=[
    path('',views.index,name="index"),
    path('module/<str:data>',views.module,name="module"),
    path('heading/<str:data>',views.heading,name="heading"),
    path('content/<str:data>',views.content,name="content"),
    path('addnote/',views.addnote,name="addnote"),
    path('subject_equation/',views.subject_equation,name="subject_equation"),
    path('module_equation/<str:data>',views.module_equation,name="module_equation"),
    path('heading_equation/<str:data>',views.heading_equation,name="heading_equation"),
    path('equation/<str:data>',views.equation,name="equation"),
    path('add_equation/',views.addequation,name="add_equation"),
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutPage,name="logout"),
    path('addtimetable/',views.addtimetable,name="addtimetable"),
    path('displaytimetable/',views.displaytimetable,name="displaytimetable"),
    path('edittimetable',views.edit_timetable,name="edittimetable"),
    path('edit_note/<int:id>',views.edit_note,name="edit_note"),
    path('delete_note/<int:id>',views.delete_note,name="delete_note"),
    
   


]