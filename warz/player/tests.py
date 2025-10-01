from django.test import TestCase
from warz.player.models import Player
from model_bakery import baker

class PlayerModelTest(TestCase):
    def setUp(self):
        user = baker.make('auth.User', username='myplayer')
        self.player = Player.objects.create(user=user, level=1, is_vip=False)

    def tearDown(self):
        self.player.delete()

    def test_player_str(self):
        """
        Test the string representation of the Player model.
        """
        self.assertEqual(str(self.player), "myplayer")

    def test_player_object(self):
        """
        Test the Player model fields.
        """
        expected = {self.player.level: 1, self.player.is_vip: False}
        for key, value in expected.items():
            with self.subTest():
                self.assertEqual(key, value)
