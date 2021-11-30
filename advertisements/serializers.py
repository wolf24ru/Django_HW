from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description',
                  'creator', 'status', 'created_at')

    def create(self, validated_data):
        """Метод для создания"""
        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        count_status = len(Advertisement.objects.all().filter(status='OPEN', creator=self.context['request'].user))
        error_msg = 'Один пользователь может иметь только 10 одновременно открытых объявлений'
        match self.context['view'].action:
            case 'partial_update':
                if count_status <= 9 or data['status'] == 'CLOSED':
                    return data
                raise ValueError(error_msg)
            case 'create':
                if count_status <= 9:
                    return data
                raise ValueError(error_msg)
