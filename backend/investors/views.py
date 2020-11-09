import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from rest_framework import viewsets, status
from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import *
from .serializers import *


class InvestorView(APIView):
    @swagger_auto_schema(manual_parameters=[openapi.Parameter('investor_id', openapi.IN_QUERY, type='number')])
    def get(self, request, format=None):
        investor = get_object_or_404(Investor, id=request.GET.get('investor_id', 0))
        #     type_qualification = models.IntegerField(choices=TYPE_QUALIFICATION, default=None, null=True)
        #     document_qualification
        return Response(InvestorQualification(investor).data)

    @swagger_auto_schema(request_body=InvestorSerializer)
    def post(self, request, format=None):
        name = request.data.get('name', None)
        surname = request.data.get('surname', None)
        patronymic = request.data.get('patronymic', None)
        series_passport = request.data.get('series_passport', None)
        birthday = request.data.get('birthday', None)
        birth_place = request.data.get('birth_place', None)
        issue_date_passport = request.data.get('issue_date_passport', None)
        issue_by_passport = request.data.get('issue_by_passport', None)
        department_code = request.data.get('department_code', None)
        reg_address = request.data.get('reg_address', None)
        if not name or not surname or not patronymic or not series_passport or not birthday or not birth_place \
                or not issue_date_passport or not issue_by_passport or not department_code or not reg_address:
            new_investor = Investor(name=name, surname=surname, patronymic=patronymic, series_passport=series_passport,
                                    birthday=birthday, birth_place=birth_place, issue_date_passport=issue_date_passport,
                                    issue_by_passport=issue_by_passport, department_code=department_code,
                                    reg_address=reg_address)
            new_investor.save()
            return Response(InvestorDetailSerializer(new_investor).data)

        return Response({'error': 'invalid field or data in body'}, status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(manual_parameters=[openapi.Parameter('investor_id', openapi.IN_QUERY, type='number')])
    def put(self, request, format=None):
        investor_id = request.GET.get('investor_id', 0)
        investor = get_object_or_404(Investor, id=investor_id)

        if request.FILES and 'file' in request.FILES:
            photo = request.FILES['file']
            f = FileSystemStorage()
            filename = f.save(f'passport/{investor_id}_{photo.name}', photo)

            investor.passport = filename
            investor.save()
            return Response(InvestorDetailSerializer(investor).data)

        return Response({'error': 'invalid investor_id or file'}, status.HTTP_400_BAD_REQUEST)


# TODO: Не уверен, что для этого запроса нужно было выносить в отдельную функцию
class AcceptRuleView(APIView):
    @swagger_auto_schema(manual_parameters=[openapi.Parameter('investor_id', openapi.IN_QUERY, type='number')])
    def put(self, request, format=None):
        investor = get_object_or_404(Investor, id=request.GET.get('investor_id', 0))
        investor.accept_rules = True
        investor.save()
        return Response(InvestorDetailSerializer(investor).data)


class QualificationView(APIView):
    @swagger_auto_schema(manual_parameters=[openapi.Parameter('investor_id', openapi.IN_QUERY, type='number')])
    def get(self, request, format=None):
        investor_id = request.GET.get('investor_id', 0)
        investor = get_object_or_404(Investor, id=investor_id)

        return Response(InvestorDetailSerializer(investor).data)

    @swagger_auto_schema(manual_parameters=[openapi.Parameter('investor_id', openapi.IN_QUERY, type='number')],
                         request_body=InvestorQualification)
    def put(self, request, format=None):
        investor_id = request.GET.get('investor_id', 0)
        type_qualification = request.data.get('type_qualification', None)

        investor = get_object_or_404(Investor, id=investor_id)
        # Проверяем, чтоб тип квалификации был в системе
        if not investor_id or type_qualification not in (-1, 2, 3, 4, 5, 6):
            return Response({'error': 'invalid investor_id or file'}, status.HTTP_400_BAD_REQUEST)

        if type_qualification == -1:
            investor.type_qualification = type_qualification
            investor.save()
        elif 'file' not in request.FILES:
            return Response({'error': 'invalid file'}, status.HTTP_400_BAD_REQUEST)
        else:
            photo = request.FILES['file']
            f = FileSystemStorage()
            filename = f.save(f'qualification/{investor_id}_{photo.name}', photo)
            investor = get_object_or_404(Investor, id=investor_id)
            investor.document_qualification = filename
            investor.type_qualification = type_qualification
            investor.save()

        return Response(InvestorDetailSerializer(investor).data)
