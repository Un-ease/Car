from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def home(request):
    context = {'link': 'style.css'}
    return render(request, 'web.html', context)

current_command = 'S'  # Default command is 'Stop'

@api_view(['POST'])
def send_command(request):
    """
    API endpoint to send a command to the ESP32 car.
    """
    global current_command
    command = request.data.get('command', None)
    
    if command in ['F', 'B', 'L', 'R', 'S']:  # Valid commands
        current_command = command
        return Response({'status': 'success', 'command': current_command})
    else:
        return Response({'status': 'error', 'message': 'Invalid command'}, status=400)

@api_view(['GET'])
def get_command(request):
    """
    API endpoint to retrieve the current command.
    """
    global current_command
    return Response({'status': 'success', 'command': current_command})