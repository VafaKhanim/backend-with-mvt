from django.conf import settings

def social_media_links(request):

    return {
        'twitter': getattr(settings, 'TWITTER_URL', '#'),
        'facebook': getattr(settings, 'FACEBOOK_URL', '#'),
        'linkedin': getattr(settings, 'LINKEDIN_URL', '#'),
         'instagram': getattr(settings, 'INSTAGRAM_URL', '#')
    }

def head_bar(request):
    return {
        'home': getattr(settings, 'HOME_URL', '#'),
        'about': getattr(settings, 'ABOUT_URL', '#'),
        'furniture': getattr(settings, 'FURNITURES_URL', '#'),
        'blog': getattr(settings, 'BLOG_URL', '#'),
        'contact_us': getattr(settings, 'CONTACT_PAGE_URL', '#'),
    }


def contact_ways(request):
    return {
        'call' : getattr(settings, 'CALL_URL', '#'),
        'mail' : getattr(settings, 'MAIL_URL', '#'),
        'location': getattr(settings, 'LOCATION_URL', '#')
    }