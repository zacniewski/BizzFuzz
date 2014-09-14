# -*- coding: utf-8 -*-
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
#from bizz_fuzz_app.forms import MyUserForm
#from bizz_fuzz_app.admin import UserCreationForm, UserChangeForm
from bizz_fuzz_app.models import MyUser


class MyUsersView(ListView):
    template_name = 'view_all_users.html'
    model = MyUser
    success_url = '/'


class MyUserUpdateView(UpdateView):
    template_name_suffix = '_update_form'
    model = MyUser
    success_url = '/'
    fields = ['birthday', 'random_number']

    #def get_success_url(self):
    #    return reverse_lazy('update-user', kwargs={'pk': self.get_object().id})


class MyUserDeleteView(DeleteView):
    model = MyUser
    success_url = '/'


# Doesn't work yet
def export_xls(request):
    from export_xls.views import export_xlwt
    fields = ["username", "birthday", "random_number"]

    filename = MyUser._meta.verbose_name_plural.lower()
    queryset = MyUser.objects.all()
    try:
        return export_xlwt(filename, fields, queryset.values_list(*fields))
    except Exception, e:
        raise e
