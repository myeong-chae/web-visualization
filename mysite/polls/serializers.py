#product/serializers.py
from rest_framework import serializers
from .models import Product, Data

class ProductSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Product        # product 모델 사용
        fields = '__all__'            # 모든 필드 포함


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'