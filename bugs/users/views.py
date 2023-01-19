from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from faker import Faker
from .serializers import UsersSerializer
import bugs.users.credentials

fake = Faker()


@api_view(['GET'])
def users(request):
    user_list = []
    for i in range(10):
        id = fake.random_int()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        password = fake.password()
        phone_number = fake.phone_number()
        address = fake.address()
        city = fake.city()
        state = fake.country()
        postcode = fake.postcode()
        is_active = 1

        user = {
            'id': id,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'phone_number': phone_number,
            'address': address,
            'city': city,
            'state': state,
            'postcode': postcode,
            'is_active': is_active
        }
        serializer = UsersSerializer(
            data=user
        )
        serializer.is_valid(raise_exception=True)
    return Response(user_list, status=status.HTTP_200_OK)


# @api_view(['POST'])
# def userCreate(request):
#     print(request.POST)
#     if request.META['HTTP_BEARER'] == bugs.users.credentials.loremu:
#         serializer = UsersSerializer(
#             data=request.data
#         )
#         serializer.is_valid(raise_exception=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     else:
#         return Response('ACCESS DENIED', status=status.HTTP_403_FORBIDDEN)

@api_view(['POST', 'GET'])
def userCreate(request):
    token = request.META.get('HTTP_AUTHORIZATION').split(" ")[1]
    print(token)
    if token is None:
        return Response({'error': 'Token is missing'}, status=status.HTTP_401_UNAUTHORIZED)
    if token != bugs.users.credentials.loremu:
        return Response('ACCESS DENIED', status=status.HTTP_403_FORBIDDEN)
    serializer = UsersSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.data, status=status.HTTP_200_OK)