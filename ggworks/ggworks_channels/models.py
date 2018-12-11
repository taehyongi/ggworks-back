# from __future__ import unicode_literals

from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import User

class ChatRoom(models.Model):
  name = models.TextField()
  created_date = models.DateTimeField(auto_now_add=True)
  modified_date = models.DateTimeField(auto_now=True)

class ChatRoomUser(models.Model):
  chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
  chat_user = models.ForeignKey(User, on_delete=models.CASCADE)
  join_date = models.DateTimeField(auto_now_add=True)

  class Meta:
        unique_together = (("chat_room", "chat_user"))

class ChatMessage(models.Model):
  chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
  chat_user = models.ForeignKey(User, on_delete=models.CASCADE)
  message_date = models.DateTimeField(auto_now_add=True, db_index=True)
  message_text = models.TextField()