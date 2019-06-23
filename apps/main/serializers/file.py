from rest_framework import serializers

from main.models import File


class FileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'file', 'name', 'content_type']
        extra_kwargs = dict(
            name=dict(read_only=True),
            content_type=dict(read_only=True),
        )

    def create(self, validated_data):
        instance: File = super(FileModelSerializer, self).create(validated_data)
        instance.name = instance.file.name
        instance.content_type = instance.name.split('.')[-1]
        instance.save()
        return instance
