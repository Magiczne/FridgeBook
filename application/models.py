from django.conf import settings
from django.db import models


# Create your models here.

class Note(models.Model):
    # Fields
    title = models.CharField(max_length=255, help_text='Enter note title')
    content = models.CharField(max_length=255, help_text='Enter note content')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name="User")
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    # Metadata
    class Meta:
        get_latest_by = ['-created_at']

    # Methods
    # def dummy(self):
    #     return "dummy"

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title
