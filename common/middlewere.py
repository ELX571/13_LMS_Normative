import time

from django.shortcuts import render

request_history = {}


class RateLimiter:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        current_time = time.time()

        ip = request.META.get('REMOTE_ADDR')

        times = request_history.get(ip, [])

        times = [t for t in times if current_time - t < 10]

        times.append(current_time)

        request_history[ip] = times

        if len(times) > 5:
            return render(request, 'error.html',status=429)

        response = self.get_response(request)

        return response