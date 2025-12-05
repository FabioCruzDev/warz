from django.db import models


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Village(models.Model):
    owner = models.ForeignKey('player.Player', null=True, blank=True, on_delete=models.DO_NOTHING)
    x = models.IntegerField()
    y = models.IntegerField()

    def __str__(self):
        return f"{self.name()} ({self.x}|{self.y})"
    
    def name(self):
        return f"Village of {self.owner.user.username}" if self.owner else "Barbarian Village"
    
    def coordinates(self):
        return f"({self.x}|{self.y})"
    
    def population(self):
        pass