from rest_framework.generics import get_object_or_404
from rest_framework import status
from users.serializers import UserSerializer ,CustomTokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from users.models import MyUser

from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.
#회원가입
class SignUp(APIView):
    def post(self,request):
        serializer= UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": f"{serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
    

#로그인
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

#로그인후
class UserView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    #자신의정보보기
    def get(self,request):
        user = get_object_or_404(MyUser,id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    #업데이트
    def put(self,request):
        user = get_object_or_404(MyUser,id=request.user.id)
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"수정완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
    #삭제
    def delete(self,request):
        user = get_object_or_404(MyUser,id=request.user.id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

