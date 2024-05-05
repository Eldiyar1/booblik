from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FeedbackSerializer
from .tasks import send_feedback_email


class FeedbackAPIView(APIView):
    serializer_class = FeedbackSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            send_feedback_email.delay(
                full_name=serializer.validated_data['full_name'],
                phone_number=str(serializer.validated_data['phone_number']),
                comment=serializer.validated_data['comment'],
                filial=serializer.validated_data['filial_id'].id
            )
            return Response({"message": "Отзыв был успешно отправлен"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
