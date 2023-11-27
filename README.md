# AF-117
## Arctic fox 117
### Get started
- Install Docker with the Compose plugin (see: https://docs.docker.com/compose/install/)
- Clone this project
  ```shell
  git clone https://github.com/vetus-dominus/AF-117.git
  ```
- Create and run Docker container
  ```shell
  cd AF-117
  docker compose build
  docker compose up -d
  ```
- Open the URL http://localhost/ in your browser
  You will be see Django REST framework dashboard.
  ![Django REST framework](_img/af-117.png)

### API overview
#### Book list
- Get all records - ```GET /booklist/```
- Get row by ID - ```GET /booklist/<ID>```
- Create new row - ```POST /booklist/```
- Modify record - ```PUT /booklist/<ID>```
- Delete record - ```DELETE /booklist/<ID>```
#### Book list
- Get all records - ```GET /users/```
- Get row by ID - ```GET /users/<ID>```
- Create new row - ```POST /users/```
- Modify record - ```PUT /users/<ID>```
- Delete record - ```DELETE /users/<ID>```

For overview features we recommended use Django REST framework (http://localhost/)
