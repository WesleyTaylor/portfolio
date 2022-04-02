from django.db import models

class Project(models.Model):
    def upload_image(self, filename):
        return 'project/{}/{}'.format(self.title, filename)

    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/")

