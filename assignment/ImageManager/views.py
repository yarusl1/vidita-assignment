from django.db.models import Q
from django.http import Http404
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Image, Person
from .serializers import ImageSerializer, PersonSerializer
import dateutil.parser
import json


class PeopleAutocompleteView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, _, name):
        images = Image.objects.filter(people__name__icontains=name, owner=self.request.user)
        people_list = []
        for image in images:
            people_list += image.people.all()
        people_list = set(people_list)
        people_list = set([people for people in people_list if name.lower() in people.name.lower()])
        serializer = PersonSerializer(people_list, many=True)
        resp = [entry['name'] for entry in serializer.data]
        return Response(resp)


class ImageView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        image = serializer.save(owner=self.request.user)
        people_data_json = self.request.data.pop('people', "[]")
        people_data = [json.loads(people.replace("'", '"')) for people in people_data_json]
        people_data = [person for sublist in people_data for person in sublist]
        people_data = [person for person in people_data if person.get('name', '').strip()]
        people = [Person(name=person.get('name')) for person in people_data]
        Person.objects.bulk_create(people)
        image.people.set(people)
        image.save()

    def get_list(self, request):
        geo_location = request.query_params.get('geo_location', None)
        date = request.query_params.get('date', None)
        people = json.loads(request.query_params.get('people', "[]"))
        description = request.query_params.get('description', None)

        images = Image.objects.filter(owner=self.request.user)
        if geo_location:
            images = images.filter(geo_location=geo_location)
        if date:
            try:
                parsed_date = dateutil.parser.parse(date).date()
            except Exception:
                raise ValidationError('Invalid date format')

            images = images.filter(date=parsed_date)
        q_objects = Q()
        for person in people:
            q_objects |= Q(people__name=person["name"])
        if people:
            images = images.filter(q_objects)
        if description:
            images = images.filter(description__icontains=description)

        serializer = ImageSerializer(images, many=True)
        return Response([entry["image"] for entry in serializer.data])

    def get_image(self, _, image_id):
        try:
            image = Image.objects.get(id=image_id, owner=self.request.user)
            serializer = ImageSerializer(image)
            return Response(serializer.data)
        except Image.DoesNotExist:
            raise Http404
