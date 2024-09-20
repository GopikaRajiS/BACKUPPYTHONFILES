from django.db import models


# declare a new model with a name "Lmodel"
class Lmodel(models.Model):
    # fields of the model
    # title = models.CharField(
    #     max_length=50,
    #     null=False,
    #     blank=False,
    #     unique=True,
    #     verbose_name='Todo Title'
    # )
    #
    # description = models.TextField(
    #     max_length=300,
    #     verbose_name='Description'
    # )
    # # renames the instances of the model with their title name
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
