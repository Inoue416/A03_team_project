from rest_framework import serializers
from app.models.nice import Nice

class NiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nice
        fields = ('markdown', 'user')
