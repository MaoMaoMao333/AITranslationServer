from __future__ import unicode_literals

from django.db import models
from RESTAITranslation.RESTAITranslation.algorithms import Algorithms 

class Translation(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    originalText = models.TextField()
    translatedText = models.TextField(blank=True)
    sourceLanguage = models.CharField(max_length=200, default='Chinese')
    targetLanguage = models.CharField(max_length=200, default='English')
    algorithmId = models.BigIntegerField()
    algorithmName = models.CharField(max_length=200, default='')
    score = models.IntegerField(default=-1)
    suggestedAnswer = models.TextField(blank=True)
    algorithmReload = models.NullBooleanField()

    def save(self, *args, **kwargs):
        algorithm = Algorithms()
        self.translatedText = algorithm.translate(self.algorithmName, self.algorithmId, self.originalText, self.algorithmReload)
        super(Translation, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created',)

class Algorithm(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    algorithmId = models.BigIntegerField()
    algorithmName = models.CharField(max_length=200, default='')
    algorithmDescription = models.TextField()
    algorithmAlias = models.CharField(max_length=200, default='')
    algorithmPath = models.TextField()

    class Meta:
        ordering = ('algorithmId',)
