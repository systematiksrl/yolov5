from subprocess import Popen, PIPE

cmd = "python3 detect.py --weights best.pt --data data/dataset.yaml --img 1280 --conf 0.25 --source /home/kobayashi/Documents/job/yolov5/data/example.png"
process = Popen(cmd.split(), stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
print(stdout)

# python3 detect.py --weights best.pt --data data/dataset.yaml --img 1280 --conf 0.25 --source 0