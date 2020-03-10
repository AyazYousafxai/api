from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import request
import jsonpickle
import numpy as np
import cv2
import ast
import base64
import numpy as np
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@api_view(["POST"])
def kiran(vision_data):
	print(vision_data.method)
	if vision_data.method == 'POST':
		print("______")
		try:
			 shape = ast.literal_eval(vision_data.POST.get('shape'))
			 buffer = base64.b64decode(vision_data.POST.get('image'))
        # Reconstruct the image
			 img = np.frombuffer(buffer, dtype=np.uint8).reshape(shape)
			 # cv2.imshow('img',img)
			 # cv2.waitKey(0)
        # Process image
			 data = {
	        'name': 'Vitor',
	        'location': 'Finland',
	        'is_active': True,
	        'count': [[12,12,12,12],[2,2,2,2]]
   			 }
			 return JsonResponse(data)


		except ValueError as e:
			return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
