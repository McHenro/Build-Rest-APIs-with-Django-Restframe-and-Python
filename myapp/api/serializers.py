from rest_framework import serializers
from myapp.models import WatchList, StreamPlatForm, Review


class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'
        


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many = True, read_only = True)
    # len_name = serializers.SerializerMethodField()
    class Meta:
        model = WatchList
        fields = '__all__'
 
# Using HyperlinkedModelSerializer
# class StreamPlatFormSerializer(serializers.HyperlinkedModelSerializer):
#     watchlist = WatchListSerializer(many = True, read_only = True)
        
# Using ModelSerializer
class StreamPlatFormSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many = True, read_only = True)
    
    # Using Nested serializer
    # watchlist = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    # watchlist = serializers.StringRelatedField(many = True, read_only = True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie-detail'
    # )
    
    class Meta:
        model = StreamPlatForm
        fields = '__all__'
        
        
        
        
        
        
    # def get_len_name(self, object):
    #     obj_name = object.name
    #     return len(obj_name)

    # def validate_name(self, value):
    #     if len(value) < 3:
    #         raise serializers.ValidationError('name must be at least 3 characters')
    #     return value
    
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError('name and description must not be the same')
    #     return data


# def name_length(value):
#     if len(value) < 3:
#         raise serializers.ValidationError('name must be at least 3 characters')
#     return value


# Using serializers.Serializer#
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     # def validate_name(self, value):
#     #     if len(value) < 3:
#     #         raise serializers.ValidationError('name must be at least 3 characters')
#     #     return value
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('name and description must not be the same')
#         return data
        
        
