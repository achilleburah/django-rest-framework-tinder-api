from django.urls import path, include
from users import views
from rest_framework.routers import SimpleRouter



router = SimpleRouter()
router.register(r'', views.MatchRequestViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('requests/', include(router.urls)),
    path('new/', views.CustomUserView.as_view()),
    path('proposals/', views.MatchProposalsView.as_view()),
    path('matches/', views.MatchedUsersView.as_view())
]
