from django.db import models


class IndexText(models.Model):
    """IndexText handles text for base display. A title and summary are needed, and then depending on the size of
    the text needs, choose either small or big."""
    text_title = models.CharField(max_length=250)
    text_summary = models.CharField(max_length=250)
    small_text_fields = models.CharField(max_length=250, blank=True)
    big_text_fields = models.TextField(blank=True)

    def __str__(self):
        """
        Checks value of text fields, starting with small, to determine which to return.
        :return: Either small_text_fields or big_text_fields.
        """
        if self.small_text_fields is not None:
            return f"{self.text_title} - {self.text_summary}: {self.small_text_fields}"
        if self.big_text_fields is not None:
            return f"{self.text_title} - {self.text_summary}: {self.big_text_fields}"
