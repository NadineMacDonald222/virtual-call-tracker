from django.shortcuts import render
from rest_framework import viewsets
from .models import CallLog
from .serializer import CallLogSerializer

# --- API ViewSet (existing) ---
class CallLogViewSet(viewsets.ModelViewSet):
    queryset = CallLog.objects.all()
    serializer_class = CallLogSerializer

# --- Dashboard View (new) ---
def dashboard(request):
    calls = CallLog.objects.all().order_by('-created_at')  # show latest first
    return render(request, 'tracker/call_dashboard.html', {'calls': calls})

