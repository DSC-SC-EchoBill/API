from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Receipt, VerifyCodes, Device


# -----------------------------------------------------------
# 회원관리
# 회원가입
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"], password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"]
        )
        return user


# 접속 유지중인가 확인
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


# 로그인
class SigninSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")


# 비밀번호 찾기
class SearchPWSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyCodes
        fields = ('email', 'verify_code')


# 디바이스 추가
class SignupDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = 'brand_name',


# -----------------------------------------------------------
# 영수증 관리
# 영수증 tuple을 생성하는 시리얼라이저
class CreateReceiptTupleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ('receipt_img_url', 'receipt_img_uri', 'device_id')


# 생성된 영수증 tuple에 사용자를 추가하는 시리얼라이저
class CheckUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = '__all__'


# 서버에서 받아온 영수증주소 투플생성
class NewReceiptURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ('id', 'user', 'receipt_img_url', 'device_id')

    def create(self, validated_data):
        receipt = Receipt.objects.create(
            user=validated_data["user"], receipt_img_url=validated_data["receipt_img_url"],
            device_id=validated_data["device_id"]
        )
        return receipt


# -----------------------------------------------------------
# 영수증 리스트 반환
# 선택한 날짜와 시간의 맞는 영수증 이미지리스트
class ReceiptDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ('id', 'user', 'receipt_img_url', 'receipt_date', 'total_price', 'device_id')
