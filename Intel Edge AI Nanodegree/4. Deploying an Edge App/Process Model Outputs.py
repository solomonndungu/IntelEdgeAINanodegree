counter = 0
incident_flag = False

def assess_scene(result, counter, incident_flag):
    '''
    Based on the determined situation, potentially send
    a message to the pets to break it up.
    '''
    if result[0][1] == 1 and not incident_flag:
        timestamp = counter / 30
        print("Log: Incident at {:.2f} seconds.".format(timestamp))
        print("Break it up!")
        incident_flag = True
    elif result[0][1] !=1:
        incident_flag = False

    return incident_flag

# Process the output
incident_flag = assess_scene(result, counter, incident_flag)