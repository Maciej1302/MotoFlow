from django.http import JsonResponse


def my_view(request):
    return JsonResponse({"message": "Hello from my new cars its django here!"})
