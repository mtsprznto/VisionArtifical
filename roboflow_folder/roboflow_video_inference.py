"""
PARA PARAR LA CAMARA APRETAR "3"
"""
# Import the InferencePipeline object
from inference import InferencePipeline
import cv2

from dotenv import load_dotenv
import os



load_dotenv()

ROBO_FLOW_API_KEY = os.getenv("ROBO_FLOW_API_KEY")


# Import the InferencePipeline object
from inference import InferencePipeline
import cv2

def my_sink(result, video_frame):
    if result.get("label_visualization"): # Display an image from the workflow response
        cv2.imshow("Workflow Image", result["label_visualization"].numpy_image)
        
        key = cv2.waitKey(1) & 0xFF  # Captura la tecla presionada
        if key == ord('3'):  # Si se presiona la tecla "3"
            print("🔴 Visualización detenida por el usuario (tecla 3)")
            cv2.destroyAllWindows()
            # Opcional: detener el pipeline si querés terminar todo
            os._exit(0)  # Fuerza la salida del programa (útil si estás en hilo)
            return  # Sale de la función sin seguir mostrando


        #cv2.waitKey(1)
    print(result) # do something with the predictions of each frame


# initialize a pipeline object
pipeline = InferencePipeline.init_with_workflow(
    api_key=ROBO_FLOW_API_KEY,
    workspace_name="wow-owpic",
    workflow_id="v0pruebaswflow",
    video_reference=0, # Path to video, device id (int, usually 0 for built in webcams), or RTSP stream url
    max_fps=30,
    on_prediction=my_sink
)
pipeline.start() #start the pipeline
pipeline.join() #wait for the pipeline thread to finish
