from rest_framework import serializers
from . models import Result, MarkSheet

class MarkSheetNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkSheet
        fields = ['id', 'cgpa', 'is_pass']


class ResultBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['id', 'std_id', 'full_name', 'marks']


class ResultSerializer(serializers.ModelSerializer):
    name = MarkSheetNestedSerializer(many=True, read_only=True)

    class Meta:
        model = Result
        fields = ['id', 'std_id', 'full_name', 'marks', 'name']

class MarkSheetSerializer(serializers.ModelSerializer):
    std_name=ResultBasicSerializer(read_only=True)
    std_name_id=serializers.PrimaryKeyRelatedField(
        queryset=Result.objects.all(),
        source='std_name',
        write_only=True
    )

    class Meta:
        model=MarkSheet
        fields=['id', 'std_name', 'std_name_id', 'cgpa', 'is_pass']