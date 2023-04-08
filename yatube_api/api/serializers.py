from rest_framework import serializers

from posts.models import Comment, Post, Follow, Group, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        required=False
    )

    class Meta:
        fields = '__all__'
        model = Post
        read_only_fields = ('author',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        required=False
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('author', 'post')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        required=False
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        required=True
    )

    class Meta:
        fields = '__all__'
        model = Follow
        read_only_fields = ('user',)

    def validate(self, data):
        user = data.get('following')

        if user == self.context['request'].user:
            raise serializers.ValidationError(
                'Вы не можете подписаться на самого себя'
            )

        if Follow.objects.filter(user=self.context['request'].user,
                                 following=user).exists():
            raise serializers.ValidationError(
                'Вы уже подписаны на данного пользователя'
            )

        return data


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group
