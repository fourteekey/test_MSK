from django.db import models

#
# class Qualification_type(models.Model):
#     id = models.AutoField()
#     name = models.CharField(max_length=50)


class Investor(models.Model):
    TYPE_QUALIFICATION = (
        (-1, 'Без квалификации'),
        (1, 'Высшее экономическое образование в ВУЗе с правом аттестации профучастника'),
        (2, 'Общая стоимость ценный бумаг и производственных > 6 млн Р. '),
        (3, 'Опыт работы в финансовой компании > 2 лет'),
        (4, 'Депозитные, металические счета > 6 млн Р'),
        (5, 'Активная торговля ценными бумагами и производственными на сумму > 6 млн Р'),
        (6, 'Уже квалифицирован инвестиционной платформой')
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=30)
    series_passport = models.CharField(max_length=15)
    birthday = models.DateField()
    birth_place = models.CharField(max_length=100)
    issue_date_passport = models.DateField()
    issue_by_passport = models.CharField(max_length=100)
    passport = models.ImageField(default=None, null=True)
    department_code = models.IntegerField()
    reg_address = models.CharField(max_length=100)
    accept_rules = models.BooleanField(default=False)
    type_qualification = models.IntegerField(choices=TYPE_QUALIFICATION, default=None, null=True)
    document_qualification = models.ImageField(default=None, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    class Meta:
        db_table = 'investors'
