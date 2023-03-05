# PostExpress

## 1. Description

This project consists of developing a web page that allows users to make posts. 
The main focus is on the use of microservices implemented with technologies such as Django, 
Flask, and RabbitMQ. Each microservice will be independent and have a specific functionality. 
RabbitMQ, a messaging tool that allows message exchange between applications, 
will be used for communication between the microservices.

Each service will be hosted in a separate Docker container, providing flexibility and scalability 
to the project. Docker Compose will be used to manage the containers, allowing for easy configuration 
and project management.

Communication between services will be done through RabbitMQ message queues. Each service will 
be configured to listen on a specific queue, allowing it to receive messages from other services. 
Additionally, services can send messages to other queues to notify other services of changes or results.

## 2. Architecture
![photo_2023-02-28_18-54-18](https://user-images.githubusercontent.com/71409094/222980510-c9f9387c-954e-4040-8af2-86ad6fc69d69.jpg)
## 3. Installing and running the project
### 3.1. [DjangoAdmin](https://gitlab.com/juancamilosuarez3/postexpress/-/tree/master/DjangoAdmin)
### 3.2. [MainFlask](https://gitlab.com/juancamilosuarez3/postexpress/-/tree/master/MainFlask)