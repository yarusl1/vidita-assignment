from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from .models import Image, Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image', 'geo_location', 'description')

    def create(self, validated_data):
        user = self.context['request'].user
        if user.is_anonymous:
            raise PermissionDenied('You must be logged in to create an image.')
        validated_data['owner'] = user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        people_data = validated_data.pop('people')
        people = instance.people.all()
        people = list(people)
        for person_data in people_data:
            person = next((x for x in people if x.id == person_data.get('id')), None)
            if person:
                person.name = person_data.get('name', person.name)
            else:
                person = Person.objects.create(**person_data)
                people.append(person)
        instance.people.set(people)
        return super().update(instance, validated_data)
