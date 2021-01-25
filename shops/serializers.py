from rest_framework import serializers

from .models import Street, Shop, City


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class StreetSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Street
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):

    city = serializers.SlugRelatedField(slug_field='name',
                                        queryset=City.objects.all())
    street = serializers.SlugRelatedField(slug_field='name',
                                          queryset=Street.objects.all())

    class Meta:
        model = Shop
        fields = '__all__'


class ShopCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = '__all__'


