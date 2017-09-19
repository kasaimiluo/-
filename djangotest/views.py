# -*- coding:utf-8 -*-
from django.shortcuts import render
import pymysql
import random
from .models import UserMessage

# Create your views here.

def getform(request):
    # messages=None
    # all_messages=UserMessage.objects.filter(name='luguanyan')
    # if all_messages:
    #     messages = all_messages[0]

    # for messages in all_messages:
    #     #messages.delete()
    #     print (messages.name)

    if request.method == "POST":
         name=request.POST.get('name','')
         sex=request.POST.get('sex', '')
         age=request.POST.get('age', '')
         university=request.POST.get('university', '')
         major=request.POST.get('major', '')
         message=request.POST.get('message','')
         address=request.POST.get('address','')
         email=request.POST.get('email','')

         user_message = UserMessage()
         user_message.name=name
         user_message.sex=sex
         user_message.age=age
         user_message.university=university
         user_message.major=major
         user_message.message=message
         user_message.email=email
         user_message.address=address
         user_message.save()

    return render(request, 'wang.html')
    #{"my_message":messages}