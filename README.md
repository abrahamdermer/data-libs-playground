# Data Libraries Playground

Repo for students to learn popular Python libraries by topic: GIS, Image Processing, Audio/Speech, and NLP.

## How to use
1. Create a virtual environment (Windows PowerShell):
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
2. Open any folder under a topic and run the example script.

## Topics
- `gis/` → GeoPandas, ArcGIS (notes)
- `image/` → OpenCV, Pillow, scikit-image
- `audio/` → SpeechRecognition, Librosa, PyDub, PyAudio
- `nlp/` → NLTK, spaCy, TextBlob, Gensim

## Contributing
- Keep examples minimal and runnable.
- Each library folder should include:
  - `README.md` with: What it does, Install, Common tasks, Exercises.
  - `example_*.py` with short, commented code (Hebrew + English comments).
