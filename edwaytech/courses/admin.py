from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'instructor', 'date', 'time', 'registration_link',
        'duration', 'certificate', 'placement_opportunity'
    ]
    list_filter = ['certificate', 'placement_opportunity', 'live_classes']
    search_fields = ['title', 'instructor', 'syllabus', 'description']
    fieldsets = (
        ("Basic Info", {
            'fields': ('title', 'instructor', 'date', 'time', 'registration_link', 'image')
        }),
        ("Course Details", {
            'fields': (
                'description', 'syllabus', 'duration', 'certificate',
                'placement_opportunity', 'mock_interviews', 'live_classes',
                'notes_provided', 'source_code_link', 'deployment_support'
            )
        }),
        ("Instructor & Feedback", {
            'fields': ('instructor_info', 'student_feedback')
        }),
    )
