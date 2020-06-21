import sys
import numpy as np
import os
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

print("dodo")

image_fullpath = sys.argv[1]
image_path = sys.argv[2]
labels= sys.argv[3]

print(labels)
samples=len(labels)
fileSave = 'media/report1.pdf'
documentTitle = 'Report'
subTitle= 'Uploaded File:'

pdf = canvas.Canvas(fileSave)
pdf.setTitle(documentTitle)
pdf.drawString(270, 770, 'Report')

def drawMyRuler(pdf):
    pdf.drawString(100,810, 'x100')
    pdf.drawString(200,810, 'x200')
    pdf.drawString(300,810, 'x300')
    pdf.drawString(400,810, 'x400')
    pdf.drawString(500,810, 'x500')

    pdf.drawString(10,100, 'y100')
    pdf.drawString(10,200, 'y200')
    pdf.drawString(10,300, 'y300')
    pdf.drawString(10,400, 'y400')
    pdf.drawString(10,500, 'y500')
    pdf.drawString(10,600, 'y600')
    pdf.drawString(10,700, 'y700')
    pdf.drawString(10,800, 'y800') 
    
#drawMyRuler(pdf)
pdf.setFillColorRGB(0,0, 255)
pdf.drawString(120, 720, subTitle )
pdf.drawString(220, 720, image_path )
pdf.drawString(120, 650, "Result from the clustering algorithm is: {}".format(labels) )

pdf.line(30,710,550,710)

for i in range(samples):
    if(labels[i]!="]" and labels[i]!=" " and labels[i]!="["):
        n = 410 + 20*i
        text = pdf.beginText(120, n)
        text.setFillColor(colors.red)
        text.textLine("Prediction for {} sample is {}".format(i, labels[i]))
        pdf.drawText(text)
pdf.save()