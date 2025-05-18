from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse 

# Create your models here.

class Resume(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    job_title = models.CharField(_("Job Title"), max_length=50)
    skills = models.TextField(_("Skills"))
    experince = models.TextField(_("Experience"))
    education = models.TextField(_("Education"))  # Make sure this field is present
    genrated_resume = models.TextField(_("Generated Resume"))
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)

    class Meta:
        verbose_name = _("Resume")
        verbose_name_plural = _("Resumes")  # Fixed plural name

    def __str__(self):
        return self.job_title  # Changed to return job_title instead of name
    def get_absolute_url(self):
        return reverse("resume_detail", kwargs={"pk": self.pk})  

    

