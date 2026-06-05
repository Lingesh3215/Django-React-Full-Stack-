from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import RoleModel,UserModel,NewsModel
from .serializers import UserS, NewsS
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication, JWTStatelessUserAuthentication
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
class Login(APIView):
    #authentication_classes=[JWTAuthentication]
    def post(self,request,*args,**kwargs):
        email=request.data.get('email')
        password=request.data.get('password')
        if not password:
            return Response({'error': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_400_BAD_REQUEST)

        #if not user.check_password(password):
        if not user.password==password:
            return Response({'error': 'Invalid password.'}, status=status.HTTP_401_UNAUTHORIZED)

        #refresh = RefreshToken.for_user(user)
        token = str(AccessToken.for_user(user))
        return Response({'token': token}, status=status.HTTP_201_CREATED)
    

class Register(APIView):
    # def post(self, request, *args, **kwargs):
    #     username = request.data.get('username')
    #     email = request.data.get('email')
    #     password = request.data.get('password')
    #     role = request.data.get('role')

    #     if not username or not email or not password or not role:
    #         return Response({'error': 'Missing required fields.'}, status=400)

    #     if UserModel.objects.filter(email=email).exists():
    #         return Response({'error': 'Email already registered.'}, status=400)

    #     try:
    #         qs = RoleModel.objects.get(id=role)
    #     except RoleModel.DoesNotExist:
    #         return Response({'error': 'Invalid role.'}, status=400)

    #     UserModel.objects.create(
    #         username=username, email=email, password=password, role=qs
    #     )
        # return Response({'message': 'User registered.'}, status=201)
    def post(self,request,*args,**kwargs):
        s1=UserS(data=request.data)
        if s1.is_valid():
            s1.save()
            return Response('user registered',status=201)
        else:
            return Response(s1.errors,status=400)

        
    
class NewsListPost(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def post(self,request,*args,**kwargs):
        if not request.user or request.user.role.role_name!='reporter':
            return Response(status=403)
        s1=NewsS(data=request.data)
        if s1.is_valid():
            s1.save(author=request.user)
            return Response(s1.data,status=201)
        else:
            return Response(s1.errors,status=400)
    

    def get(self,request,*args,**kwargs):
        try:
            qs=NewsModel.objects.all()
            category = request.query_params.get("category")
            if category:
                qs = qs.filter(category=category)

        # ✅ Optional sorting (test31)
            sort = request.query_params.get("sort")
            if sort == "asc":
                qs = qs.order_by("id")
            elif sort == "desc":
                qs = qs.order_by("-id")

        except:
            return Response(status=400)
        s1=NewsS(qs,many=True)
        return Response(s1.data,status=200)
    
class NewsRetrieve(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def get(self,request,id):
        try:
            qs=NewsModel.objects.get(pk=id)
        except:
            return Response(status=404)
        s1=NewsS(qs)
        return Response(s1.data,status=200)
    


    def put(self,request,id,*args,**kwargs):
        if not request.data:
            return Response(status=400)
        try:
            qs=NewsModel.objects.get(pk=id)
        except:
            return Response(status=404)
        if qs.author!=request.user:
            return Response(status=403)
        s1=NewsS(qs,data=request.data)
        if s1.is_valid():
            s1.save()
        return Response(s1.data,status=200)
    
    def patch(self,request,id,*args,**kwargs):
        
        try:
            qs=NewsModel.objects.get(pk=id)
        except:
            return Response(status=404)
        if qs.author!=request.user:
            return Response(status=403)
        s1=NewsS(qs,data=request.data,partial=True)
        if s1.is_valid():
            s1.save()
        return Response(s1.data,status=200)
    


    def delete(self,request,id,*args,**kwargs):
        
        try:
            qs=NewsModel.objects.get(pk=id)
        except:
            return Response(status=404)
        if qs.author!=request.user:
            return Response(status=403)
        qs.delete()
        return Response(status=204)