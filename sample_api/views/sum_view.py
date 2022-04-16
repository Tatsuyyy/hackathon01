from rest_framework import views, status
from rest_framework.response import Response
from sample_api.serializers import SumSerializer

class SumView(views.APIView):
    def post(self, request):
        """
        数字を2つ受け取り、足し算した結果を返す
        
        num1: int  
        num2: int
        """

        serializer = SumSerializer()
        sum = serializer.sum(request.data['num1'], request.data['num2'])
        return Response({'data': {'sum': sum}}, status.HTTP_200_OK)