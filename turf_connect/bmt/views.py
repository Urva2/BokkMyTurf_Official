from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages

from turfs.models import Turf, VerificationDocument, TurfImage
from .decorators import player_required, owner_required, admin_required

User = get_user_model()


def homepage(request):
    """General landing page for all users."""
    turfs = Turf.objects.all()[:4]
    return render(request, 'homepage.html', {'turfs': turfs})


@player_required
def player_home(request):
    turfs = Turf.objects.all()[:4]
    return render(request, 'player_home.html', {'turfs': turfs})

@player_required
def player_dashboard(request):
    return render(request, 'playerdashboard.html')


@owner_required
def owner_home(request):
    turfs = Turf.objects.all()[:4]
    return render(request, 'owner_home.html', {'turfs': turfs})

@owner_required
def owner_dashboard(request):
    owner_turfs = Turf.objects.filter(owner=request.user).order_by('-created_at')

    context = {
        'owner_turfs': owner_turfs,
    }
    return render(request, 'ownerdashboard.html', context)


@player_required
def booking_history(request):
    bookings = request.user.turf_bookings.all().order_by('-created_at')
    return render(request, 'bookinghistorypage.html', {'bookings': bookings})

@admin_required
def admin_dashboard(request):
    from bookings.models import Booking

    context = {
        'total_turfs': Turf.objects.count(),
        'pending_turfs': Turf.objects.filter(status='pending').count(),
        'total_users': User.objects.count(),
        'total_bookings': Booking.objects.count(),
        'pending_verification_list': Turf.objects.filter(status='pending'),
    }
    return render(request, 'admindashboard.html', context)


@admin_required
def admin_verify_turf(request, turf_id):
    turf = get_object_or_404(Turf, id=turf_id)

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'approve':
            turf.status = 'approved'
            turf.rejection_reason = ''
            turf.save()
            messages.success(request, f'Turf "{turf.name}" has been approved.')
        elif action == 'reject':
            turf.status = 'rejected'
            turf.rejection_reason = request.POST.get('rejection_reason', '')
            turf.save()
            messages.success(request, f'Turf "{turf.name}" has been rejected.')
        return redirect('admin_dashboard')

    verification_documents = VerificationDocument.objects.filter(turf=turf).first()
    turf_images = TurfImage.objects.filter(turf=turf)

    context = {
        'turf': turf,
        'verification_documents': verification_documents,
        'turf_images': turf_images,
    }
    return render(request, 'turfverificationdetail.html', context)
