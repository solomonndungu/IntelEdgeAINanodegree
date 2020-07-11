# Set up paths so we can run Dev Cloud utilities:
# run this every time you enter a Workspace session
%env PATH=/opt/conda/bin:/opt/spark-2.4.3-bin-hadoop2.7/bin:/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/intel_devcloud_support
import os
import sys
sys.path.insert(0, os.path.abspath('/opt/intel_devcloud_support'))
sys.path.insert(0, os.path.abspath('/opt/intel'))

"""

We will be using the vehicle-license-plate-detection-barrier-0106 model
for this exercise. Remember that to run a model on the IGPU, we need to
use FP16 as the model precision.

"""

# We will be using the following filepath during the job submission:
/data/models/intel/vehicle-license-plate-detection-barrier-0106/FP16/vehicle-license-plate-detection-barrier-0106

"""

The first step is to create a Python script that you can use to load
the model and perform an inference. I have used the %%writefile magic command to
create a Python file called load_model_to_device.py. This will create a new Python file
in the working directory.

"""

%%writefile load_model_to_device.py

import time
from openvino.inference_engine import IECore
import argparse

def main(args):
    model=args.model_path
    model_weights=model+'.bin'
    model_structure=model+'.xml'

    start=time.time()

    core = IECore()
    model = core.read_network(model=model_structure, weights=model_weights)
    net = core.load_network(network=model, device_name=args.device, num_requests=1)

    print(f"Time taken to load model = {time.time()-start} seconds")

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--model_path', required=True)
    parser.add_argument('--device', default=None)

    args=parser.parse_args()
    main(args)

"""
%%writefile magic command creates a shell script called load_gpu_model_job.sh

Creating a Job Submission Script
The script does a few things:
1. Writes stdout and stderr to their respective .log files
2. Creates the /output directory
3. Creates DEVICE and MODELPATH variables and assigns their value as the first and second argument passed to the shell script
4. Calls the Python script using the MODELPATH and DEVICE variable values as the command line argument
5. Changes to the /output directory
6. Compresses the stdout.log and stderr.log files to output.tgz

"""

%%writefile load_gpu_model_job.sh

exec 1>/output/stdout.log 2>/output/stderr.log

mkdir -p /output

DEVICE=$1
MODELPATH=$2

# Run the load model python script
