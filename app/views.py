from django.shortcuts import render
from .models import Session, Character, Location, UserProfile
from rest_framework import generics
from .serializers import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.validators import validate_email
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .serializers import LoginSerializer
ensure_csrf = method_decorator(ensure_csrf_cookie, name='dispatch')
csrf_protect_method = method_decorator(csrf_protect, name='dispatch')

#Session return all & return specific
class SessionList(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class SessionDetail(generics.RetrieveUpdateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

#Character return all & return specific
class CharacterList(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharactersSerializer

class CharacterDetail(generics.RetrieveUpdateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharactersSerializer

#Location return all & return specific
class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetail(generics.RetrieveUpdateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

# Set CSRF cookie API call
class setCSRFCookie(APIView):
    permission_classes = [AllowAny,]
    authentication_classes = []
    @ensure_csrf
    def get(self, request):
        return Response({ 'success': 'CSRF Cookie set.'})

#Login API call
@csrf_protect_method    
class LoginView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()   
    def post(self, request):
        data = self.request.data

        username = data['username']
        password = data['password']
        try:
            user = authenticate(username=username, password=password)

            if (user is not None):
                login(request, user)
                return Response({ 'success': 'User authenticated', 'username': username})
            else:
                return Response({ 'error': 'Error Authenticating'})
        except:
            return Response({'error': 'Something went wrong logging in'})
        
#Logout API call        
class LogoutView(APIView):
    def post(self, request, format=None):
        try:
            logout(request)
            return Response({ 'success': 'Logged Out'})
        except:
            return Response({'error': 'Something went wrong when logging out'})

#SignUp API Call
@csrf_protect_method    
class SignupView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        data = self.request.data

        username = data['username']
        email = data['email']
        password = data['password']
        re_password = data['re_password']
        try:
            try:
                validate_email(email)
            except:
                return Response({'error': 'Invalid email format'})
            if (password == re_password):
                if User.objects.filter(username=username).exists():
                    return Response({'error': 'Username already exists'})
                else:
                    if (len(password) < 6):
                        return Response({ 'error': 'Password length must atleast 6 characters'})
                    else:
                        user = User.objects.create_user(username=username, password=password, email=email)
                        user.save()
                        user = User.objects.get(id=user.id)
                        user_profile = UserProfile(user=user, first_name='', last_name='', email=email)
                        user_profile.save()
                        return Response({ 'success': 'User created successfully'})
            else:
                return Response({'error': 'Password do not match'})
        except:
            return Response({'error': 'Something went wrong when registering an account.'})
        
#Is current session Authenticated API call        
@csrf_protect_method
class CheckAuthenticatedView(APIView):
    def get(self, request, format=None):
        try:
            isAuthenticated = User.is_authenticated

            if isAuthenticated:
                return Response({ 'isAuthenticated': 'success'})
            else:
                return Response({ 'isAuthenticated': 'error'})
        except:
            return Response({'error': 'Something went wrong verifying authentication status'})
        
class DeleteAccountView(APIView):
    def delete(self, request):
        user = self.request.user

        try:
            user = User.objects.filter(id=user.id).delete()
            return Response({ 'success': 'User deleted'})
        except:
            return Response({ 'error': 'Something went wrong when trying to delete user'})