from rest_framework import serializers
from watchlist_app.models import   StreamPlatform , WatchList ,Review

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only = True)
    
    class Meta:
        model = Review
        fields = "__all__"

# class MovieSerializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name' , instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active = validated_data.get('activate', instance.active)
#         instance.save()
#         return instance

class WatchListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WatchList
        fields  = '__all__'

class StreamPlatformSerilizer(serializers.ModelSerializer):
    
    # watchlist = WatchListSerializer(many=True, read_only=True)
    watchlist = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = StreamPlatform
        fields  = '__all__'
        

