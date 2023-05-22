from django.db import models


class House(models.Model):

    """Model Definition for Houses"""

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True)

    # on_delete = models.SETNULL : 사용자가 계정을 지워도 house는 주인이 없는 상태로 남을것이다.
    # on_delete = models.CASCADE : 사용자가 계정을 지우면 house도 지워진다

    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
