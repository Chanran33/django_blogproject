from django import forms
from django.forms import fields
from django.forms.widgets import Widget
from .models import Blog #모델에 맞는 데이터 형식의 form을 사용하기 위해서 import

class BlogForm(forms.ModelForm):#장고에서 지원해주는 forms 상속 받음
    class Meta: #일종의 이름표 역할! 아래의 정보를 가지고 BlogForm을 만들어주겟다!
        model = Blog
        fields = ['title', 'writer', 'body', 'image']

    title = forms.CharField(
        label="제목",
        widget=forms.TextInput(
            attrs={
                'placeholder' : ''
            }
        )
    )

    writer = forms.CharField(
        label="작성자",
        widget=forms.TextInput(
            attrs={
                'class': 'col-sm-4',
                "placeholder" : ""
            }
        )
    )

    body = forms.CharField(
        label="가사",
        widget=forms.Textarea(
            attrs={
                "placeholder" : ""
            }
        )
    )

    image = forms.ImageField(
        label="이미지 업로드"
    )



