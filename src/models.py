from django.db import models

domain = (("Structural", "Structural"),
          ("Electronice", "Electronics"),
          ("Coding", "Coding"))

yearoFstudy = (("2024", "2024"),
               ("2023", "2023"),
               ("2025", "2025"),
               ("2026", "2026"))


class team_member(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    year = models.CharField(
        max_length=200, choices=yearoFstudy, null=True, blank=True)


class projects(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    purpose = models.TextField(null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    pdfLink = models.CharField(max_length=200, null=True, blank=True)
    members = models.ManyToManyField(team_member, blank=True, null=True)
    ytlink = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class member(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    domain = models.CharField(
        max_length=200, choices=domain, null=True, blank=True)
    year = models.CharField(
        max_length=200, choices=yearoFstudy, null=True, blank=True)
    branch = models.CharField(max_length=200, null=True, blank=True)
    linkedinLInk = models.CharField(max_length=200, null=True, blank=True)
    githubLink = models.CharField(max_length=200, null=True, blank=True)
    twitterLink = models.CharField(max_length=200, null=True, blank=True)
    projects_part = models.ManyToManyField(projects, blank=True, null=True)
    profile = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
