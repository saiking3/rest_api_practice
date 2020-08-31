from rest_framework import serializers
from .models import Books

"""
#----Serializers------#
class BooksSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)
    category = serializers.CharField(max_length=10)
    reference_no = serializers.IntegerField()
    CREATED_ON = serializers.DateTimeField()
    UPDATED_ON = serializers.DateTimeField()

    def create(self, validated_data):
        return Books.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.reference_no = validated_data.get('reference_no', instance.reference_no)
"""

#----Model Serializers----#
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"