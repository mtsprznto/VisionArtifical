"""
NECESITA DOCKER PARA INICIAR ESTE SCRIPT

"""

from inference_sdk import InferenceHTTPClient


from dotenv import load_dotenv
import os



load_dotenv()

ROBO_FLOW_API_KEY = os.getenv("ROBO_FLOW_API_KEY")


client = InferenceHTTPClient(
    api_url="http://localhost:9001", # use local inference server
    api_key=ROBO_FLOW_API_KEY
)



results = client.run_workflow(
    workspace_name="wow-owpic",
    workflow_id="v0pruebaswflow",
    images={
        "image": "../data_raw/img/pruebas/pruebas/frame_00000.jpg"
    }
)
print(results[0])
classes = [pred["class"] for pred in results[0]["model_predictions"]["predictions"]]
print(classes)
