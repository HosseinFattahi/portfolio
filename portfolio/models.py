from django.db import models
from django.utils import timezone

# Model for Site-Wide Settings (e.g., Intro, About)

from solo.models import SingletonModel

class SiteSettings(SingletonModel):
    first_image = models.ImageField(
        upload_to='settings/',
        blank=True,
        null=True,
        help_text="Upload the first image for the Intro section."
    )
    first_image_2x = models.ImageField(
        upload_to='settings/',
        blank=True,
        null=True,
        help_text="Upload the high-resolution (2x) version of the first image."
    )
    first_image_alt = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Alternative text for the first image."
    )
    cv_file = models.FileField(
        upload_to='cv/',
        blank=True,
        null=True,
        help_text="Upload your CV."
    )
    
    # New Email Field for "Say Hello" Section
    contact_email = models.EmailField(
        max_length=254,
        blank=True,
        null=True,
        help_text="Email address for the 'Say Hello' section."
    )
    
    # Updated Social Links
    instagram_link = models.URLField(blank=True, null=True, help_text="Instagram Profile URL")
    linkedin_link = models.URLField(blank=True, null=True, help_text="LinkedIn Profile URL")
    x_link = models.URLField(blank=True, null=True, help_text="X (Twitter) Profile URL")
    whatsapp_link = models.URLField(blank=True, null=True, help_text="WhatsApp Contact URL")
    telegram_link = models.URLField(blank=True, null=True, help_text="Telegram Contact URL")
    recent_work_title = models.CharField(max_length=100,default="Recent Works")
    recent_work_text = models.TextField(default="",blank=True,null=True)
    say_hi_title = models.CharField(max_length=100,default="Recent Works")
    say_hi_text = models.TextField(default="",blank=True,null=True)
    
    def __str__(self):
        return "Site Settings"



class SiteContent(models.Model):
    SECTION_CHOICES = [
        ('intro', 'Intro'),
        ('about', 'About'),
        ('expertise', 'Expertise'),
        ('experience', 'Experience'),
        ('education', 'Education'),
        ('contact', 'Contact'),
    ]
    section = models.CharField(max_length=50, choices=SECTION_CHOICES, unique=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_section_display()

# Model for Expertise Skills
class Expertise(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model for Timeline Entries (Experience and Education)
class TimelineEntry(models.Model):
    CATEGORY_CHOICES = [
        ('experience', 'Experience'),
        ('education', 'Education'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    timeframe = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} - {self.role}"

# Model for Portfolio (Music Samples)
class PortfolioItem(models.Model):
    CATEGORY_CHOICES = [
        ('music_upload', 'Music Upload'),
        ('music_link', 'Music Link'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    audio_file = models.FileField(upload_to='music/', blank=True, null=True)
    audio_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    project_link = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
