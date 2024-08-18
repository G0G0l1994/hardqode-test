from django.db import models




class Course(models.Model):
    """Модель продукта - курса."""
    
    author = models.CharField(
        max_length=250,
        verbose_name='Автор',
    )
    title = models.CharField(
        
        max_length=250,
        verbose_name='Название',
        null=True
    )
    start_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name='Дата и время начала курса'
    )

    price = models.PositiveIntegerField(
        verbose_name='Стоимость'
    )

    is_active = models.BooleanField(
        verbose_name='Доступно к покупке',
        default=True
    )
 
    
    # TODO

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ('-id',)
        
        
    def __str__(self):
        return self.title
    


class Lesson(models.Model):
    """Модель урока."""

    title = models.CharField(
        max_length=250,
        verbose_name='Название',
    )
    link = models.URLField(
        max_length=250,
        verbose_name='Ссылка',
    )

    course = models.ForeignKey(
        Course,
        name = 'Course', 
        verbose_name='Курс',
        on_delete=models.CASCADE,
        null=True
    )

    # TODO

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('id',)

    def __str__(self):
        return self.title


class Group(models.Model):
    """Модель группы."""

    group_name = models.CharField(
        verbose_name='Имя группы',
        max_length=100
    )
    free_seats = models.IntegerField(
        verbose_name='Свободные_места',
        default=10
    )

    def __str__(self):
        return self.group_name
    

    # TODO

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ('-id',)


