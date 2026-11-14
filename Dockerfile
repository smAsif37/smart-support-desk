# Hugging Face Spaces (Docker SDK, free CPU: 2 vCPU / 16 GB RAM). Works on any Docker host too.
FROM python:3.11-slim

RUN useradd -m -u 1000 user
ENV HOME=/home/user PATH=/home/user/.local/bin:$PATH HF_HOME=/home/user/.cache/huggingface \
    PYTHONUNBUFFERED=1 TOKENIZERS_PARALLELISM=false
ENV INDEX_DIR=/tmp/index
WORKDIR /home/user/app

COPY --chown=user requirements.txt .
USER user
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu \
 && pip install --no-cache-dir -r requirements.txt

# bake the two public models into the image so cold starts are fast
RUN python -c "from sentence_transformers import SentenceTransformer as S; S('sentence-transformers/all-MiniLM-L6-v2'); \
from transformers import pipeline; pipeline('sentiment-analysis', model='cardiffnlp/twitter-roberta-base-sentiment-latest')"

COPY --chown=user . .
# if no documents were committed, generate the fictional ShopEase sample policies
RUN ls docs/*.pdf >/dev/null 2>&1 || python scripts/make_sample_pdfs.py

EXPOSE 7860
CMD ["bash", "start.sh"]
