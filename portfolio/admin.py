from django.contrib import admin
from .models import SiteContent, Expertise, TimelineEntry, PortfolioItem,SiteSettings
from solo.admin import SingletonModelAdmin

@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ('section', 'title', 'last_updated')
    list_filter = ('section',)
    search_fields = ('title', 'content')

@admin.register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(TimelineEntry)
class TimelineEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'role', 'category', 'timeframe', 'order')
    list_filter = ('category',)
    search_fields = ('title', 'role', 'description')
    ordering = ('category', 'order')

@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'order')
    list_filter = ('category',)
    search_fields = ('title', 'description')
    ordering = ('category', 'order')

@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'first_image', 'first_image_2x', 'first_image_alt',
                'cv_file', 'contact_email',
                'instagram_link', 'linkedin_link', 'x_link',
                'whatsapp_link', 'telegram_link',
                "recent_work_title","recent_work_text",
                "say_hi_title","say_hi_text"
            )
        }),
    )