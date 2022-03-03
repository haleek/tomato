
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from tensorflow.keras.preprocessing import image
from django.shortcuts import render
from .apps import Predictator
import numpy as np
from rest_framework.parsers import MultiPartParser
# Create your views here.

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import views
import cv2
import numpy as np




tomato=['Bacterial spot', 'Early blight','Late Blight', 'Leaf Mold','Septoria Leaf Spot',
       'Spider Mites Two Spotted Spider Mite','Tomato Target Spot', 'Tomato Yellow Leaf Curl Virus',
       'Tomato mosaic virus', 'healthy']


class predict(views.APIView):
    parser_classes = (MultiPartParser,)

   
    

    def post(self, request):
        
        if 'file' in request.data:
        
                im= request.data['file']
                if im is not None:    
                    img = cv2.imdecode(np.fromstring(request.data['file'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
                    img = cv2.resize(img, (32, 32))
                    img=img.reshape(1,32,32,3)
                    img=img/255
                    res=tomato[Predictator.model.predict_classes(img)[0]]
                    return Response(res,status=200)
                
                else:
                    return Response({"message":"file is not recieved"},status=400)

        else:
            return Response({"message":"provide the image"},status=404)


      