import json

data_from_csv=[]

with open('data_set.txt', 'r') as f:data_from_txt = json.loads(f.read())

import csv

field_names=["brake","hand_brake","throttle","steer"]

def _parse_vehicle_keys(self, keys, milliseconds):

    driving_data = {}
    if keys[K_UP] or keys[K_w]:
        self._control.throttle = min(self._control.throttle + 0.01, 1)
    else:
        self._control.throttle = 0.0
    driving_data["throttle"] = self._control.throttle
    if keys[K_DOWN] or keys[K_s]:
        self._control.brake = min(self._control.brake + 0.2, 1)
    else:
        self._control.brake = 0
    driving_data["brake"] = self._control.brake
    self._control.hand_brake = keys[K_SPACE]
    driving_data["hand_brake"] = self._control.hand_brake
    
    steer_increment=0.0005*milliseconds
    if keys[K_LEFT] or keys[K_a]:
        if self._steer_cache>0:
            self._steer_cache=0
        else:
            self._steer_cache-=steer_increment
    elif keys[K_RIGHT] or keys[K_d]:
        if self._steer_cache<0:
            self._steer_cache=0
        else:
            self._steer_cache+=steer_increment
    else:
        self._steer_cache=0.0
    self._steer_cache=min(0.7,max(-0.7,self._steer_cache))
    self._control.steer=round(self._steer_cache,1)
    driving_data["steer"]=self._control.steer
    csv_file_store=open('project_227.csv','w',newline="")
    writer=csv.DictWriter(csv_file_store,fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data_from_txt)

    with open('project_227.csv', 'r') as file: reader = csv.reader(file)
    
    for row in file:
        data_from_csv.append(row)
        print(data_from_csv)