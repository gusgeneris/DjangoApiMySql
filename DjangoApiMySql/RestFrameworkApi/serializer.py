from rest_framework import serializers

class InstitucionSerializer(serializers.Serializer):
    """Instituciones Serializer"""
    nombre = serializers.CharField()
    url = serializers.URLField()
    
class CreateInstitucionSerializer(serializers.Serializer):
    """Create Institucion"""
    nombre = serializers.CharField(max_length=140)
    url = serializers.URLField(max_length=140)
    