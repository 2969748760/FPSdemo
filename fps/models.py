from django.db import models

class Room(models.Model):
    name = models.CharField(default="Room", max_length=100) # 房间名
    port = models.IntegerField(default=7777) # 房间端口号

    def __str__(self):
        return self.name + ' - ' + str(self.port)
