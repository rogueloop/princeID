# !pip install roboflow
# !pip install ultralytics==8.0.196


from roboflow import Roboflow
rf = Roboflow(api_key="WihKS3LuF8Y10kqS1ozX")
project = rf.workspace("vi-8ob6k").project("id-card-detection-dccsg")
version = project.version(1)
dataset = version.download("yolov8")
