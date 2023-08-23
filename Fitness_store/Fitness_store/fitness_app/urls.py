from django.urls import path, include

from Fitness_store.fitness_app.views import HomePageView, AboutUsPageView, SupplementsPageView, GymEquipmentPageView, \
    ContactsPageView, ProfileLoginView, EquipmentProductPageView, SupplementProductPageView, \
    RegisterUserView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('about-us/', AboutUsPageView.as_view(), name='about us'),
    path('supplements/', SupplementsPageView.as_view(), name='supplements'),
    path('gym-equipment/', GymEquipmentPageView.as_view(), name='gym equipment'),
    path('contact/', ContactsPageView.as_view(), name='contacts'),
    path('equipment_product/', EquipmentProductPageView.as_view(), name='equipment_product'),
    path('supplement_product', SupplementProductPageView.as_view(), name='supplement_product'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', ProfileLoginView.as_view(), name='login'),
]
