from django.urls import path

# Views
from .views import PetDateListCreateAPIView, PetDateRetrieveUpdateDestroyAPIView, PetOwnersListCreateAPIView, PetsListCreateAPIView, PetOwnerRetrieveUpdateDestroyAPIView, PetsRetrieveUpdateDestroyAPIView

urlpatterns = [
    # Pet owners
    path( "owners/", PetOwnersListCreateAPIView.as_view(), name="owners_list-create" ),
    path( "owners/<int:pk>", PetOwnerRetrieveUpdateDestroyAPIView.as_view(), name="owners_retrieve-update-destroy" ),

    # Pets
    path( "pets/", PetsListCreateAPIView.as_view(), name="pets_list-create" ),
    path( "pets/<int:pk>", PetsRetrieveUpdateDestroyAPIView.as_view(), name="pets_retrieve-update-destroy" ),

    # PetDates
    path( "petdate/", PetDateListCreateAPIView.as_view(), name="petdate_list-create" ),
    path( "petdate/<int:pk>", PetDateRetrieveUpdateDestroyAPIView.as_view(), name="petdate_retrieve-update-destroy" ),
]
