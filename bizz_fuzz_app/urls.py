from django.conf.urls import patterns, url
from .views import MyUsersView, MyUserUpdateView, MyUserDeleteView
from django.views.generic.edit import CreateView
from bizz_fuzz_app.admin import UserCreationForm, UserChangeForm

urlpatterns = patterns(
    '',
    url(r'^view-all-users/$',
        MyUsersView.as_view(),
        name="all-users-view"),
    url(r'^add-new-user/$', CreateView.as_view(
            template_name='add_new_user.html',
            form_class=UserCreationForm,
            success_url='/'),
        name="add-new-user"),
    url(r'^update-user/(?P<pk>\d+)/$',
        MyUserUpdateView.as_view(),
        name="update-user"),
    url(r'^delete-user/(?P<pk>\d+)/$',
        MyUserDeleteView.as_view(),
        name="delete-user"),
    url(r'^export-to-excel/$', 'export_xls', name='export_xls'), # doesn't work so far'
)