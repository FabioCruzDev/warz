from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from warz.core.models import AbstractBaseModel, models


User = get_user_model()

class Player(AbstractBaseModel):
    user = models.OneToOneField(User, verbose_name=_('user'), on_delete=models.CASCADE, related_name='player')
    level = models.IntegerField(verbose_name=_('level'), default=1)
    is_vip = models.BooleanField(verbose_name=_('is vip'), default=False)
    avatar = models.ImageField(verbose_name=_('avatar'), upload_to='avatars/', null=True, blank=True)
    presentation = models.TextField(verbose_name=_('presentation'), null=True, blank=True)

    class Meta:
        verbose_name = _('player')
        verbose_name_plural = _('players')

    def __str__(self):
        return f'{self.user.username}'