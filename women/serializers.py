import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault()) # чтобы поле с юзер заполнялось автоматически при аутентификации пользователя
    class Meta:
        model = Women
        fields = '__all__'  # какие поля будет возвращать клиенту
