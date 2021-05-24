from rest_framework import serializers
from . models import CovidCaseWebData



class CovidCaseWebDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = CovidCaseWebData
        fields = "__all__"

        read_only_fields = ["country_name",]
