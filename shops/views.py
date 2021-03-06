from datetime import datetime

from rest_framework import status
from rest_framework import viewsets, generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from .models import Street, Shop, City
from .serializers import CitySerializer, ShopSerializer, ShopCreateSerializer,\
    StreetSerializer
from .service import ShopFilter


class CityView(generics.ListAPIView):
    """Вывод списка городов"""
    queryset = City.objects.all()
    serializer_class = CitySerializer


class ShopView(viewsets.ModelViewSet):
    """Добавление и просмотр магазинов"""

    filter_backends = (DjangoFilterBackend,)
    filterset_class = ShopFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return ShopSerializer
        elif self.action == "create":
            return ShopCreateSerializer

    def get_queryset(self):
        shops = Shop.objects.all()
        open = self.request.query_params.get('open')
        if open == '1':
            # открыт
            shops = Shop.objects.filter(
                opening_time__lte=datetime.now().time(),
                closing_time__gte=datetime.now().time())
        elif open == '0':
            shops = Shop.objects.filter(
                ~(Q(opening_time__lte=datetime.now().time())&
                    Q(closing_time__gte=datetime.now().time())))
        return shops

    def create(self, request, *args, **kwargs):
        # Существует ли указанная улица в Указанном городе
        try:
            Street.objects.get(city=int(request.data.get('city')),
                           id=int(request.data.get('street')))
        except Street.DoesNotExist:
            return Response(data="Улица не найдена в данном Городе",
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class StreetView(generics.ListAPIView):
    """Вывод списка улиц определенного города"""

    serializer_class = StreetSerializer

    def get_queryset(self):
        return Street.objects.filter(city_id=self.kwargs.get('city_id'))