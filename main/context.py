from django.contrib.auth import get_user


def navbar_template(request):
    user = get_user(request)
    return {'navbar_template': 'membersnavbar.html' if user.is_authenticated else 'navbar.html'}
