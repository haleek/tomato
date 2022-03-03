from django.apps import AppConfig
import os
from tensorflow.keras.models import load_model
from django.conf import settings

class TomatoapiConfig(AppConfig):
    name = 'tomatoAPI'

class Predictator(AppConfig):
  
    model_name='modelFinal.h5'

    
    model_path = os.path.join(settings.MODEL_ROOT, model_name)
    
    model=load_model(model_path)
