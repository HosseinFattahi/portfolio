from django.shortcuts import render, redirect
from .models import SiteContent, Expertise, TimelineEntry, PortfolioItem, SiteSettings
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    # Fetch content for different sections
    intro = SiteContent.objects.filter(section='intro').first()
    about = SiteContent.objects.filter(section='about').first()
    expertise = Expertise.objects.all()
    experience = TimelineEntry.objects.filter(category='experience')
    education = TimelineEntry.objects.filter(category='education')
    contact = SiteContent.objects.filter(section='contact').first()
    portfolio = PortfolioItem.objects.all()
    site_settings = SiteSettings.get_solo()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            subject = f'New contact form submission from {name}'
            message_body = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
            send_mail(
                subject,
                message_body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.RECIPIENT_EMAIL],
                fail_silently=False,
            )

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')
        else:
            messages.error(request, 'There was an error sending your message. Please try again.')
    else:
        form = ContactForm()

    context = {
        'intro': intro,
        'about': about,
        'expertise': expertise,
        'experience': experience,
        'education': education,
        'contact': contact,
        'portfolio': portfolio,
        'form': form,
        'site_settings': site_settings,
    }

    return render(request, 'index.html', context)
