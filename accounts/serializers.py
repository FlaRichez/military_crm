from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *
from django.contrib.auth.models import User, Group

from .services import mailing


class CarSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Car
        fields = ['id','mark','model','year','number','color','type']


class EducationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Education
        fields = ['id','start_date','end_date','school_name','major']


class WarcraftSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Warcraft
        fields = ['id','start_date','end_date','military_area','major','start_pose','end_pose']


class DosierSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True)
    education = EducationSerializer(many=True)
    warcraft = WarcraftSerializer(many=True)

    class Meta:
        model = Dossier
        fields = ['id','fullname','image','user','date_birth','gender','cars','education','warcraft']

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name',instance.full_name)
        cars_data = validated_data.pop('cars')
        education_data = validated_data.pop('education')
        warcraft_data = validated_data.pop('warcraft')
        for car in cars_data:
            car_id = car['id']
            car_data = Car.objects.get(id=car_id)
            car_data.mark = car['mark']
            car_data.save()
        for education in education_data:
            education_id = education['id']
            education_data = Education.objects.get(id=education_id)
            education_data.marl = education['mark']
            education_data.save()
        for warcraft in warcraft_data:
            warcraft_id = warcraft['id']
            warcraft_data = Warcraft.objects.get(id=warcraft_id)
            warcraft_data.marl = warcraft['mark']
            warcraft_data.save()


class RegisterSerializer(serializers.ModelSerializer):
    user_type = serializers.ChoiceField(choices=(
        ('warrior','warrior'),
        ('common','common')
    ),write_only=True)
    check_password = serializers.CharField(write_only=True)
    dossier = DosierSerializer()

    class Meta:
        model = User
        fields = ['username','email','password','check_password','user_type','dossier']

    def create(self, validated_data):
        user_type = validated_data.pop('user_type')
        dossier_data = validated_data.pop('dossier')
        password = validated_data.pop('password')
        check_password = validated_data.pop('check_password')
        user = User.objects.create(**validated_data)

        if password != check_password:
            raise ValidationError("Passwords don't match")
        user.set_password(password)

        if user_type == 'warrior':
            user.is_active = False
            group = Group.objects.get(name='sergeant')
            user.groups.add(group)
            mailing(user.username)
        user.save()
        cars_data = dossier_data.pop('cars')
        education_date = dossier_data.pop('education')
        warcraft_data = dossier_data.pop('warcraft')
        dossier = Dossier.objects.create(user=user,**dossier_data)

        for car in cars_data:
            Car.objects.create(dossier=dossier,**car)
        for education in education_date:
            Education.objects.create(dossier=dossier, **education)
        for warcraft in warcraft_data:
            Warcraft.objects.create(dossier=dossier, **warcraft)
        return user



