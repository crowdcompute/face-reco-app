# Face recognition CrowdCompute App using ageitgey/face_recognition

The face recognition python library can be found on github.com/ageitgey/face_recognition.
This app is running as an HTTP server. 
It gets images as an input and returns URL links of the faces in a JSON format.

# Build

docker build -t face_reco .

# Run

docker run -p 3000:3000 --rm face_reco