from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import UserProfile
from .serializers import UserProfileSerializer
from django.db.models import Q  # For search functionality

@api_view(['GET'])
def get_users(request):
    """Fetch all users or filter by search term"""
    search_query = request.query_params.get('search', None)
    users = UserProfile.objects.all()

    if search_query:
        users = users.filter(Q(name__icontains=search_query) | Q(email__icontains=search_query))

    serializer = UserProfileSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user_by_id(request, user_id):
    """Fetch a single user by ID"""
    user = get_object_or_404(UserProfile, id=user_id)
    serializer = UserProfileSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    """Create a new user"""
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_user(request, user_id):
    """Update user details"""
    user = get_object_or_404(UserProfile, id=user_id)
    serializer = UserProfileSerializer(user, data=request.data, partial=True)  # Partial update allowed
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request, user_id):
    """Delete a user"""
    user = get_object_or_404(UserProfile, id=user_id)
    user.delete()
    return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
