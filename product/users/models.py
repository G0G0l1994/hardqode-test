from django.contrib.auth.models import AbstractUser
from django.db import models

from courses.models import Course


class CustomUser(AbstractUser):
    """Кастомная модель пользователя - студента."""

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=250,
        unique=True
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'last_name',
        'password',
        
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-id',)

    def __str__(self):
        return self.get_full_name()


class Balance(models.Model):
    """Модель баланса пользователя."""

    value = models.PositiveIntegerField(
        verbose_name='Значение баланса',
        default=1000
    )
    users = models.ForeignKey(
        CustomUser, 
        verbose_name='Баланс', 
        related_name='user_balance',
        on_delete=models.CASCADE
    )
    # TODO



    class Meta:
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'
        ordering = ('-id',)

    def __str__(self):
        return self.users.get_full_name()


class Subscription(models.Model):
    """Модель подписки пользователя на курс."""
    user = models.ForeignKey(CustomUser,related_name='subscribe',on_delete=models.CASCADE)
    course = models.ForeignKey(Course,related_name="Курс", on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    

    

    # TODO

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('-id',)
    
    def __str__(self):
        return f"{self.user.username}"

