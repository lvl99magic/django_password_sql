from django.shortcuts import render
from urllib.parse import urlparse
from django.template import RequestContext, context

def index(request):
    if request.method == 'POST':
        print("hello")
        context = RequestContext(request)
        print(context)
    return render(request, 'hello/index.html')


# context_dict = {}
# return render_to_response('hello/index.html', context_dict, context)