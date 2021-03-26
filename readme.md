API DOCS -


GET TASKS - http://127.0.0.1:8000/rest/tasks/ 
Method - GET
Response - [
    {
        "id": 3,
        "task_type": 3,
        "task_desc": "Sample New Test"
    },
    {
        "id": 1,
        "task_type": 3,
        "task_desc": "Sample Updated"
    }
]

CEATE TASK - http://127.0.0.1:8000/rest/tasks/
Method - POST
payload={'task_type': '2', 'task_desc': 'Adding Example Task'}
Instruction - task_type will only accept any of [1,2,3], for the value which is not in list it'll raise error
Response - 
{
        "id": 4,
        "task_type": 2,
        "task_desc": "Adding Example Task"
},


UPDATE TASK - http://127.0.0.1:8000/rest/tasks/{id}
Method - PUT/PATCH
payload={'task_type': '3', 'task_desc': 'Adding Example Task Updated'}
Response - 
{
        "id": 4,
        "task_type": 3,
        "task_desc": "Adding Example Task Updated"
}


CEATE TASK TRACKER - http://127.0.0.1:8000/rest/tasks-tracker/
Method - POST
payload=    {
        "task_type": 2,
        "update_type": 1,
        "email": "Sample@gmail.com"
    }
Instruction - update_type will only accept any of [1,2,3], for the value which is not in list it'll raise error
              task_type will only accept any of [1,2,3], for the value which is not in list it'll raise error
Response - 
{
        "id": 2,
        "task": 2,
        "update_type": 1,
        "email": "Sample@gmail.com"
}



UPDATE TASK TRACKER - http://127.0.0.1:8000/rest/tasks-tracker/{id}
Method - PUT?PATCH
payload=    {
        "id" : 2,
        "task_type": 2,
        "update_type": 1,
        "email": "Sample@gmail.com"
    }
Instruction - update_type will only accept any of [1,2,3], for the value which is not in list it'll raise error
              task_type will only accept any of [1,2,3], for the value which is not in list it'll raise error
Response - 
{
        "id": 2,
        "task": 2,
        "update_type": 1,
        "email": "Sample@gmail.com"
}