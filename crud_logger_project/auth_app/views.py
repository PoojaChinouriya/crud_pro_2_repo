from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .serializers import UserSerializer
import logging

error_logger = logging.getLogger('error_logger')
success_logger = logging.getLogger('success_logger')


class UserAPI(APIView):
    def person(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            success_logger.info(f"The user with username:{serializer.data.get('username')}created successfully")
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            error_logger.error(f"Error saving yhe user data {serializer.errors}")
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)