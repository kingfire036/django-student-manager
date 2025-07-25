from django.test import TestCase
from django.urls import reverse
from .models import Student
import datetime

class StudentViewTests(TestCase):

    def setUp(self):
        self.student = Student.objects.create(
            first_name="Test",
            last_name="Student",
            email="test.student@example.com",
            date_of_birth=datetime.date(2005, 5, 24),
            enrollment_number="TS2025001"
        )

    def test_student_list_view(self):
        """
        Tests that the student list view returns a 200 status code,
        uses the correct template, and contains the student data.
        """
        response = self.client.get(reverse('student-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/student_list.html')
        self.assertContains(response, self.student.first_name)

    def test_student_orm_creation(self):
        """
        Tests that a Student can be created via the ORM.
        """
        student_count = Student.objects.count()
        Student.objects.create(
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com",
            date_of_birth=datetime.date(2006, 8, 15),
            enrollment_number="JD2025002"
        )
        self.assertEqual(Student.objects.count(), student_count + 1)