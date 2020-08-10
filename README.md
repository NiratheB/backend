# Backend

Features:
- Create Model
    - Send POST request to /models
- Get Models
    - Send GET resuets to /models
    
## Data Structure:
  - Shape:
      - type
      - color
      - attributes</br>
   Example: A green sphere of radius 2:</br>
      Shape(type = 1, color = '00ff00', attributes= {'radius': 2})
   
 ## Usage:
  - Build the docker-compose file
  - Run docker-compose-up
  - Go to web container and migrate using python manage.py migrate
  
