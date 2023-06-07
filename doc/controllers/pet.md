# Pet

Everything about your Pets

Find out more: [http://swagger.io](http://swagger.io)

```python
pet_controller = client.pet
```

## Class Name

`PetController`

## Methods

* [Update Pet](../../doc/controllers/pet.md#update-pet)
* [Add Pet](../../doc/controllers/pet.md#add-pet)
* [Find Pets by Status](../../doc/controllers/pet.md#find-pets-by-status)
* [Find Pets by Tags](../../doc/controllers/pet.md#find-pets-by-tags)
* [Get Pet by Id](../../doc/controllers/pet.md#get-pet-by-id)
* [Update Pet With Form](../../doc/controllers/pet.md#update-pet-with-form)
* [Delete Pet](../../doc/controllers/pet.md#delete-pet)
* [Upload File](../../doc/controllers/pet.md#upload-file)


# Update Pet

Update an existing pet by Id

```python
def update_pet(self,
              name,
              photo_urls,
              id=None,
              category=None,
              tags=None,
              pet_status=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Form, Required | - |
| `photo_urls` | `List of string` | Form, Required | - |
| `id` | `long\|int` | Form, Optional | - |
| `category` | [`Category`](../../doc/models/category.md) | Form, Optional | - |
| `tags` | [`List of Tag`](../../doc/models/tag.md) | Form, Optional | - |
| `pet_status` | [`PetStatusEnum`](../../doc/models/pet-status-enum.md) | Form, Optional | pet status in the store |

## Response Type

[`Pet`](../../doc/models/pet.md)

## Example Usage

```python
name = 'doggie'

photo_urls = [
    'photoUrls5',
    'photoUrls6',
    'photoUrls7'
]

id = 10

tags = [
    Tag()
]

result = pet_controller.update_pet(
    name,
    photo_urls,
    id,
    tags
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid ID supplied | `APIException` |
| 404 | Pet not found | `APIException` |
| 405 | Validation exception | `APIException` |


# Add Pet

Add a new pet to the store

```python
def add_pet(self,
           name,
           photo_urls,
           id=None,
           category=None,
           tags=None,
           pet_status=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Form, Required | - |
| `photo_urls` | `List of string` | Form, Required | - |
| `id` | `long\|int` | Form, Optional | - |
| `category` | [`Category`](../../doc/models/category.md) | Form, Optional | - |
| `tags` | [`List of Tag`](../../doc/models/tag.md) | Form, Optional | - |
| `pet_status` | [`PetStatusEnum`](../../doc/models/pet-status-enum.md) | Form, Optional | pet status in the store |

## Response Type

[`Pet`](../../doc/models/pet.md)

## Example Usage

```python
name = 'doggie'

photo_urls = [
    'photoUrls5',
    'photoUrls6',
    'photoUrls7'
]

id = 10

tags = [
    Tag()
]

result = pet_controller.add_pet(
    name,
    photo_urls,
    id,
    tags
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 405 | Invalid input | `APIException` |


# Find Pets by Status

Multiple status values can be provided with comma separated strings

```python
def find_pets_by_status(self,
                       status='available')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`StatusEnum`](../../doc/models/status-enum.md) | Query, Optional | Status values that need to be considered for filter<br>**Default**: `'available'` |

## Response Type

[`List of Pet`](../../doc/models/pet.md)

## Example Usage

```python
status = StatusEnum.AVAILABLE

result = pet_controller.find_pets_by_status(
    status
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid status value | `APIException` |


# Find Pets by Tags

Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

```python
def find_pets_by_tags(self,
                     tags=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tags` | `List of string` | Query, Optional | Tags to filter by |

## Response Type

[`List of Pet`](../../doc/models/pet.md)

## Example Usage

```python
result = pet_controller.find_pets_by_tags()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid tag value | `APIException` |


# Get Pet by Id

Returns a single pet

```python
def get_pet_by_id(self,
                 pet_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pet_id` | `long\|int` | Template, Required | ID of pet to return |

## Response Type

[`Pet`](../../doc/models/pet.md)

## Example Usage

```python
pet_id = 152

result = pet_controller.get_pet_by_id(pet_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid ID supplied | `APIException` |
| 404 | Pet not found | `APIException` |


# Update Pet With Form

Updates a pet in the store with form data

```python
def update_pet_with_form(self,
                        pet_id,
                        name=None,
                        status=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pet_id` | `long\|int` | Template, Required | ID of pet that needs to be updated |
| `name` | `string` | Query, Optional | Name of pet that needs to be updated |
| `status` | `string` | Query, Optional | Status of pet that needs to be updated |

## Response Type

`void`

## Example Usage

```python
pet_id = 152

result = pet_controller.update_pet_with_form(pet_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 405 | Invalid input | `APIException` |


# Delete Pet

delete a pet

```python
def delete_pet(self,
              pet_id,
              api_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pet_id` | `long\|int` | Template, Required | Pet id to delete |
| `api_key` | `string` | Header, Optional | - |

## Response Type

`void`

## Example Usage

```python
pet_id = 152

result = pet_controller.delete_pet(pet_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid pet value | `APIException` |


# Upload File

uploads an image

```python
def upload_file(self,
               pet_id,
               additional_metadata=None,
               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pet_id` | `long\|int` | Template, Required | ID of pet to update |
| `additional_metadata` | `string` | Query, Optional | Additional Metadata |
| `body` | `typing.BinaryIO` | Form, Optional | - |

## Response Type

[`PetImage`](../../doc/models/pet-image.md)

## Example Usage

```python
pet_id = 152

result = pet_controller.upload_file(pet_id)
print(result)
```

