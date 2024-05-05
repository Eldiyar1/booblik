from rest_framework.response import Response

from .tasks import send_resume_email
from rest_framework.views import APIView
from rest_framework import status, generics
from .models import Vacancy
from .serializers import VacancyListSerializer, VacancyDetailSerializer, ResumeSerializer


class VacancyListView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer


class VacancyDetailView(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyDetailSerializer


class SendResumeView(APIView):
    serializer_class = ResumeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            resume_content = request.FILES.get('resume').read() if request.FILES.get('resume') else None
            resume_name = request.FILES.get('resume').name if request.FILES.get('resume') else None

            send_resume_email.delay(
                full_name=serializer.validated_data['full_name'],
                phone_number=str(serializer.validated_data['phone_number']),
                birth_date=serializer.validated_data.get('birth_date'),
                resume_content=resume_content,
                resume_name=resume_name
            )
            return Response({"message": "Резюме было успешно отправлено."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
