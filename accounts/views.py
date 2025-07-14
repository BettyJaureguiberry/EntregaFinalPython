from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages as django_messages
from .forms import SignUpForm
from .models import Profile, Message
from .forms import ProfileForm

# 📝 Registro con avatar y bio
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            avatar = form.cleaned_data.get('avatar')
            bio = form.cleaned_data.get('bio')
            Profile.objects.create(user=user, avatar=avatar, bio=bio)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

# 👤 Vista del perfil
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/edit_profile.html', {'form': form})

# 💬 Iniciar conversación desde dropdown
@login_required
def start_conversation_view(request):
    users = User.objects.exclude(id=request.user.id)

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        if user_id:
            return redirect('conversation', user_id=user_id)

    return render(request, 'accounts/start_conversation.html', {'users': users})

# 📥 Conversación privada uno-a-uno
@login_required
def conversation_view(request, user_id):
    contact = User.objects.get(id=user_id)

    messages = Message.objects.filter(
        sender__in=[request.user, contact],
        receiver__in=[request.user, contact]
    ).order_by('timestamp')

    messages.filter(receiver=request.user, is_read=False).update(is_read=True)

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(
                sender=request.user,
                receiver=contact,
                content=content,
                is_read=False
            )
            django_messages.success(request, "📨 ¡Mensaje enviado con glow rebelde!")
            return redirect('conversation', user_id=contact.id)

    return render(request, 'accounts/conversation.html', {
        'contact': contact,
        'messages': messages,
        'user': request.user
    })