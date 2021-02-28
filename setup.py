from setuptools import setup

setup(
   name='Optical Character Recognition - OCR project',
   version='0.1',
   description='Read images with texts on it and process the text',
   author='Csaba Hermann',
   author_email='hcsabi98@gmail.com',
   packages=['ocr'],
   install_requires=[
       'numpy',
       'opencv-python',
   ],
   scripts=[]
)
