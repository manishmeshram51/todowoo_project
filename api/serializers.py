from todo.models import Todo
from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ['id', 'title', 'memo', 'important','created','datecompleted']
        read_only_fields = ['datecompleted', 'created']

class TodoCompleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ['id']
        read_only_fields = [ 'memo', 'important','created','datecompleted']
