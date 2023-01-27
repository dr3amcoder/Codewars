# Codewars How good are you really?

def better_than_average(class_points, your_points):
    peers_ts = sum(class_points) / len(class_points)
    
    return True if your_points > peers_ts else False