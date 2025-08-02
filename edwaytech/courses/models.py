from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    instructor = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    registration_link = models.URLField()
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)

    # Additional course detail fields
    description = models.TextField(blank=True)
    syllabus = models.TextField(blank=True)
    duration = models.CharField(max_length=50, blank=True)
    certificate = models.BooleanField(default=False)
    placement_opportunity = models.BooleanField(default=False)
    mock_interviews = models.BooleanField(default=False)
    live_classes = models.BooleanField(default=False)
    notes_provided = models.BooleanField(default=False)
    source_code_link = models.URLField(blank=True)
    deployment_support = models.BooleanField(default=False)
    instructor_info = models.TextField(blank=True)
    student_feedback = models.TextField(blank=True)

    def __str__(self):
        return self.title
