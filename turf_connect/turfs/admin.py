from django.contrib import admin
from .models import Turf, TurfImage, VerificationDocument, Slot, Booking, Payment

admin.site.register(Turf)
admin.site.register(TurfImage)
admin.site.register(VerificationDocument)
admin.site.register(Slot)
admin.site.register(Booking)
admin.site.register(Payment)
