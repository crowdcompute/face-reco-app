# Face recognition CrowdCompute App

This app is running as an HTTP server. 
It gets images as an input and returns URL links of the faces in a JSON format.

# Build and run

docker build -t face_reco .
docker run -p 3000:3000 --rm face_reco