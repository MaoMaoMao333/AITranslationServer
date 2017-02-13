from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from RESTAITranslation.RESTAITranslation.models import Translation
from RESTAITranslation.RESTAITranslation.serializers import TranslationSerializer
from RESTAITranslation.RESTAITranslation.models import Algorithm
from RESTAITranslation.RESTAITranslation.serializers import AlgorithmSerializer

from rest_framework import generics

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'translations': reverse('translation-list', request=request, format=format),
        'algorithms': reverse('algorithm-list', request=request, format=format)
    })

class TranslationList(generics.ListCreateAPIView):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer


class TranslationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer


# class TranslatedText(generics.GenericAPIView):
#     queryset = Translation.objects.all()
#     # renderer_classes = (renderers.StaticHTMLRenderer,)

#     def get(self, request, *args, **kwargs):
#         translation = self.get_object()
#         return Response(translation.translatedText)

class AlgorithmList(generics.ListCreateAPIView):
    queryset = Algorithm.objects.all()
    serializer_class = AlgorithmSerializer


class AlgorithmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Algorithm.objects.all()
    serializer_class = AlgorithmSerializer

        