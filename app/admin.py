from django.contrib import admin

from .models import Category, Event, TicketType, UserProfile, Ticket, Review

admin.site.register(Category)
admin.site.register(Event)
admin.site.register(TicketType)
admin.site.register(UserProfile)
admin.site.register(Ticket)
admin.site.register(Review)
