from django.urls import path
# from myapp.api.views import movie_list, movie_details
from myapp.api.views import (ReviewList, ReviewDetail, WatchListAV, 
                             WatchDetailsAV, StreamPlatFormListAV, 
                             StreamPlatFormDetailAV)

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailsAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatFormListAV.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatFormDetailAV.as_view(), name='stream-detail'),
    
    # using Mixins alongside GenericAPIView
    path('review/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),   
    
    # URL structure
    # path('stream/<int:pk>/review', StreamPlatFormDetailAV.as_view(), name='stream-detail'),
    # path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    
]
