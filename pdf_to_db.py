import os
import requests
import PyPDF2
from tqdm import tqdm
from spacy.lang.en import English
import re
from sentence_transformers import SentenceTransformer


#import PDF

pdf_path = "harry-potter.pdf"
print(f"File {pdf_path} exists.")

#Geting Pages and Texts


