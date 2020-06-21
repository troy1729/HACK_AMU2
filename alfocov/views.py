import requests
import os
from django.db import models
from django.utils.text import slugify
from django.dispatch import receiver
from django.shortcuts import render
import subprocess
from sklearn.cluster import KMeans
import sys
from subprocess import run,PIPE
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import pickle
import glob
clusterer = pickle.load(open('models/clust.pkl', 'rb'))
import pandas as pd

def button(request):
    return render(request,'a.html')
def external(request):
    files = glob.glob('media/*.csv')
    for f in files:
        os.remove(f)
    file = glob.glob('media/*.pdf')
    for f in file:
        os.remove(f)
    audi=request.FILES['file']
    print("csv is ",audi)
    fs=FileSystemStorage()
    filename=fs.save(audi.name,audi)
    fileurl=fs.open(filename)
    templateurl=fs.url(filename)
    print("file raw url",filename)
    print("file full url", fileurl)
    print("template url",templateurl)
    print("dodo")
    print("dodo")
    table = pd.read_csv(filename)
    clusterer = KMeans(n_clusters=5,random_state=10).fit(table)
    centers = clusterer.cluster_centers_
    labels= clusterer.predict(table)
    aud = subprocess.Popen([sys.executable,'models\\hamu.py',str(fileurl),str(filename),str(labels)],shell=False,stdout=PIPE)
    aud.communicate()
    print("dodo")
    print(aud.stdout)
    return render(request,'a.html',{'raw_url':templateurl,'edit_url':aud.stdout})
    