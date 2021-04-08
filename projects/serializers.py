from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'developer', 'title', 'description', 'start_date', 'end_date'
        )

    def validate(self, attrs):
        if attrs['start_date'] >= attrs['end_date']:
            raise serializers.ValidationError(
                'La fecha de inicio no puede ser igual o mayor la de fin'
            )

        return attrs
