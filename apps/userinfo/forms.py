# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 20:13
# @Author  : wenzhaoqing

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
import re
User=get_user_model()
from .models import UserInfo

class RegForm(forms.Form):
    username=forms.CharField(
        max_length=20,
        label="用户名",
        error_messages={
            "max_length":"用户名最长20位",
            "require":"用户名不为空"
        },
        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"},
        )
    )

    password=forms.CharField(
        min_length=6,
        max_length=16,
        label="密码",
        error_messages={
            "min_length":"密码最少6位",
            "max_length":"密码最长16位",
            "require":"密码不为空",
        },
        widget=forms.widgets.PasswordInput(
            attrs={"class": "form-control"},
            render_value=True
        ),

    )

    re_password = forms.CharField(
        min_length=6,
        max_length=16,
        label="确认密码",
        widget=forms.widgets.PasswordInput(
            attrs={"class": "form-control"},
            render_value=True,
        ),
        error_messages={
            "min_length": "确认密码至少要6位！",
            "max_length":"密码最多16位",
            "required": "确认密码不能为空",
        }
    )

    def phone_validate(value):
        phone_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
        if not phone_re.match(value):
            raise ValidationError('手机号码格式错误')
        is_exist=User.objects.filter(phone=value)
        if is_exist:
            raise ValidationError("手机号码已经被注册")



    phone=forms.CharField(
            max_length=11,
            min_length=11,
            label="电话号码",
            error_messages={
                "max_length":"电话号码必须为11位",
                "min_length": "电话号码必须为11位",
                "require":"电话号码不为空",
            },
            widget=forms.widgets.EmailInput(
                attrs={"class": "form-control"},
                render_value=True
            ),
            validators=[phone_validate,],

    )

    def clean(self):
        password=self.cleaned_data.get("password")
        re_password=self.cleaned_data.get("re_password")
        if re_password and password != re_password:
            self.add_error("re_password",ValidationError("两次密码不一致"))

        else:
            return self.cleaned_data

    def clean_username(self):
        username=self.cleaned_data.get("username")
        usernameIsExit=UserInfo.objects.filter(username=username)
        if usernameIsExit:
            self.add_error("username",ValidationError("用户名已存在"))
        else:
            return username
