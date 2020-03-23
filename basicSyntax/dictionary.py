sprint = {'swimming': '750m', 'biking': '20km', 'running': '5km'}

triatlhon_distances = {'sprint': {'swimming': '750m', 'biking': '20km', 'running': '5km'}, 'olympic':{
    'swimming': '1500m', 'biking': '40km', 'running': '10km'}}
sprint_running_distance = triatlhon_distances['sprint']['running']
print(sprint_running_distance)
print(sprint.keys())
print(triatlhon_distances.values())

sprint_copy = sprint.copy()
print(sprint_copy)

print(sprint.pop('biking'))
print(sprint)
print(sprint["biking"])