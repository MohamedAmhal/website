from django.contrib import admin
from core.models import CartOrderProducts, Coupon, Product, Category, Vendor, CartOrder, ProductImages, ProductReview, wishlist_model, Address
from import_export.admin import ImportExportModelAdmin

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(ImportExportModelAdmin):
    inlines = [ProductImagesAdmin]
    list_editable = ['title', 'price', 'featured', 'product_status']
    list_display = ['user', 'title', 'product_image', 'price', 'category', 'vendor', 'featured', 'product_status', 'pid']

class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['title', 'category_image']

class VendorAdmin(ImportExportModelAdmin):
    list_display = ['title', 'vendor_image']


class CartOrderAdmin(ImportExportModelAdmin):
    list_editable = ['paid_status', 'product_status', 'sku']
    list_display = ['user',  'price', 'paid_status', 'order_date','product_status', 'sku']


class CartOrderProductsAdmin(ImportExportModelAdmin):
    list_display = ['order', 'invoice_no', 'item', 'image','qty', 'price', 'total']


class ProductReviewAdmin(ImportExportModelAdmin):
    list_display = ['user', 'product', 'review', 'rating']


class wishlistAdmin(ImportExportModelAdmin):
    list_display = ['user', 'product', 'date']


class AddressAdmin(ImportExportModelAdmin):
    list_editable = ['address', 'status']
    list_display = ['user', 'address', 'status']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderProducts, CartOrderProductsAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(wishlist_model, wishlistAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Coupon)
