from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer

from shared_models.models import Course, Section, Product, Profile
from models.course.section import Section as SectionModel
from models.courseprovider.course_provider import CourseProvider as CourseProviderModel
from models.course.course import Course as CourseModel
from models.publish.publish_job import PublishJob as PublishJobModel
from models.log.publish_log import PublishLog as PublishLogModel


from rest_framework_mongoengine.fields import ReferenceField


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id', 'store', 'external_id', 'product_type',
            'title', 'content', 'image', 'limit_applicable',
            'total_quantity', 'quantity_sold', 'available_quantity',
            'is_active', 'tax_code', 'fee', 'currency_code'
        )


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = (
            'id',
            'course_provider',
            'title',
            'content_ready',
            'slug',
            'content_db_reference',
            'course_image_uri',
            'external_image_url'
        )


class CourseModelSerializer(DocumentSerializer):
    provider = ReferenceField(CourseProviderModel)

    class Meta:
        model = CourseModel


class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = ('id', 'course', 'name', 'fee', 'seat_capacity', 'available_seat',
                  'execution_mode', 'registration_deadline', 'content_db_reference', 'is_active')


class CheckSectionModelValidationSerializer(EmbeddedDocumentSerializer):

    class Meta:
        model = SectionModel


class PublishJobModelSerializer(DocumentSerializer):

    class Meta:
        model = PublishJobModel


class PublishLogModelSerializer(DocumentSerializer):

    class Meta:
        model = PublishLogModel
        fields = ('type', 'external_id', 'status', 'time', 'message', 'errors')


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'primary_email', 'primary_contact_number')
