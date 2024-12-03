from django.db import models

# TODO: We could use this model if we wanted to have a granular control over the users
# class User(models.Model):
#     username = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


#     def __str__(self):
#         return self.username

class Post(models.Model):
    title = models.CharField(max_length=255)
    username = models.CharField(max_length=255, default='Anonymous', blank=True)
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    # TODO: We could use this field if we wanted to have a granular control over the users
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_datetime']
