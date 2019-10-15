from rest_framework_gis import serializers
from .models import Step
import geostuff_app.validators.step_validator as step_validator


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ('id', 'name', 'point')

    def validate(self, data):
        data['name'] = step_validator.validate_step(data)

        return data

