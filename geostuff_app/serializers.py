from rest_framework.serializers import ModelSerializer
from rest_framework_gis import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Step, Map
import geostuff_app.validators.step_validator as step_validator


class StepSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Step
        fields = ('id', 'name', 'point')
        geo_field = "point"

    def validate(self, data):
        step_validator.validate_step(data)

        return data


class MapSerializer(ModelSerializer):
    class Meta:
        model = Map
        fields = "__all__"
