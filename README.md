## RestAPi Emarkt Applction By Django Rest Frame Work

## download repo (لازم تكون محمل اداه git )
```bash
git clone https://github.com/JokerPython3/EmarktDjangoRestFrameWork
```


### download libary 
```bash
pip install -r requirements.txt
```


### Add DataBase Info in Settings.py 
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Yout DataBase Name',
        'USER': 'Your DateBase Username',
        'PASSWORD': 'Your DateBase Password',
        'HOST': 'Your Host',
        'PORT': 'Your Port',
    }
}
```

```bash
python manage.py makemigration
python manage.py migrate
```
## Run
```bash
python manage.py runserver
```
### Register
```http request
POST api/login/auth/register/
BODY {"username":"Atro","password":"123"}
{"data":{"created accounts Successfully"}}
```
### Login 
```http 
POST api/auth/login/
BODY {"username":"Atro","password":"123"}
{"data":{"access_token":"eJ...","refresh_token":"eJ...","atroooo":"atrp"}}
```
### Access Token Exiperd 1 Day
### Refresh Token Expierd 1 Day
### بقيه ريكوستات يعني بعد تسجيل دخول لازم بيها Access_token تحطه بي هيدارس

## Logout
```http request
POST api/logout/auth/atro/s1/ntro/
Authorization: Bearer <access_token>
{"data":{"message":"logout sucessfully"}}
```
## Update Username 
```http request
POST api/auth/update/username/account/
Authorization: Bearer <access_token>
Data : {"username1":"old username","username2":"يوزرك جوديد"}
{"data":{"username":"updated"}}
```
## Update Password
```http request
POST api/auth/update/password/account/
Authorization: Bearer <access_token>
data : {"password1":"old Password","password2":"new Password"}
{"data":{"message":"success"}}
```
## Product Show
```http request
GET api/auth/products/show/
Authorization: Bearer <access_token>
{
"product info"
}
```
###  بيها لايكات وشسمه  وتعليقات
### Search Of name
```http request
POST api/auth/serach/name/
Authorization: Bearer <access_token>
data : {"name":"name product"}
{
"data":{}
}
```
### اكو بحث عن طريق سعر و نوع منتج ه
### Like Add
```http request
POST api/auth/like/product/1/
Authorization: Bearer <access_token>
{"data":{"liked":1,"like_count":1}}
```
#### ال 1 هذا ايدي منتج
### Comment Add
```http request
POST api/auth/comment/atro/ntro/ss/1/
Authorization: Bearer <access_token>
{}
```
### Comment Update
```http request
PUT api/auth/comment/ss/1/
Authorization: Bearer <access_token>
{}
```
### Comment Delete
```http request
DELETE api/auth/comment/ss/1/
Authorization: Bearer <access_token>
{"data":{"success"}}
```
```java
class Atro{
    void ntro(){
        System.out.print("atro");
    }
}

public class Main Exstend Atro{
    @Ovvoirde 
    void ntro(){
        System.out.print("atro");
    }
}

```
# Built with PyCharm

