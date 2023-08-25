from rest_framework import serializers
from .models import Visitor
from .models import StaffMember
from .models import VisitorDetails
from .models import Drink
from .models import VisitorDrink

class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = '__all__'

class StaffMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffMember
        fields = '__all__'

class VisitorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorDetails
        fields = '__all__'

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'

class VisitorDrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorDrink
        fields = '__all__'