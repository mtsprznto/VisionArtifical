# Visión Artificial

![License](https://img.shields.io/badge/license-MIT-blue.svg)

Un conjunto de herramientas y módulos para procesamiento de imágenes y visión artificial utilizando tecnologías como YOLO, OpenCV y Roboflow.

## 📋 Descripción

Este proyecto contiene diversos módulos para el procesamiento de imágenes y visión artificial, incluyendo:

- Detección de billetes en tiempo real
- Estimación de poses humanas
- Extracción de frames de videos
- Integración con Roboflow para inferencia de modelos
- Monitoreo de tráfico

Cada módulo está diseñado para funcionar de manera independiente, permitiendo su uso en diferentes aplicaciones de visión artificial.

## 🚀 Estructura del Proyecto

```
├── data_raw/               # Datos brutos (imágenes y videos)
├── detect_bills/           # Detección de billetes con YOLO
├── detect_pruebas/         # Pruebas de detección
├── poses/                  # Estimación de poses humanas
├── roboflow_folder/        # Integración con Roboflow
├── traffic_monitor/        # Monitoreo de tráfico
└── extraccion_frame_tovideo.py  # Utilidad para extraer frames
```

## 🛠️ Módulos Principales

### Detección de Billetes

Utiliza YOLO para detectar billetes en tiempo real a través de la cámara web.

```bash
python detect_bills/main.py
```

### Estimación de Poses

Implementa modelos de YOLO para detectar poses humanas en imágenes.

```bash
python poses/poses_v0.py  # Procesamiento básico de poses
python poses/pose_img_opencv.py  # Visualización avanzada con OpenCV
```

### Integración con Roboflow

Proporciona herramientas para utilizar modelos de Roboflow para inferencia en imágenes y video.

```bash
python roboflow_folder/roboflow_img_inference.py  # Inferencia en imágenes
python roboflow_folder/roboflow_video_inference.py  # Inferencia en video
```

### Extracción de Frames

Utilidad para extraer frames de videos y guardarlos como imágenes.

```bash
python extraccion_frame_tovideo.py
```

## ⚙️ Requisitos

- Python 3.8+
- OpenCV
- Ultralytics YOLO
- Roboflow Inference SDK
- Docker (para algunos módulos de Roboflow)
- python-dotenv

Instala las dependencias con:

```bash
pip install ultralytics opencv-python inference-sdk python-dotenv tqdm
```

## 🔧 Configuración

Para los módulos que utilizan Roboflow, es necesario crear un archivo `.env` en la raíz del proyecto con la siguiente estructura:

```
ROBO_FLOW_API_KEY=tu_api_key_aquí
```

## 📈 Uso

Cada módulo puede ejecutarse de forma independiente. Consulta la sección de módulos principales para ver ejemplos de uso.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir los cambios que te gustaría realizar.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

## 📞 Contacto

Si tienes preguntas o sugerencias, no dudes en abrir un issue en este repositorio.