from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

def product_imagen(instance, filename):
    """
    Encargado de crear un path donde guardar las imagenes de ProductImage.
    """
    return "product/{0}/{1}".format(
        instance.product.title,
        filename
    )

def trademark_imagen(instance, filename):
    """
    Encargado de crear un path donde guardar las imagenes de Trademark.
    """
    return "trademark/{0}/{1}".format(
        instance.title,
        filename
    )

def subcategory_imagen(instance, filename):
    """
    Encargado de crear un path donde guardar las imagenes de SubCategory.
    """
    return "subcategory/{0}/{1}".format(
        instance.title,
        filename
    )

def category_imagen(instance, filename):
    """
    Encargado de crear un path donde guardar las imagenes de Category.
    """
    return "category/{0}/{1}".format(
        instance.title,
        filename
    )

class BaseModel(models.Model):
    """
    Definicion del modelo base.
    """
    title = models.CharField("Titulo", max_length=255, unique=True)
    is_active = models.BooleanField("¿Activo?", default=True)
    short_description = models.TextField("Descripcion Corta", blank=True)
    slug = models.SlugField("URL", max_length=255, unique=True, blank=True, null=True)
    created_at = models.DateTimeField("Creado el", auto_now_add=True, null=True)
    update_at = models.DateTimeField("Actualizado", auto_now=True, null=True)

    class Meta:
        abstract = True

class TC(models.Model):
    """
    Definicion del modelo TC
    * Aloja el tipo de cambio
    """
    tc = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateTimeField("Creado el", auto_now_add=True, null=True)
    update_at = models.DateTimeField("Actualizado", auto_now=True, null=True)

    class Meta:
        verbose_name = "Tipo de Cambio"
        verbose_name_plural = "Tipo de Cambio"
    
    def __str__(self):
        return f"{self.tc}"


class Trademark(BaseModel):
    """
    Definicion del Modelo Trademark
    """
    image = models.ImageField("Imagen", upload_to=category_imagen, blank=True, null=True)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas" 
    
    def __str__(self):
        return self.title

class Category(BaseModel):
    """
    Definicion del modelo Category.
    * Encargado de administrar las categorias.
    """
    image = models.ImageField("Imagen", upload_to=category_imagen, blank=True, null=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    
    def __str__(self):
        return self.title

class SubCategory(BaseModel):
    """
    Definicion del modelo SubCategory
    * Posee una relacion con Category de uno a muchos.
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoria", related_name="gcategory")
    image = models.ImageField("Imagen", upload_to=subcategory_imagen, blank=True, null=True)

    class Meta:
        verbose_name = "Sub Categoria"
        verbose_name_plural = "Sub Categorias"
    
    def __str__(self):
        return self.title

class Product(BaseModel):
    """
    Definicion del modelo Product
    * Relaciones con Trademark, SubCategory
    """
    trademark = models.ForeignKey(Trademark, on_delete=models.CASCADE, verbose_name="Marca")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name="Sub Categoria")
    sku = models.CharField("SKU", max_length=255)
    specs = models.TextField("Especificaciones", blank=True, null=True)
    stock = models.IntegerField("STOCK", default=0)
    price = models.DecimalField("Precio $", max_digits=9, decimal_places=2)
    is_offer = models.BooleanField("¿Oferta?", default=False)
    price_offer = models.DecimalField("Precio Oferta $", max_digits=9, decimal_places=2)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
    
    def __str__(self):
        return self.title
    
    # Se calcula los precios locales
    def price_pen(self):
        get_tc = TC.objects.last()
        price_calculate = self.price * get_tc
        return price_calculate
    
    def price_pen_offer(self):
        get_tc = TC.objects.last()
        if self.is_offer:
            if self.price_offer is not None:
                price_calculate = self.price_offer * get_tc
        
        return price_calculate

class ProductImagen(models.Model):
    """
    Definicion ProductImagen.
    Para guardar imagenes de productos.
    Esta relacionado con una FK con product.
    """
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField("Imagen", upload_to=product_imagen, blank=True, null=True)
    created_at = models.DateTimeField("Creado el", auto_now_add=True, null=True)
    update_at = models.DateTimeField("Actualizado", auto_now=True, null=True)

    def __str__(self):
        return f"Imagen de {self.pk} - {self.product.title}"
    
    class Meta:
        verbose_name = "Imagenes de Productos"
        verbose_name_plural = "Imagenes de Productos"
    