# Store

Access to Petstore orders

Find out more about our store: [http://swagger.io](http://swagger.io)

```python
store_controller = client.store
```

## Class Name

`StoreController`

## Methods

* [Get Inventory](../../doc/controllers/store.md#get-inventory)
* [Place Order](../../doc/controllers/store.md#place-order)
* [Get Order by Id](../../doc/controllers/store.md#get-order-by-id)
* [Delete Order](../../doc/controllers/store.md#delete-order)


# Get Inventory

Returns a map of status codes to quantities

```python
def get_inventory(self)
```

## Response Type

`dict`

## Example Usage

```python
result = store_controller.get_inventory()
print(result)
```


# Place Order

Place a new order in the store

```python
def place_order(self,
               id=None,
               pet_id=None,
               quantity=None,
               ship_date=None,
               order_status='approved',
               complete=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Form, Optional | - |
| `pet_id` | `long\|int` | Form, Optional | - |
| `quantity` | `int` | Form, Optional | - |
| `ship_date` | `datetime` | Form, Optional | - |
| `order_status` | [`OrderStatusEnum`](../../doc/models/order-status-enum.md) | Form, Optional | Order Status<br>**Default**: `'approved'` |
| `complete` | `bool` | Form, Optional | - |

## Response Type

[`Order`](../../doc/models/order.md)

## Example Usage

```python
id = 10

pet_id = 198772

quantity = 7

ship_date = dateutil.parser.parse('05/31/2023 00:00:00')

order_status = OrderStatusEnum.APPROVED

complete = True

result = store_controller.place_order(
    id,
    pet_id,
    quantity,
    ship_date,
    order_status,
    complete
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 405 | Invalid input | `APIException` |


# Get Order by Id

For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.

```python
def get_order_by_id(self,
                   order_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `long\|int` | Template, Required | ID of order that needs to be fetched |

## Response Type

[`Order`](../../doc/models/order.md)

## Example Usage

```python
order_id = 62

result = store_controller.get_order_by_id(order_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid ID supplied | `APIException` |
| 404 | Order not found | `APIException` |


# Delete Order

For valid response try integer IDs with value < 1000. Anything above 1000 or nonintegers will generate API errors

```python
def delete_order(self,
                order_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `long\|int` | Template, Required | ID of the order that needs to be deleted |

## Response Type

`void`

## Example Usage

```python
order_id = 62

result = store_controller.delete_order(order_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid ID supplied | `APIException` |
| 404 | Order not found | `APIException` |

