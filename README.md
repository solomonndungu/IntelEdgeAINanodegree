# IntelEdgeAINanodegree
Is a folder containing the code practices that I've been doing based on the Intel Edge AI Nanodegree. It teaches about internet of things. Edge means local or near-local processing. The use of edge can come from a desire for real-time decision-making in certain applications.

Instructions for downloading and installing the intel Distribution of OpenVINO toolkit can be found here:

https://software.intel.com/content/www/us/en/develop/tools/openvino-toolkit/choose-download.html

The first folder (Leveraging Pre-Trained models) explains how to download pre-trained models so that you may use them for pre-processing before feeding it to the model optimizer for optimization. Then after downloading them you pre-process the models. Details pertaining to the leveraging and pre-processing (reshaping of height, width) can be found here:

https://software.intel.com/content/www/us/en/develop/tools/openvino-toolkit/pretrained-models.html

The second folder (The Model Optimizer) talks of how you can convert a tensorflow model into an Intermediate Representation (IR) for feeding into the Inference Engine. Documentation on how to use cmd to perform this optimization can be found in the link below:

https://docs.openvinotoolkit.org/2019_R3/_docs_MO_DG_prepare_model_convert_model_Convert_Model_From_TensorFlow.html

The third folder deals with the Inference Engine, which runs the actual inference on a model. You first feed an IR to inference engine,then run code to perform inference requests.
Documentation about using the IECore can be found here: https://docs.openvinotoolkit.org/2019_R3/classie__api_1_1IECore.html
Docs about IENetwork: https://docs.openvinotoolkit.org/2019_R3/classie__api_1_1IENetwork.html
Inference requests include synchronous requests (will wait and do nothing else until the inference response is returned, blocking the main thread) and asynchronous (when the response for a particular item takes a long time, you don't hold up the rest of your website or app from loading or operating appropriately. It means that other tasks may continue while waiting on the IE to respond)
Then finally you integrate all of the above knowledge into a running app.

The fourth folder has code about handling input streams and server communications.

Do enjoy!!!
