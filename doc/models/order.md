
# Order

## Structure

`Order`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Optional | - |
| `pet_id` | `long\|int` | Optional | - |
| `quantity` | `int` | Optional | - |
| `ship_date` | `datetime` | Optional | - |
| `order_status` | [`OrderStatusEnum`](../../doc/models/order-status-enum.md) | Optional | Order Status<br>**Default**: `'approved'` |
| `complete` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "id": 10,
  "petId": 198772,
  "quantity": 7,
  "shipDate": "05/31/2023 00:00:00",
  "orderStatus": "approved",
  "complete": true
}
```

