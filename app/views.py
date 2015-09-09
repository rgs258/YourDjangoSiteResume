"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

YOUR_INFO = {
    'name' : 'Ryan Sullivan',
    'bio' : 'A person who does things...sometimes',
    'email' : '', # Leave blank if you'd prefer not to share your email with other conference attendees
    'twitter_username' : 'rgs258', # No @ symbol, just the handle.
    'github_username' : "rgs258", 
    'headshot_url' : 'https://pbs.twimg.com/profile_images/3430729352/d59992d2464d98372fd53c5dff539fbb_400x400.jpeg', # Link to your GitHub, Twitter, or Gravatar profile image.
}
    
def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/base.html',
        context_instance = RequestContext(request,
            {
                'attendee' : YOUR_INFO,    
                'year': datetime.now().year,
            })
    )