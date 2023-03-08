# PostExpress | Django/Flask | React
[code on gitlab](https://gitlab.com/juancamilosuarez3/postexpress)


https://user-images.githubusercontent.com/71409094/223773616-d1998930-5e21-45cc-8b35-dfdbb51de416.mp4



## 1. Introduction
### 1.1 Description

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

### 1.2 Main features
* Connect Django with MySQL with Docker
* User Endpoint with APIView
* Flask Setup with Docker
* Django Producer and Consumer
* Flask Producer and Consumer
* RabbitMQ
* Queue Service
### 1.3 Limitations & Unknowns
* Flask
* Connect Flask with Mysql
* flask Migrations
* React
* React Setup
## 2. Architecture
### 2.1 Data Base Structure
### Django Data Base (MySql)
![image](https://user-images.githubusercontent.com/71409094/223774501-62201e22-cb1d-4f43-abad-f6590586597a.png)


### Flask Data Base (MySql))
![image](https://user-images.githubusercontent.com/71409094/223774738-8ecce692-9c5c-4007-8e2c-9bb889ea5395.png)
### 2.2 System Context Diagram
![photo_2023-02-28_18-54-18](https://user-images.githubusercontent.com/71409094/222980510-c9f9387c-954e-4040-8af2-86ad6fc69d69.jpg)
## 3. Installing and running the project
### 3.1. [DjangoAdmin](https://gitlab.com/juancamilosuarez3/postexpress/-/tree/master/DjangoAdmin)
### 3.2. [MainFlask](https://gitlab.com/juancamilosuarez3/postexpress/-/tree/master/MainFlask)
