from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from common.models import Profile
from zerowaste.forms import ArticleForm





# 회원가입
def signup(request):
    # 복사
    if request.method == 'POST':
        form_1 = ArticleForm(request.POST)
        if form_1.is_valid():
            article = form_1.save()
            return redirect('/')
    else:
        form_1 = ArticleForm()
    # 복사
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            Profile.objects.create(user=signed_user)

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('/owaste/index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form, 'form_1' : form_1})

# 프로필
@login_required
def profile(request):
    # 복사
    if request.method == 'POST':
        form_1 = ArticleForm(request.POST)
        if form_1.is_valid():
            article = form_1.save()
            return redirect('/')
    else:
        form_1 = ArticleForm()
    # 복사
    return render(request, "common/profile.html", {'form_1' : form_1})

# 비밀번호 변경
@login_required
def change_password(request):
    # 복사
    if request.method == 'POST':
        form_1 = ArticleForm(request.POST)
        if form_1.is_valid():
            article = form_1.save()
            return redirect('/')
    else:
        form_1 = ArticleForm()
    # 복사
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/owaste/index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'common/change_password.html', {
        'form': form, 'form_1' : form_1
    })