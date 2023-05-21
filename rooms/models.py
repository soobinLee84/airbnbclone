from django.db import models
from common.models import CommonModel


class Room(CommonModel):

    """ " Room Model Definition"""

    class RoomkindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Privatge Room")
        SHARED_ROOM = ("shared_room", "Shared Room")

    name = models.CharField(max_length=180, default="")
    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    pet_friendly = models.BooleanField(
        default=True,
    )
    kind = models.CharField(
        max_length=20,
        choices=RoomkindChoices.choices,
    )
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

    amenities = models.ManyToManyField(
        "rooms.Amenity",
    )

    def __str__(self):
        return str(self.name)


class Amenity(CommonModel):
    """Amenity Definition"""

    name = models.CharField(max_length=150)
    # blank = True 는 django form 에서의 공백
    # null = True 는 데이터베이스에서의 공백
    description = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Amenities"
