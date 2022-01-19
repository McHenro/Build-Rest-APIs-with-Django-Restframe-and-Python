
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
























# from django.db.models import When
# from django.utils.translation import gettext_lazy as _
# from rest_framework.response import Response
# from rest_framework import status
# from django.core.exceptions import ValidationError

# # Create your models here.
# class Seller(models.Model):
#     name = models.CharField(_('Store name'), max_length=255)
#     description = models.TextField(blank=True)
    
# class Supplier(models.Model):
#     name = models.CharField(_('Business name'), max_length=255)
#     description = models.TextField(blank=True)
    
# class SlotAllocation(models.Model):
#     ACTIVITY = [
#         ('P', 'Purchase'),
#         ('S', 'Subscription'),
#     ]

#     slots = models.SmallIntegerField(
#         _('Slots'))
#     seller = models.ForeignKey(Seller,on_delete=models.CASCADE, 
#                                null=True, verbose_name=_('Reseller'),)
#     supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE, 
#                                  null=True, verbose_name=_('Supplier'))
#     activity = models.CharField(_('Activity'), max_length=2, choices=ACTIVITY)
#     created_at = models.DateTimeField(_('Date Created'), auto_now_add=True)
    
#     class Meta:
#         verbose_name_plural = _('Slot Allocations') 
        
        
#     def clean(self):
#         if self.seller and self.supplier:
#             raise ValidationError('Please select only Reseller OR Supplier, not both.')
#         elif not self.seller and not self.supplier:
#              raise ValidationError('Please select either Reseller or Supplier.')
            
           
      
      
#     # def clean(self):
#     #     cleaned_data = super(SlotAllocation, self).clean()
#     #     breakpoint()
#     #     seller = cleaned_data.get('seller')
#     #     supplier = cleaned_data.get('supplier')
        
#     #     if seller in cleaned_data and supplier in cleaned_data:
#     #         raise ValidationError('Both seller and supplier fields cannot have values ')
#     #     # elif seller is not None and supplier is not None:
#         #     raise ValidationError('Both seller and supplier cannot be not None')
#         # elif seller is not None:
#         #     supplier is None
#         # elif seller is None:
#         #     supplier is not None
    
      
      
      
      
      
      
        
#     # def clean(self):
#     #     super(SlotAllocation, self).clean()
#     #     breakpoint()
#     #     if self.seller is not None:
#     #         self.supplier is None
#     #     if self.supplier is not None:
#     #         self.seller is None
#     #     if self.seller is None and self.supplier is None:
#     #         raise ValidationError('Both seller and supplier cannot be None ')
#     #     if self.seller is not None and self.supplier is not None:
#     #         raise ValidationError('Both seller and supplier\'s fields cannot have values')
#     #     # if self.seller is not None and self.supplier is None:
#     #     #     return self.seller
#     #     # if self.seller is None and self.supplier is not None:
#     #     #     return self.supplier
   
    
    
    
    
    
#     # def save(self,*args,**kwargs):
#     #     if self.seller is not None and self.supplier is not None:
#     #         raise Exception('Both seller and supplier cannot be not None')
#     #     if self.seller is not None and self.supplier is None:
#     #         return self.seller
#     #     if self.seller is None and self.supplier is not None:
#     #         return self.supplier
#     #     super(SlotAllocation, self).save(self,*args,**kwargs)
        
   
   
   
   
   
   
   
#     # def clean(self):
#     #     cleaned_data = super().clean()
#     #     seller = cleaned_data.get('seller')
#     #     supplier = cleaned_data.get('supplier')
#     #     if seller and supplier in cleaned_data:
#     #         raise Exception('seller and supplier objects cannot be both NULL and cannot be both NOT NULL')
#     #     return cleaned_data
        
    

    
    
    
    
    
    
    
    
    
#     # def clean(self,seller=seller,supplier=supplier):
#     #     cleaned_data = super().clean()
#     #     if seller and supplier in cleaned_data:
#     #         raise Exception('seller and supplier objects cannot be both NULL and cannot be both NOT NULL')
#     #     return cleaned_data
       
       
       
       
       
#         #     return Response(
#         #         {'message':'seller and supplier objects cannot be both NULL and cannot be both NOT NULL'},
#         #          status=status.HTTP_400_BAD_REQUEST)
#         # return Response(cleaned_data)
        
#     # def clean(self):
#     #     cleaned_data = super(SlotAllocation, self).clean()
#     #     # breakpoint()
#     #     seller = self.cleaned_data.get('seller')
#     #     supplier = self.cleaned_data.get('supplier')
#     #     if seller in cleaned_data and supplier in cleaned_data:
#     #         raise ValidationError('Atleast seller and supplier fields cannot have values ')
#     #     elif seller is not None and supplier is not None:
#     #         raise ValidationError('Atleast seller and supplier cannot be not None')
#     #     elif seller is not None:
#     #         supplier is None
#     #     elif seller is None:
#     #         supplier is not None