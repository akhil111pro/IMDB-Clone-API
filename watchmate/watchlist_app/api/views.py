from watchlist_app.models import StreamPlatform ,Review ,WatchList
from watchlist_app.api.serilizers import  StreamPlatformSerilizer,ReviewSerializer,WatchListSerializer
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError 
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.all()
        
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk = pk)
        
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist = watchlist , review_user = review_user)
        
        if review_queryset.exists():
            raise ValidationError("you have already reviewed this movie or watch list!")
        
        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating =(watchlist.avg_rating + serializer.validated_data['rating'] )/2
            
            
        serializer.save(watchlist = watchlist , review_user = review_user)

class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist = pk)
    
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
# class ReviewDetail(mixins.RetrieveModelMixin , generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
    
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
class StreamPlatformAV(APIView):

    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerilizer(platform, many=True)
        return Response(serializer.data)

    def post(self, request):
        serilizer = StreamPlatformSerilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        else:
            return Response(serilizer.error_messages)


class StreamPlatformDetailAV(APIView):

    def get(self, request, pk):
        detail = StreamPlatform.objects.get(pk=pk)
        serilizer = StreamPlatformSerilizer(detail)

        return Response(serilizer.data)


# class MovieListAV(APIView):
#     def get(self, request):
#         movies = Movie.objects.all()
#         serilizer = MovieSerializers(movies, many=True)
#         return Response(serilizer.data)

#     def post(self, request):
#         serilizer = MovieSerializers(data=request.data)
#         if serilizer.is_valid():
#             serilizer.save()
#             return Response(serilizer.data)
#         else:
#             return Response(serilizer.errors)


# class MovieDetail(APIView):
#     def get(self, request, pk):
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error': 'movie not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = MovieSerializers(movie)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         movie = Movie.objects.get(pk=pk)
#         serilizer = MovieSerializers(movie, data=request.data)
#         if serilizer.is_valid():
#             serilizer.save()
#             return Response(serilizer.data)
#         else:
#             return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serilizer = MovieSerializers(movies , many=True)
#         print(serilizer.data)
#         return Response(serilizer.data)

#     if request.method == 'POST':
#         serilizer = MovieSerializers(data=request.data)
#         if serilizer.is_valid():
#             serilizer.save()
#             return Response(serilizer.data)
#         else:
#             return Response(serilizer.errors)


# @api_view(['GET','PUT','DELETE'])
# def movie_details(request , pk):

#     if request.method == 'GET':
#         movie = Movie.objects.get(pk = pk)
#         serilizer = MovieSerializers(movie)
#         return Response(serilizer.data)

#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serilizer = MovieSerializers(movie,data = request.data)
#         if serilizer.is_valid():
#             serilizer.save()
#             return Response(serilizer.data)
#         else:
#             return Response(serilizer.errors , status=status.HTTP_400_BAD_REQUEST)


#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
