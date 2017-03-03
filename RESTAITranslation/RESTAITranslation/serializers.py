from rest_framework import serializers
from RESTAITranslation.RESTAITranslation.models import Translation
from RESTAITranslation.RESTAITranslation.models import Algorithm

class TranslationSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')    
    # translatedText = serializers.HyperlinkedIdentityField(view_name='translation-translatedText')

    class Meta:
        model = Translation
        fields = ('url', 'id', 'originalText', 'translatedText',
                  'sourceLanguage', 'targetLanguage', 'algorithmId', 'algorithmName', 'score', 'suggestedAnswer', 'algorithmReload')


class AlgorithmSerializer(serializers.HyperlinkedModelSerializer):    

    class Meta:
        model = Algorithm
        fields = ('url', 'id', 'algorithmId', 'algorithmName', 'algorithmDescription','algorithmAlias','algorithmPath')