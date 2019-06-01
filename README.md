# Face recognition CrowdCompute App using ageitgey/face_recognition

The face recognition python library can be found on github.com/ageitgey/face_recognition.

This app is running as an HTTP server. 

It gets images as an input and returns URL links of the faces in a JSON format.

## Build

-t flag tags the docker image with the name *face_reco*

```
docker build -t face_reco .
```

## Run

Docker image exposes port 3000. 

-p flag binds the port 3000 of the container to port 3000 on the host machine.

```
docker run -p 3000:3000 face_reco
```

## Web app

Call `localhost:3000/face_reco` to upload images.

Parameters:

**images** : The images you want face recognize