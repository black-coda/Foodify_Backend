from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class CafetriaType(models.Model):
    CAFETERIA_TYPE = (
        ("cafe 1", 'Anchor Cafteria 1'),
        ("Cafe 2", 'Anchor Cafeteria 2'),
    )

    cafeteria = models.CharField(max_length=20, choices=CAFETERIA_TYPE)

    class Meta:
        verbose_name = 'Cafeteria'
        verbose_name_plural = 'Cafeterias'

    def __str__(self):
        return self.cafeteria


class FoodAvailabilityManager(models.Manager):
    def get_queryset(self):
        return super(FoodAvailabilityManager, self).get_queryset().filter(available=True)


class FoodCategory(models.Model):
    category_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = 'Food Category'
        verbose_name = 'category'

    def save(self, *args, **kwargs):
        super(FoodCategory, self).save()
        value = self.category_name
        self.slug = slugify(value)

    def __str__(self):
        return self.category_name


class FoodItem(models.Model):
    cafetria = models.OneToOneField(CafetriaType, on_delete=models.CASCADE)
    category = models.ForeignKey(FoodCategory, on_delete=models.SET_NULL, null=True, blank=True)
    name_of_food = models.CharField(max_length=200)
    price = models.CharField(blank=True, max_length=200, null=True, default="All food are minimum of N100")
    available = models.BooleanField(default=False)
    # Default manager
    objects = models.Manager()
    # Custom manager to filter out available food
    available_manager = FoodAvailabilityManager()
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.cafetria}  -  {self.category} -  {self.available}'

    class Meta:
        ordering = ('name_of_food',)

    def get_absolute_url(self):
        return reverse('main:shop_detail', args=[self.id, self.name_of_food])
