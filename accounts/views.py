from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.base import View
from .forms import *


class PageUserView(TemplateView):
    template_name = "account/userprofile.html"

#
# class PageContact(View):
#     def page_contact(self, request):
#
#         sent = False
#         mailfrom = local_settings.EMAIL_HOST_USER
#         mailto = [local_settings.EMAIL_HOST_USER]
#         if request.method == 'POST':
#             form = ContactForm(request.POST)
#             if form.is_valid():
#                 cd = form.cleaned_data
#                 subject = 'Новое письмо от {}'.format(cd['name'])
#                 message = 'Прислал {}. Пишет {}'.format(cd['email'], cd['message'])
#                 send_mail(subject, message, mailfrom, mailto)
#                 sent = True
#         else:
#             form = ContactForm()
#
#         return render(request, 'accounts/new_message.html', context={'form': form,
#                                                                      'sent': sent})
