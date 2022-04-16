from rest_framework import views, status
from rest_framework.response import Response
from sample_api.serializers import HelloSerializer

class SimpleView(views.APIView):
    
    def get(self, request):
        """
        hello worldを返す
        """
        
        serializer = HelloSerializer()
        message = serializer.get_message()
        return Response({'data': message}, status.HTTP_200_OK)
