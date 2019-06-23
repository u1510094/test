import datetime
import uuid

from django.core.validators import RegexValidator
from django.core.validators import ValidationError as Error
from django.db import models
from rest_framework.serializers import ValidationError

from core.django.model import BaseModel, DeleteModel

FILE_TYPES = {
    r'^(doc|docx)$': 'document',
    r'^(pdf)$': 'pdf',
    r'^(jpg|jpeg|png|gif)$': 'image',
    r'^(xls|xlsx)$': 'excel',
    r'^(zip|rar)$': 'compressed',
}


def upload_name(instance, filename):
    file_type = filename.split('.')[-1]
    today = str(datetime.datetime.today())[0:7]
    for regex, folder in FILE_TYPES.items():
        try:
            RegexValidator(regex).__call__(file_type)
            return 'file/%s/%s/%s.%s' % (
                folder, today, uuid.uuid4(), file_type)
        except Error:
            pass
    raise ValidationError(detail={'File type is unacceptable'})


class File(DeleteModel, BaseModel):
    name = models.CharField(max_length=255, null=True)
    content_type = models.CharField(max_length=255, null=True)
    file = models.FileField(upload_to=upload_name)

    def __str__(self):
        return self.name or f'id={self.id}'
