from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Person
from .serializers import PersonSerializer


class TestPerson(APITestCase):
    """Test Person model class"""

    def setUp(self) -> None:
        Person.objects.create(name="Mr. Test")

    def test_list_persons(self) -> None:
        """Test list all data is succesful"""
        persons = Person.objects.all()
        responce = self.client.get("/api/")
        serializers = PersonSerializer(persons, many=True)
        self.assertEqual(responce.data, serializers.data)
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertIsInstance(responce.json(), list)

    def test_create_person(self) -> None:
        """Test creating a person data is succesful"""
        person = Person.objects.create(name="Test 1")
        responce_post = self.client.post("/api/", data={"name": "Test 2"})
        responce_get = self.client.get("/api/")
        self.assertEqual(str(person), person.name)
        self.assertEqual(len(responce_get.data), 3)
        self.assertEqual(responce_post.status_code, status.HTTP_201_CREATED)

    def test_retrieve_person(self) -> None:
        """Test get particular person data is succesful"""
        person = Person.objects.create(name="Mr. Test")
        responce = self.client.get(f"/api/{person.id}/")
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertIsInstance(responce.data, dict)
        self.assertEqual(person.name, "Mr. Test")

    def test_update_person(self) -> None:
        """Test update  particular person data is succesful"""
        person = Person.objects.create(name="Mr. Test")
        responce = self.client.put(f"/api/{person.id}/", data={"name": "Test 3"})
        new_person = Person.objects.get(id=person.id)
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertEqual(new_person.name, "Test 3")
        self.assertIsInstance(responce.data, dict)

    def test_partial_update_person(self) -> None:
        """Test partial update  particular person data is succesful"""
        person = Person.objects.create(name="Mr. Test")
        responce = self.client.patch(f"/api/{person.id}/", data={"name": "Test 4"})
        new_person = Person.objects.get(id=person.id)
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertEqual(new_person.name, "Test 4")
        self.assertIsInstance(responce.data, dict)

    def test_delete_person(self) -> None:
        """Test delete  particular person data is succesful"""
        person = Person.objects.create(name="Mr. Test")
        responce = self.client.delete(f"/api/{person.id}/")
        self.assertEqual(responce.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(person.DoesNotExist):
            Person.objects.get(id=person.id)
