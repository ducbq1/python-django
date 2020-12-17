from django.db import models

class Paper(models.Model):
    id = models.IntegerField(primary_key=True)
    pii = models.IntegerField()
    title = models.TextField(max_length=200)
    abstract = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    url = models.CharField(max_length=200)
    journal_id = models.IntegerField()


class CoAuthorship(models.Model):
    # date = models.DateTimeField('date published')
    first_author_id = models.IntegerField()
    second_author_id = models.IntegerField()
    paper_id = models.IntegerField()


class PotentialCoAuthor(models.Model):
    # date = models.DateTimeField('date published')
    first_author_id = models.IntegerField()
    second_author_id = models.IntegerField()
    # paper_id = models.IntegerField()



