from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from app.models.nice import Nice
from app.models.markdown_post import MarkdownPost
from app.models.user import User

class NiceView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        data = request.data
        is_nice = Nice.objects.filter(
            markdown=MarkdownPost.objects.get(id=data['markdown_id']), 
            user=User.objects.get(id=request.user.id)
        ).first()
        message = ""
        if not is_nice:
            nice_data = Nice(
                markdown=MarkdownPost.objects.get(id=data['markdown_id']),
                user=User.objects.get(id=request.user.id)
            )
            nice_data.save()
            message = "Save nice."
        else:
            Nice.objects.filter(
                markdown=MarkdownPost.objects.get(id=data['markdown_id']),
                user=User.objects.get(id=request.user.id)
            ).delete()
            message = "Delete nice."
        nice_num = Nice.objects.filter(markdown=MarkdownPost.objects.get(id=data['markdown_id'])).count()
        return Response({"status": "200", "message": message, "nice_num": nice_num})
