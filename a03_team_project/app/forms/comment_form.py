from django import forms
from app.models.comment import Comment
from app.models.user import User
from app.models.markdown_post import MarkdownPost

class CommentForm(forms.Form):
    markdown_id = forms.IntegerField(widget=forms.HiddenInput, required=True)
    comment = forms.CharField(widget=forms.Textarea(), required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs['rows'] = 3
        self.fields['comment'].widget.attrs['class'] = 'form-control mb-3'
        self.fields['markdown_id'].widget.attrs['id'] = 'markdown-id'
    
    def save(self, user_id):
        data = self.cleaned_data
        comment = Comment(markdown=MarkdownPost.objects.get(id=data['markdown_id']),
                          user=User.objects.get(id=user_id), 
                          comment=data['comment'])
        comment.save()
        print('Save comment in comment table.')


