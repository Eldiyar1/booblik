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
                serializer.validated_data['full_name'],
                str(serializer.validated_data['phone_number']),
                serializer.validated_data['email'],
                serializer.validated_data['comment']
            )
            return Response({"message": "Feedback has been sent successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
