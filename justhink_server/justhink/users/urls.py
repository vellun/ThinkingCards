import django.urls

import users.views

app_name = "users"

urlpatterns = [
    django.urls.path(
        "<str:uid>/",
        users.views.UserInfoView.as_view(),
        name="user-info",
    ),
]
