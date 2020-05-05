from django.db import models


# Create your models here.

class Note(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    content = models.CharField(max_length=200, help_text='Enter note content')
    created_at = models.DateTimeField(auto_now_add=True)

    # Metadata
    class Meta:
        ordering = ['-created_at']

    # Methods
    def dummy(self):
        return "dummy"

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.content
