# itemtask

Sample HTTP endpoint which collects the data about items in the cart.

### General information

I like the concept of thin views.
I treat Django Views as a place to deal with incoming/outcoming HTTP requests and refer to business logic from elsewhere to glue things together.
Serializers provided by DRF are used to validate dictionaries of data passed via HTTP.

I didn't write many unit tests because the task's requirements are largely simplified therefore doesn't require much custom logic.
Instead, I used built-in Django methods. Usage of `get_object_or_404` may seem like a bad idea but I accept this type of controlled coupling in Django.
 

### Development

To start development server you need to run:

```
docker-compose up --build
```

### Testing

To run tests you need to run:

```
docker-compose run --rm api pytest
``` 
