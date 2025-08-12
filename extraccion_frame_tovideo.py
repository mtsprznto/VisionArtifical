import cv2
from pathlib import Path
import logging
from tqdm import tqdm

def extract_frames(video_path: str, output_dir: str, image_format: str = 'jpg') -> None:
    # Configurar logging
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    # Validar rutas
    video_path = Path(video_path)
    output_dir = Path(output_dir)
    if not video_path.exists():
        logging.error(f"El archivo de video no existe: {video_path}")
        return
    output_dir.mkdir(parents=True, exist_ok=True)

    # Abrir video
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        logging.error(f"No se pudo abrir el video: {video_path}")
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    logging.info(f"Extrayendo {total_frames} frames de {video_path.name}")

    frame_idx = 0
    for _ in tqdm(range(total_frames), desc="Procesando frames"):
        ret, frame = cap.read()
        if not ret:
            logging.warning(f"Frame {frame_idx} no pudo ser leído. Deteniendo.")
            break

        frame_filename = output_dir / f"frame_{frame_idx:05d}.{image_format}"
        cv2.imwrite(str(frame_filename), frame)
        frame_idx += 1

    cap.release()
    logging.info(f"Extracción completada. Frames guardados en: {output_dir}")


OBJECTO = "pruebas"

FOLDER_VIDEO = f"./data_raw/video/{OBJECTO}"
FOLDER_IMG = f"./data_raw/img/{OBJECTO}"

extract_frames(f"{FOLDER_VIDEO}/{OBJECTO}.mp4", f"{FOLDER_IMG}/{OBJECTO}", image_format="jpg")
