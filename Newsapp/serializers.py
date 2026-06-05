from rest_framework.serializers import ModelSerializer

from .models import UserModel, NewsModel, RoleModel

class UserS(ModelSerializer):
    class Meta:
        model=UserModel
        fields='__all__'
        #read_only_fields=['role']
        #extra_kwargs={'password':{'write_only':True}}
        # def create(self,validated_data):
        #     password=validated_data.pop('password')
        #     owner=UserModel(**validated_data)
        #     owner.set_password(password)
        #     owner.save()
        #     return owner
class NewsS(ModelSerializer):
    class Meta:
        model=NewsModel
        fields='__all__'
        read_only_fields=['author']
        

class RoleS(ModelSerializer):
    class Meta:
        model=RoleModel
        fields='__all__'
        read_only_fields=[]