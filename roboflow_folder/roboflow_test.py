from inference import InferencePipeline
from inference.core.interfaces.stream.sinks import render_boxes
import cv2

from dotenv import load_dotenv
import os


load_dotenv()

ROBO_FLOW_API_KEY = os.getenv("ROBO_FLOW_API_KEY")

# test_model_-m5b2g

MODEL_ID= "test_model_-m5b2g/6"


def mostrar_datos(result, video_frame):
    if result.get('output_image'):
        cv2.imshow("VIDEO", result['output_image'].numpy_image)
        cv2.waitKey(1)
    print(result)






pipeline = InferencePipeline.init(
    model_id=MODEL_ID,
    video_reference=0,
    on_prediction=mostrar_datos,
    api_key=ROBO_FLOW_API_KEY,
)
pipeline.start()

pipeline.join()

