from rest_framework import serializers
from .models import Chart


class ChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chart
        fields = [
            "is_pregnant",
            "is_diabetic",
            "is_smoker",
            "is_allergic",
            "heart_disease",
            "dificulty_healing",
            "use_medication",
            "other_information",
        ]
