from django.db import models
from django.contrib.auth.models import User

# Категория события 
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Событие 
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Тип билета 
class TicketType(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    event_date = models.DateTimeField()
    available_quantity = models.PositiveIntegerField()
    total_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.description} - {self.event.title}"


# Профиль пользователя 
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.username


# Билет
class Ticket(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.owner.user.username} - {self.ticket_type}"


# Отзыв
class Review(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    description = models.TextField()
    rating = models.PositiveIntegerField()
    published_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"Review by {self.author.user.username} - {self.rating}"
