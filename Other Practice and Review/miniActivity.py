
def get_hedons_per_min(activity):
    if activity == "jumping":
        hedons_per_min = 1
    elif activity == "swimming" and (cur_minutes - last_non_rest >= 60):
        hedons_per_min = 2
    else:
        hedons_per_min = 0
    return hedons_per_min

def perform_activity(activity, duration):
    global cur_hedons, cur_minutes, last_non_rest
    hedons_per_min = get_hedons_per_min(activity)
    
    cur_hedons += hedons_per_min * duration
    cur_minutes += duration
    
    if activity != "resting":
        last_non_rest = cur_minutes
        
def print_cur_hedons():
    print("current hedons:", cur_hedons)

def initialize():
    global cur_hedons, cur_minutes, last_non_rest
    cur_hedons = 0
    cur_minutes = 0
    last_non_rest = -100 #keep track of the end of the last non-rest activity
        
if __name__ == '__main__':

    initialize()
    perform_activity("jumping", 13) #13
    perform_activity("resting", 7) #0
    perform_activity("swimming", 1) #3
    print_cur_hedons()