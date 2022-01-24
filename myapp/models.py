
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class StreamPlatForm(models.Model):
    name = models.CharField(_('Name'),max_length=30)
    about = models.CharField(_('About'),max_length=150)
    website = models.URLField(_('Website'),max_length=100)
    
    class Meta:
        verbose_name_plural = _('Stream Platforms')
        
    def __str__(self):
        return self.name
    
    
class WatchList(models.Model):
    title = models.CharField(_('Title'),max_length=50)
    storyline = models.CharField(_('Story Line'),max_length=200)
    platform = models.ForeignKey(StreamPlatForm, on_delete=models.CASCADE,
                                 related_name='watchlist', verbose_name=_('Platform'))
    active = models.BooleanField(_('Active'),default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = _('Watch Lists')
    
    def __str__(self):
        return self.title
    

class Review(models.Model):
    rating = models.PositiveIntegerField(_('Rating'), 
                validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(_('Description'), max_length=200, null=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, 
                related_name='reviews', verbose_name=_('Watchlist') )
    active = models.BooleanField(_('Active'), default=True)
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    updated = models.DateTimeField(_('Update'), auto_now=True)
    
    def __str__(self):
        return str(self.rating) + " |  " + self.watchlist.title


# class Movie(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=200)
#     active = models.BooleanField(default=True)
    
#     def __str__(self):
#         return self.name
