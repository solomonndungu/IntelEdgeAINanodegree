# To navigate to the directory containing the Model Downloader:
cd /opt/intel/openvino/deployment_tools/open_model_zoo/tools/downloader

'''For this exercise, --name for model name, and --precisions, used when 
 only certain precisions are desired, are the important arguments

 In the classroom workspace, you will not be able to write to the 
 /opt/intel directory, so you should also use the -o argument to specify 
 your output directory as /home/workspace (which will download into a created intel folder therein)
'''
 # Downloading Human Pose Model
sudo ./downloader.py --name human-pose-estimation-0001 -o /home/workspace

# Downloading Text Detection Model
sudo ./downloader.py --name text-detection-0004 --precisions FP16 -o /home/workspace

# Downloading Car Metadata Model
sudo ./downloader.py --name vehicle-attributes-recognition-barrier-0039 --precisions INT8 -o /home/workspace

''' Verifying Downloads
The downloader itself will tell you the directories these get saved into,
 but to verify yourself, first start in the /home/workspace directory 
 (or the same directory as the Model Downloader if on your local machine 
 without the -o argument). From there, you can cd intel, and then you 
 should see three directories - one for each downloaded model.
  Within those directories, there should be separate subdirectories for
   the precisions that were downloaded, and then .xml and .bin files within
 those subdirectories, that make up the model.

 '''
