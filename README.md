# face-reco-app
Face recognition CrowdCompute Application that is running as a HTTP server. 
Gets images as an input and returns URL links of the faces.

How to build and run the docker container:

docker build -t face_reco .
docker run -p 3000:3000 --rm face_reco