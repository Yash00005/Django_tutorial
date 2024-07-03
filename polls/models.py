from django.db import models

# Create your models here.
class siterating(models.Model):
    RATING_CHOICES = [
        (1, '1 - Very poor'),
        (2, '2 - Poor'),
        (3, '3 - Fair'),
        (4, '4 - Good'),
        (5, '5 - Very good'),
        (6, '6 - Excellent'),
        (7, '7 - Outstanding'),
        (8, '8 - Exceptional'),
        (9, '9 - Amazing'),
        (10, '10 - Perfect'),
    ]

    rating = models.IntegerField(choices=RATING_CHOICES, default=1)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    #class Meta:
     #   app_label = 'polls'

    def __str__(self):
        return f"Rating: {self.rating} at {self.created_at}"