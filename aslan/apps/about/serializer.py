from rest_framework import serializers

from apps.about import models

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ['id', 'title', 'description', 'created_at', 'completed']

        