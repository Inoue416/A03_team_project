"""
ユーザモデル
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

class UserManager(BaseUserManager):
    """ユーザのオブジェクトマネージャ"""
    
    def create_user(self, name, email, password, **extra_fields):
        # 名無しのハンドル
        if not name:
            raise ValueError('名前が含まれていません')
        # emailなしのハンドル
        if not email:
            raise ValueError('emailが含まれていません。')
        # パスワードなしのハンドル
        if not password:
            raise ValueError('パスワードが設定されていません')
        
                
        user = self.model(name=name, email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        
        # if not (user.is_student ^ user.is_company):
        #     raise ValueError('生徒か企業のどっちかを選んでください')
            
        
        # 生徒と会社どっちも選ばれてない場合のハンドル
        # HACK：ValueErrorというエラーはよろしくない気が
        if user.is_student and user.is_company:
            raise ValueError('生徒か企業のどちらか一つを選んでください')
        
        # HACK：ValueErrorというエラーはよろしくない気が
        # HACK:not (user.is_student or user.is_company)が使えなかったので、下記の条件式に
        if user.is_company == False and user.is_student == False:
            raise ValueError('生徒か企業のどっちか一つだけを選んでください')
        
        user.save(using=self.db)
        
        return user
    
    def create_superuser(self, name, email, password):
        # 名無しのハンドル
        if not name:
            raise ValueError('名前が含まれていません')
        # emailなしのハンドル
        if not email:
            raise ValueError('emailが含まれていません。')
        # パスワードなしのハンドル
        if not password:
            raise ValueError('パスワードが設定されていません')
        
                
        user = self.model(name=name, email=self.normalize_email(email))
        user.set_password(password)
        user.is_superuser = True
        user.save(using=self._db)
        
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    
    """User モデル"""
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_student = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    
    objects = UserManager()
    
    # Django shell用に指定
    # HACK:名前だとuniqueではない。
    USERNAME_FIELD = 'name'
    
    class Meta:
        app_label = 'app'
        