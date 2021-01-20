from django.urls import path, include
from users import views
from rest_framework.routers import SimpleRouter



router = SimpleRouter()
router.register(r'all', views.UserViewSet)
router.register(r'requests', views.MatchRequestViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('list/', include(router.urls)),
    path('proposals/', views.MatchProposalsView.as_view()),
    path('matches/', views.MatchedUsersView.as_view())
]
