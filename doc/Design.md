# Common

## Entities

## Result

| Property | Data Type | Remark                                                       |
| -------- | --------- | ------------------------------------------------------------ |
| code     | Integer   | 0 success, 1 failed                                          |
| message  | String    | if the code equals 1 , this message will have the error information. otherwise it should be empty or null |
| data     | Object    | the data itself.                                             |



# user management

## entities

### user

All the properties are not null.

| Property    | Data Type | Remark                            |
| ----------- | --------- | --------------------------------- |
| id          | Integer   | auto increment by MySQL           |
| name        | String    |                                   |
| password    | String    |                                   |
| email       | String    |                                   |
| birth_date  | Date      |                                   |
| create_time | Date Time | maintained by MySQL automatically |
| update_time | Date Time | maintained by MySQL automatically |



## methods

| path                 | method | parameters                                                   | return | description |
| -------------------- | ------ | ------------------------------------------------------------ | ------ | ----------- |
| /user/sign-up        | POST   | user{<br />name,<br />password,<br />email,<br />birth_date} |        |             |
| /user/sign-in        | POST   | user{<br />password,<br />email}                             |        |             |
| /user/sign-out       | POST   | NONE                                                         |        |             |
| /user/delete-account | DEL    | NONE                                                         |        |             |



# Profile Management

## entities

### profile

| Property  | Data Type | Remark                          |
| --------- | --------- | ------------------------------- |
| id        |           |                                 |
| user_id   | integer   | foreign key  refer to user's id |
| weight    | float     | kilogram                        |
| height    | float     | mete                            |
| BMR       | integer   | Basal Metabolic  Rate           |
| chronic   | JSON      | List of names                   |
| allergies | JSON      | List of names                   |
| goals     | JSON      | List of names                   |



## methods

| path     | method | parameters | return | description |
| -------- | ------ | ---------- | ------ | ----------- |
| /profile | GET    |            |        |             |
| /profile | POST   | profile    |        |             |
|          |        |            |        |             |
|          |        |            |        |             |

# Food Log Management

## entities

### Food

all the fields are not null

| Property    | Data Type | Remark                            |
| ----------- | --------- | --------------------------------- |
| id          |           |                                   |
| user_id     | integer   | foreign key  refer to user's id   |
| name        | String    |                                   |
| quantity    | float     | grams or number                   |
| calories    | integer   |                                   |
| carbs       | integer   |                                   |
| protein     | integer   |                                   |
| fats        | integer   |                                   |
| create_time | Date Time | maintained by MySQL automatically |



### methods

| path     | method | parameters           | return | description                                                  |
| -------- | ------ | -------------------- | ------ | ------------------------------------------------------------ |
| /foodlog | GET    | filter and page info |        | query the list of the food, making sure the records sorted by create_time desc. |
| /foodlog | POST   | Food                 |        |                                                              |
| /diagram | GET    | filter by date range |        | will sum up calories, carbs, protein, and fats within the range by date. |
|          |        |                      |        |                                                              |



# Diet Plan

## enities

### plan

| Property    | Data Type | Remark                            |
| ----------- | --------- | --------------------------------- |
| id          |           |                                   |
| user_id     | integer   | foreign key  refer to user's id   |
| breakfast   | JSON      | List of text                      |
| lunch       | JSON      | List of text                      |
| snack       | JSON      | List of text                      |
| dinner      | JSON      | List of text                      |
| create_time | Date Time | maintained by MySQL automatically |

## methods

| path  | method | parameters           | return | description                                                  |
| ----- | ------ | -------------------- | ------ | ------------------------------------------------------------ |
| /plan | GET    | filter and page info |        | query the list of the plan sorted by create_time desc.       |
| /plan | POST   | budget               |        | generate a diet plan with budget and goals and healthy status |
|       |        |                      |        |                                                              |
|       |        |                      |        |                                                              |