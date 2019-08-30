import os

DEBUG = False
SECRET_KEY = 'topsecret'
# SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_DATABASE_URI = os.environ['postgres://ekklnezbbhkmrr:b233fdf5e51a781d0654cb8313b3b44fee212e64ad9ce4e50814e18ab884a21f@ec2-50-16-197-244.compute-1.amazonaws.com:5432/d3bti8ale1evlo']
SQLALCHEMY_TRACK_MODIFICATIONS=False