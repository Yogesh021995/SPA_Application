from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Visitor,StaffMember, VisitorDetails
from .serializers import VisitorSerializer,StaffMemberSerializer, VisitorDetailsSerializer

@api_view(['POST'])
def sign_in(request):
    serializer = VisitorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_staff_members(request):
    staff_members = StaffMember.objects.all()
    serializer = StaffMemberSerializer(staff_members, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def save_visitor_details(request):
    serializer = VisitorDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_drinks(request):
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def save_visitor_drink(request):
    serializer = VisitorDrinkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)