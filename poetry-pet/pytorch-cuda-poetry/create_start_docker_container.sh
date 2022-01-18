### Create Container

docker create -it -v /home/paresh/Code/Data-Science-Projects:/workspace --name nlp-dev pareshppp/pytorch_cuda11_poetry:19Nov21

### Start Container
# docker start <container-name>
# docker exec -it <container-name>

docker start -i nlp-dev
