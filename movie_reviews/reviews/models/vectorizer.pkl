from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    average_rating = models.FloatField(default=0)

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(default=1)  # Рейтинг от 1 до 5

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.movie.update_average_rating()

    def __str__(self):
        return f'Review for {self.movie.title}: {self.rating}'