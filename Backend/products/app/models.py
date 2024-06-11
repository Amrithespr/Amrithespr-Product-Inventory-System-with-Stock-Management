from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from versatileimagefield.fields import VersatileImageField


# Create your models here.

class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ProductID = models.BigIntegerField(unique=True)
    ProductCode = models.CharField(max_length=255, unique=True)
    ProductName = models.CharField(max_length=255)
    ProductImage = VersatileImageField(upload_to="uploads/", blank=True, null=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedDate = models.DateTimeField(blank=True, null=True)
    CreatedUser = models.ForeignKey("auth.User", related_name="user%(class)s_objects", on_delete=models.CASCADE)
    IsFavourite = models.BooleanField(default=False)
    Active = models.BooleanField(default=True)
    HSNCode = models.CharField(max_length=255, blank=True, null=True)
    TotalStock = models.DecimalField(default=0.00, max_digits=20, decimal_places=8, blank=True, null=True)

    class Meta:
        db_table = "Products"
        verbose_name = _("product")
        verbose_name_plural = _("products")
        unique_together = (("ProductCode", "ProductID"),)
        ordering = ("-CreatedDate", "ProductID")

    def __str__(self):
        return self.ProductName


class Variant(models.Model):
    name = models.CharField(max_length=100)

    db_table = "products_variant"
    verbose_name = _("variant")
    verbose_name_plural = _("variants")
    ordering = ["name"]
    unique_together = (("product", "name"),)

    def __str__(self):
        return f"{self.name}"


class SubVariant(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "products_subvariant"
        verbose_name = _("sub variant")
        verbose_name_plural = _("sub variants")
        ordering = ["name"]


    def __str__(self):
        return self.name