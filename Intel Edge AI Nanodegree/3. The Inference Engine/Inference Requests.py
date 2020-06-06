def async_inference(exec_net, input_blob, image):
    # Add code to perform asynchronous inference
    # Note: Return the exec_net
    exec_net.start_aync(request_id=0, inputs={input_blob:image})
    while True:
        status=exec_net.requests[0].wait(-1)
        if status == 0:
            break
        else:
            time.sleep(1)
    
    return exec_net

def sync_inference(exec_net, input_blob, image):
    # Add code to perform synchronous inference
    result=exec_net.infer(inputs={input_blob:image})

    return result