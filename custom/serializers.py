from djoser.serializers import UserSerializer as BaseSerializer, UserCreateSerializer as BaseUserCreateSerializer


class UserSerializer(BaseSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        ref_name = 'User1'


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
