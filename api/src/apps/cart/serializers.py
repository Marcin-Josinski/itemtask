from rest_framework import serializers


class ItemCreateInputSerializer(serializers.Serializer):
    external_id = serializers.CharField(max_length=255)
    name = serializers.CharField(required=False)
    value = serializers.IntegerField(min_value=1, required=False)
