from django.db import models


class CommonModel(models.Model):
    """Common Model Definition"""

    # auto_now_add = 해당 object가 생성되었을 때 시간으로 설정
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now = object가 저장(update)될 때마다 해당필드를 현재 date로 설정
    updatedd_at = models.DateTimeField(auto_now=True)

    # Meta 클래스는 django에서 model을 설정할 때 쓰기때문에 우리의 데이타베이스에서
    # 보이지않게끔 하는 설정이다. (재사용에 용이)
    class Meta:
        abstract = True
