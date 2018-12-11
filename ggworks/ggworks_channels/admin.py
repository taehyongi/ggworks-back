from django.contrib import admin
from .models import ChatMessage, ChatRoom, ChatRoomUser

# Register your models here.

class ChatRoomAdmin(admin.ModelAdmin):
  fields = ['name']

class ChatRoomUserAdmin(admin.ModelAdmin):
  fields = ['chat_room', 'chat_user']

class ChatMessageAdmin(admin.ModelAdmin):
  fields = ['chat_room', 'chat_user', 'message_text']

admin.site.register(ChatRoom, ChatRoomAdmin)
admin.site.register(ChatRoomUser, ChatRoomUserAdmin)
admin.site.register(ChatMessage, ChatMessageAdmin)
