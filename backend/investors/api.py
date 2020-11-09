from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *


urlpatterns = [
    path('investor/passport', InvestorView.as_view()),
    path('investor/accept_rules', AcceptRuleView.as_view()),
    path('investor/qualification', QualificationView.as_view()),
]
