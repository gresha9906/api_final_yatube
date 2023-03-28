from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('author', 'post',)
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = Follow
        fields = '__all__'
        # Так было бы лучше, но не получается
        # переопределить user
        # validators = [
        #         UniqueTogetherValidator(
        #             queryset=Follow.objects.all(),
        #             fields=['user', 'following']
        #         )
        # ]

    def validate(self, data):
        user = self.context['request'].user
        following = data['following']
        is_unique = Follow.objects.filter(user=user, following=following)
        if user == following:
            raise serializers.ValidationError(
                'Нельзя подписаться на себя.'
            )
        if len(is_unique) != 0:
            raise serializers.ValidationError(
                'Второй раз нельзя подписаться'
            )
        return data


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'
