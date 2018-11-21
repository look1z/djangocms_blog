from django.http import HttpResponse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
import json


def getUserInfo(request):
    if request.method == "POST":
        name = request.POST.get('name')
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)