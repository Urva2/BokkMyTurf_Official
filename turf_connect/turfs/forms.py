from django import forms
from .models import Turf

# Facility choices matching addturf.html checkbox values
FACILITY_CHOICES = [
    ('parking', 'Parking'),
    ('floodlights', 'Floodlights'),
    ('changing-room', 'Changing Room'),
    ('washroom', 'Washroom'),
    ('drinking-water', 'Drinking Water'),
    ('first-aid', 'First Aid'),
    ('cafeteria', 'Cafeteria'),
    ('wifi', 'WiFi'),
    ('equipment-rental', 'Equipment Rental'),
    ('showers', 'Showers'),
    ('seating-area', 'Seating Area'),
    ('cctv', 'CCTV Surveillance'),
]


class AddTurfForm(forms.ModelForm):
    """Form for turf owners to submit a new turf listing."""

    # -- Override facilities as MultipleChoiceField (model stores JSON) --
    facilities = forms.MultipleChoiceField(
        choices=FACILITY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    # -- Extra field: image URLs (not part of Turf model) --
    image_urls = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'https://example.com/image1.jpg',
            'rows': 3,
        }),
        required=False,
    )

    # -- Verification document fields (not part of Turf model) --
    identity_proof = forms.FileField(required=True)
    ownership_agreement = forms.FileField(required=True)
    municipal_permission = forms.FileField(required=True)
    gst_certificate = forms.FileField(required=False)

    class Meta:
        model = Turf
        fields = [
            'name',
            'city',
            'state',
            'address',
            'google_maps_url',
            'description',
            'facilities',
            'additional_facilities',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g., Green Arena Sports Complex',
            }),
            'city': forms.TextInput(attrs={
                'placeholder': 'e.g., Mumbai',
            }),
            'state': forms.TextInput(attrs={
                'placeholder': 'e.g., Maharashtra',
            }),
            'address': forms.TextInput(attrs={
                'placeholder': 'Enter complete address with landmarks',
            }),
            'google_maps_url': forms.URLInput(attrs={
                'placeholder': 'https://maps.google.com/...',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe your turf - surface type, unique features...',
                'maxlength': 500,
                'rows': 4,
            }),
            'additional_facilities': forms.TextInput(attrs={
                'placeholder': 'e.g., Referee service, Ball rental, Coaching',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # If editing an existing turf, make doc fields optional
        if self.instance and self.instance.pk:
            self.fields['identity_proof'].required = False
            self.fields['ownership_agreement'].required = False
            self.fields['municipal_permission'].required = False
