from django.urls import path
from rest_framework.routers import DefaultRouter
from course.apps import CourseConfig
from course.views import CourseViewSet, SubscriptionCreateView, SubscriptionDeleteView
from course.views import LessonListView, LessonCreateView, LessonDetailView, LessonUpdateView, LessonDeleteView


app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/', LessonListView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonDetailView.as_view(), name='lesson-view'),
    path('lesson/create/', LessonCreateView.as_view(), name='lesson-add'),
    path('lesson/update/<int:pk>/', LessonUpdateView.as_view(), name='lesson-edit'),
    path('lesson/delete/<int:pk>/', LessonDeleteView.as_view(), name='lesson-del'),
    # subscription
    path('subscribe/<int:pk>/', SubscriptionCreateView.as_view(), name='subscription-add'),
    path('subscription/delete/<int:course_pk>/', SubscriptionDeleteView.as_view(), name='subscription-del'),
] + router.urls
