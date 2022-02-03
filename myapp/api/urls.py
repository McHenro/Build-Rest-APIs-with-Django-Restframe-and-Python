from django.urls import path, include

# from myapp.api.views import movie_list, movie_details
from myapp.api.views import (
    ReviewList,
    ReviewDetail,
    ReviewCreate,
    WatchListAV,
    WatchDetailsAV,
    StreamPlatFormListAV,
    StreamPlatFormVS,
    StreamPlatFormDetailAV,
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("stream", StreamPlatFormVS, basename="streamplatform")


urlpatterns = [
    path("list/", WatchListAV.as_view(), name="movie-list"),
    path("<int:pk>", WatchDetailsAV.as_view(), name="movie-detail"),
    
    # using rounter
    path("", include(router.urls)),
    
    # using API view
    # path('stream/', StreamPlatFormListAV.as_view(), name='stream'),
    # path('stream/<int:pk>', StreamPlatFormDetailAV.as_view(), name='stream-detail'),
    
    # # using Mixins alongside GenericAPIView
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    
    # URL structure
    path("stream/<int:pk>/review-create", ReviewCreate.as_view(), name="review-create"),
    path("stream/<int:pk>/review", ReviewList.as_view(), name="stream-detail"),
    path("stream/review/<int:pk>", ReviewDetail.as_view(), name="review-detail"),
]
