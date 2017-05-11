def make_readable(seconds):
    # Do something
    hours = int(seconds/(60.*60.))
    minutes = int((seconds-hours*60.**2)/60.)
    seconds_a = int(seconds-hours*60.**2-minutes*60.)
    
    return str(hours).zfill(2)+":"+str(int(minutes)).zfill(2)+":"+str(seconds_a).zfill(2)