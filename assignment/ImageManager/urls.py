from django.urls import path
from .views import ImageView, PeopleAutocompleteView

urlpatterns = [
    path('upload/', ImageView.as_view({'post': 'create'}), name='image-upload'),
    path('list/', ImageView.as_view({'get': 'get_list'}), name='image-list'),
    path('image/<int:id>', ImageView.as_view({'get': 'get_image'}), name='image-get'),
    path('people_autocomplete/<str:name>', PeopleAutocompleteView.as_view(), name='people-autocomplete'),
]
