from django.urls import path
from works import views


urlpatterns=[
    path('',views.Register.as_view(),name="register"),
    path('login/',views.Login.as_view(),name="login"),
    path('projectadd/',views.ProjectaddingView.as_view(),name="projectadd"),
    path('projectlist/',views.ProjectlistView.as_view(),name="projectlist"),
    path("logout/",views.LogoutView.as_view(),name="logout"),
    path('projectlist/delete/<int:pk>',views.DeleteView.as_view(),name="delete"),
    path('projectlist/update/<int:pk>',views.UpdateView.as_view(),name="update"),

    path('project/<int:project_id>/todo/', views.ProjectTodoView.as_view(), name='project_todo'),
    path('todo/<int:todo_id>/', views.TodoUpdateView.as_view(), name='todo_update'),
    path('todo/<int:todo_id>/delete/', views.TodoDeleteView.as_view(), name='todo_delete'),
]