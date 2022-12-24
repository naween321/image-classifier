import base64
from django.http import HttpResponse
from django.shortcuts import render

from heart.utils import classify_image as clssfy_image, load_saved_artifacts


def classify_image(request):
    if request.method == 'POST':
        context = {"name": "Please add picture"}
        file = request.FILES.get("file")
        if file:
            byte_code = file.read()
            en = base64.b64encode(byte_code)
            d = en.decode("utf-8")
            load_saved_artifacts()
            p = clssfy_image(en, None)
            if p:
                context = {"name": p[0]['class'].upper()}
            else:
                context = {"name": "Can't Recognize"}
        return render(request, 'classify.html', context=context)
    return render(request, 'classify.html')
