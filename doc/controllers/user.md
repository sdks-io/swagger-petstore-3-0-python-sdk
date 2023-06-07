# User

Operations about user

```python
user_controller = client.user
```

## Class Name

`UserController`

## Methods

* [Create User](../../doc/controllers/user.md#create-user)
* [Create Users With List Input](../../doc/controllers/user.md#create-users-with-list-input)
* [Login User](../../doc/controllers/user.md#login-user)
* [Logout User](../../doc/controllers/user.md#logout-user)
* [Get User by Name](../../doc/controllers/user.md#get-user-by-name)
* [Update User](../../doc/controllers/user.md#update-user)
* [Delete User](../../doc/controllers/user.md#delete-user)


# Create User

This can only be done by the logged in user.

```python
def create_user(self,
               id=None,
               username=None,
               first_name=None,
               last_name=None,
               email=None,
               password=None,
               phone=None,
               user_status=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Form, Optional | - |
| `username` | `string` | Form, Optional | - |
| `first_name` | `string` | Form, Optional | - |
| `last_name` | `string` | Form, Optional | - |
| `email` | `string` | Form, Optional | - |
| `password` | `string` | Form, Optional | - |
| `phone` | `string` | Form, Optional | - |
| `user_status` | `int` | Form, Optional | User Status |

## Response Type

[`User`](../../doc/models/user.md)

## Example Usage

```python
id = 10

username = 'theUser'

first_name = 'John'

last_name = 'James'

email = 'john@email.com'

password = '12345'

phone = '12345'

user_status = 1

result = user_controller.create_user(
    id,
    username,
    first_name,
    last_name,
    email,
    password,
    phone,
    user_status
)
print(result)
```


# Create Users With List Input

Creates list of users with given input array

```python
def create_users_with_list_input(self,
                                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`List of User`](../../doc/models/user.md) | Body, Optional | - |

## Response Type

[`User`](../../doc/models/user.md)

## Example Usage

```python
result = user_controller.create_users_with_list_input()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | successful operation | `APIException` |


# Login User

Logs user into the system

```python
def login_user(self,
              username=None,
              password=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `string` | Query, Optional | The user name for login |
| `password` | `string` | Query, Optional | The password for login in clear text |

## Response Type

`string`

## Example Usage

```python
result = user_controller.login_user()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid username/password supplied | `APIException` |


# Logout User

Logs out current logged in user session

```python
def logout_user(self)
```

## Response Type

`void`

## Example Usage

```python
result = user_controller.logout_user()
print(result)
```


# Get User by Name

Get user by user name

```python
def get_user_by_name(self,
                    name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Template, Required | The name that needs to be fetched. Use user1 for testing. |

## Response Type

[`User`](../../doc/models/user.md)

## Example Usage

```python
name = 'name0'

result = user_controller.get_user_by_name(name)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid username supplied | `APIException` |
| 404 | User not found | `APIException` |


# Update User

This can only be done by the logged in user.

```python
def update_user(self,
               name,
               id=None,
               username=None,
               first_name=None,
               last_name=None,
               email=None,
               password=None,
               phone=None,
               user_status=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Template, Required | name that need to be deleted |
| `id` | `long\|int` | Form, Optional | - |
| `username` | `string` | Form, Optional | - |
| `first_name` | `string` | Form, Optional | - |
| `last_name` | `string` | Form, Optional | - |
| `email` | `string` | Form, Optional | - |
| `password` | `string` | Form, Optional | - |
| `phone` | `string` | Form, Optional | - |
| `user_status` | `int` | Form, Optional | User Status |

## Response Type

`void`

## Example Usage

```python
name = 'name0'

id = 10

username = 'theUser'

first_name = 'John'

last_name = 'James'

email = 'john@email.com'

password = '12345'

phone = '12345'

user_status = 1

result = user_controller.update_user(
    name,
    id,
    username,
    first_name,
    last_name,
    email,
    password,
    phone,
    user_status
)
print(result)
```


# Delete User

This can only be done by the logged in user.

```python
def delete_user(self,
               name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Template, Required | The name that needs to be deleted |

## Response Type

`void`

## Example Usage

```python
name = 'name0'

result = user_controller.delete_user(name)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid username supplied | `APIException` |
| 404 | User not found | `APIException` |

