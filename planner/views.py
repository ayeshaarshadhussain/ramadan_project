from django.shortcuts import render
from datetime import datetime
from .models import Quote, EidEvent
import random

def home(request):
     # Set Ramadan date manually (example)
      ramadan_date = datetime(2026, 2, 18)

      now = datetime.now()
      time_remaining = ramadan_date - now

      days = time_remaining.days
      seconds = time_remaining.seconds

      hours = seconds // 3600
      minutes = (seconds % 3600) // 60

       # Random daily quote
      quotes = Quote.objects.all()
      quote = None
      if quotes.exists():
        quote = random.choice(quotes)

      events = EidEvent.objects.all()

      context = {
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'quote': quote,
        'events': events
    }

      return render(request, 'planner/home.html', context)    