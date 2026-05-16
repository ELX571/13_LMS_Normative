from django.db import models
from base.models import BaseModel


class Document(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()

    img = models.ImageField(
        upload_to='media/'
        , blank=True
        , null=True
    )
    video = models.FileField(
        upload_to='media/'
        , blank=True
        , null=True
                             )
    document = models.FileField(upload_to='media/',
                                blank=True,
                                null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'document'


