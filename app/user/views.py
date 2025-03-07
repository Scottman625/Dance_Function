from modelCore.models import User 
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import viewsets, mixins

from user.serializers import UserSerializer, AuthTokenSerializer, UpdateUserSerializer ,GetUserSerializer, UserLicenceImageSerializer
from django.db.models import Q

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer

    def perform_create(self, serializer,):
        user = serializer.save(user=self.request.user)
        return user

#http://localhost:8000/api/user/token/  要用 post, 並帶參數
class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

#http://localhost:8000/api/user/me/  要有 token
class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UpdateUserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication user"""
        # if self.request.user.line_id != None and self.request.user.line_id != '':
        #     self.request.user.is_gotten_line_id = True
        
        #total_unread_num

        return self.request.user

class UpdateUserLineIdView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)

    def put(self, request, format=None):
        try:
            # print(self.request.user)
            # print(self.request.data.get('line_id'))
            user = self.request.user
            user.line_id = self.request.data.get('line_id')
            user.save()
            return Response({'message': 'success update!'})
        except Exception as e:
            raise APIException("wrong token or null line_id")

class UpdateUserPassword(APIView):
    authentication_classes = (authentication.TokenAuthentication,)

    def put(self, request, format=None):
        user = self.request.user
        old_password = self.request.data.get('old_password')

        if user.check_password(old_password):
            new_password = self.request.data.get('new_password')
            user.set_password(new_password)
            user.save()
            return Response({'message': 'success update!'})
        else:
            raise APIException("wrong old password")

class UpdateATMInfo(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, format=None):
        user = self.request.user
        user.ATMInfoBankCode = request.data.get('ATMInfoBankCode')
        user.ATMInfoBranchBankCode = request.data.get('ATMInfoBranchBankCode')
        user.ATMInfoAccount = request.data.get('ATMInfoAccount')
        user.save()
        serializer = GetUserSerializer(user)
        return Response(serializer.data)


class UpdateUserCareType(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, format=None):
        user = self.request.user
        is_home = eval(request.data.get('is_home'))
        is_hospital = eval(request.data.get('is_hospital'))
        home_wage = request.data.get('home_wage')
        hospital_wage = request.data.get('hospital_wage')
        if is_home == True:
            user.is_home = True 
        elif is_home == False: 
            user.is_home = False
        if home_wage != None:
            home_wage = home_wage.split(',')
            user.home_hour_wage = int(home_wage[0])
            user.home_half_day_wage = int(home_wage[1])
            user.home_one_day_wage = int(home_wage[2])
        if is_hospital == True:
            user.is_hospital = True 
        elif is_hospital == False: 
            user.is_hospital = False
        if hospital_wage != None:
            hospital_wage = hospital_wage.split(',')
            user.hospital_hour_wage = hospital_wage[0]
            user.hospital_half_day_wage = hospital_wage[1]
            user.hospital_one_day_wage = hospital_wage[2]
        user.save()
        serializer = GetUserSerializer(user)
        return Response(serializer.data)


class UpdateUserBackgroundImage(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, format=None):
        user = self.request.user

        background_image = request.data.get('background_image')
        if background_image != None:
            user.background_image = background_image
            
        user.save()
        serializer = GetUserSerializer(user)
        return Response(serializer.data)

class UpdateUserImage(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, format=None):
        user = self.request.user
        image = request.data.get('image')
        if image != None:
            user.image = image
        user.save()
        serializer = GetUserSerializer(user)
        return Response(serializer.data)

class GetUpdateUserFCMNotify(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        user = self.request.user
        return Response({'is_fcm_notify':user.is_fcm_notify})

    def put(self, request, format=None):
        user = self.request.user
        is_fcm_notify = request.data.get('is_fcm_notify')
        if is_fcm_notify =='true' or is_fcm_notify =='True':
            user.is_fcm_notify = True
        else:
             user.is_fcm_notify = False
        user.save()
        return Response({'message':'ok'})

class DeleteUser(generics.DestroyAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # lookup_field = 'pk'
    def delete(self, request, pk, format=None):
        
        auth_user = self.request.user
        user = User.objects.get(id=pk)
        if user == auth_user:
            if qualifications_to_delete_user(user) == False:
                return Response("continuous order exists")
            else:
                user.delete()
                return Response('delete user')
        else:
            return Response('not auth')

def qualifications_to_delete_user(user):
    for order in user.user_orders.all():
        if order.case.state == 'unComplete':
            return False
    for order in user.servant_orders.all():
        if order.case.state == 'unComplete':
            return False