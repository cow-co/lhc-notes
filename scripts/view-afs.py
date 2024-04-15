import matplotlib.pyplot as plt
import argparse
import json

parser = argparse.ArgumentParser("lhc-afs-viewer")
parser.add_argument("schemefile", help="Path to an LHC filling scheme JSON file", type=str)
parser.add_argument("--separate", help="Plot schemes for each beam on separate graphs", action=argparse.BooleanOptionalAction)
args = parser.parse_args()

jsonFile = open(args.schemefile)
data = json.load(jsonFile)

bunchArr1 = data["schemebeam1"]
bunchArr2 = data["schemebeam2"]

if args.separate:
  figure, axis = plt.subplots(2, 1)
  axis[0].plot(bunchArr1, color='b') 
  axis[0].set_title("Beam 1 Filling Scheme") 
  axis[1].plot(bunchArr2, color='r') 
  axis[1].set_title("Beam 2 Filling Scheme") 
  plt.xlabel("Bucket Filling") 
  plt.ylabel("Bucket") 
  plt.show()
else:
  plt.xlabel("Bucket Filling") 
  plt.ylabel("Bucket") 
  plt.title(f'Filling Scheme {data["schemeName"]}') 
  plt.plot(bunchArr1, color='b', label="Beam 1")
  plt.plot(bunchArr2, color='r', label="Beam 2") 
  plt.legend() 
  plt.show()