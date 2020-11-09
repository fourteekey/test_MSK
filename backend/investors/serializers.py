from rest_framework import serializers

from .models import *


class InvestorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = '__all__'


class InvestorQualification(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = ('id', 'type_qualification', 'document_qualification',)


class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = ('name', 'surname', 'patronymic', 'series_passport', 'birthday', 'birth_place', 'issue_date_passport',
                  'issue_by_passport', 'department_code', 'reg_address',)
