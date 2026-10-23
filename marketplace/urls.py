from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CropViewSet, MarketViewSet, PriceEntryViewSet, SignupView

router = DefaultRouter()
router.register('crops', CropViewSet)
router.register('markets', MarketViewSet)
router.register('prices', PriceEntryViewSet)

urlpatterns = router.urls + [
    path('signup/', SignupView.as_view()),
]