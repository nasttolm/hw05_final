from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group', 'image')
        help_texts = {
            'text': 'Write what you would like to share with other users.',
            'group': ('The group will help prevent the publication of one'
                      'topic in one place.'),
            'image': 'Attach a photo to make your post more interesting.'
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        help_texts = {
            'text': 'Write your comment.',
        }
