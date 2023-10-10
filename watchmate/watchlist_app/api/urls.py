from django.urls import path, include
from watchlist_app.api.views import ReviewCreate , StreamPlatformAV ,StreamPlatformDetailAV,ReviewDetail,ReviewList

urlpatterns = [
    # path('list/', MovieListAV.as_view() , name = 'movie-list'),
    # path('<int:pk>',MovieDetail.as_view() , name='movie-details'),
    
    # path('stream/', StreamPlatformAV.as_view(), name = 'stream-list'),
    # path('<int:pk>' , StreamPlatformDetailAV.as_view() , name = 'stream-detail'),
    
    # path('review', ReviewList.as_view() , name = 'review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name ='review-detail'),
    
    path('<int:pk>/review-create', ReviewCreate.as_view() , name = 'review-create'),
    path('<int:pk>/review', ReviewList.as_view() , name = 'review-list'),
    path('<int:pk>', ReviewDetail.as_view(), name ='review-detail')
]
