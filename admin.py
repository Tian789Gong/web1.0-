from django.contrib import admin
from .models import Topic, Entry 
# from learning_logs.models import Topic 

# Register your models here.在这里注册你的模型
# 告诉Django管理后台，你希望将 Topic 模型注册到管理后台中。
admin.site.register(Topic)
admin.site.register(Entry)

