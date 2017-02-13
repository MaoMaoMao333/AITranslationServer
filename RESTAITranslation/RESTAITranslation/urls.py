# from django.conf.urls import url, include
# from rest_framework.urlpatterns import format_suffix_patterns
# from RESTAITranslation import views

# # API endpoints
# urlpatterns = format_suffix_patterns([
#     url(r'^$', views.api_root),
#     url(r'^translations/$',
#         views.TranslationList.as_view(),
#         name='translation-list'),
#     url(r'^translations/(?P<pk>[0-9]+)/$',
#         views.TranslationDetail.as_view(),
#         name='translation-detail'),
#     url(r'^translations/(?P<pk>[0-9]+)/translatedText/$',
#         views.TranslatedText.as_view(),
#         name='translation-translatedText'),
#     url(r'^algorithms/$',
#         views.AlgorithmList.as_view(),
#         name='algorithm-list'),
#     url(r'^algorithms/(?P<pk>[0-9]+)/$',
#         views.AlgorithmDetail.as_view(),
#         name='algorithm-detail')
# ])

# # Login and logout views for the browsable API
# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls',
#                                namespace='rest_framework')),
# ]