from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db import models
from warz.core.models.village import AbstractBaseModel
from uuid import uuid4

User = get_user_model()
def avatar_upload_to(instance, filename):
    _, ext = filename.rsplit('.', 1)
    uuid = uuid4().hex
    return f'avatars/{instance.user.id}/{uuid}.{ext}'

class Player(AbstractBaseModel):
    user = models.OneToOneField(User, verbose_name=_('user'), on_delete=models.CASCADE, related_name='player')
    level = models.IntegerField(verbose_name=_('level'), default=1)
    is_vip = models.BooleanField(verbose_name=_('is vip'), default=False)
    avatar = models.ImageField(verbose_name=_('avatar'), upload_to=avatar_upload_to, null=True, blank=True)
    presentation = models.TextField(verbose_name=_('presentation'), null=True, blank=True)

    class Meta:
        verbose_name = _('player')
        verbose_name_plural = _('players')

    def __str__(self):
        return f'{self.user.username}'