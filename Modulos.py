from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter import messagebox
import tkinter as tk
import win32com.client as win32
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser
from tkcalendar import *
from datetime import datetime
import calendar
from pathlib import Path
import os
import pyodbc
import cx_Oracle
from time import sleep
#import matplotlib.pyplot as plt
import numpy as np
hiddenimports=["tkinter.ttk", "tkinter.font"]



