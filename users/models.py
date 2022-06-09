from django.db import models


# Create your models here.


class User(models.Model):  # 여기서의 모델은 도메인이다.
    user_id_migrations = True
    username = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=10)
    name = models.TextField
    email = models.TextField
    regDate = models.TextField

    class Meta:
        db_table = "users"  # 안에서 부모를 생성

    def __str__(self):  # 데이터베이스를 연결 하는 도메인 객체기 때문에 init을 사용 하지 않는다.
        return f'{self.pk} {self.username}'
