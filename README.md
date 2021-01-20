# Tinder like API using Django Rest Framework and PostgreSQL

One Paragraph of project description goes here

## Getting Started

git clone https://github.com/achilleburah/django-rest-framework-tinder-api/

pip install -r requirements.txt

### API ENDPOINTS

Register
/users/new
Login 
/api-auth/login/
Admin 
/admin

List profiles suggestions based on genre and radius
/users/proposals/?genre=F&radius__lte=5

List and create new match requests
/users/requests/

List User's matches
/users/matches/?user_id=2
