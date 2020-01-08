from django.shortcuts import render
from rest_framework import viewsets

from geostuff_app.BaseModelViewSet import BaseModelViewSet
from geostuff_app.serializers import StepSerializer, MapSerializer
from geostuff_app.models import Step, Map
from rest_framework.decorators import action
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework import permissions
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import logging, datetime

# Create your views here.

logger = logging.getLogger(__name__)

def index(request):
    try:
        return render(request, "index.html", {
        })
    except ObjectDoesNotExist:
        logger.error('ERROR')
        return render(request, 'index.html', {
        })

class StepsViewSet(BaseModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    permission_classes_by_action = {
        'create': (permissions.AllowAny,),
        'list': (permissions.IsAuthenticatedOrReadOnly,),
        'retrieve': (permissions.AllowAny,),
        'update': (permissions.AllowAny,),
        'destroy': (permissions.IsAuthenticatedOrReadOnly,),
        'search': (permissions.AllowAny,)
    }
    # add an action 'pouet' to the url
    # @action(methods=['get'], detail=False)
    # def pouet(self, request, pk=None):
    #     a = 'a'

    #override the retrieve get, see https://micropyramid.com/blog/understanding-routers-in-djangorestframework/
    # def retrieve(self, request, *args, **kwargs):
    #     b = 'b'
    #     b = 'bb'


class MapsViewSet(BaseModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    permission_classes_by_action = {
        'create': (permissions.AllowAny,),
        'list': (permissions.IsAuthenticatedOrReadOnly,),
        'retrieve': (permissions.AllowAny,),
        'update': (permissions.AllowAny,),
        'destroy': (permissions.IsAuthenticatedOrReadOnly,),
        'search': (permissions.AllowAny,)
    }