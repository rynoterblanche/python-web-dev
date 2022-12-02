This is a starter repo for python web development that aims to use clean architecture and DDD principles to separate 
core business logic from implementation details such as data sources and web frameworks.

This repo aims to use Django and FastAPI as examples of 2 different frameworks that could depend on the same core domain 
entities & abstractions

## The Goal
Decouple the high level policy that is your business logic from all other details in your system. Web frameworks, APIs, 
UIs, data sources & even cloud platforms are all details that your business logic should not have to depend on.

## The Benefits
- core domain logic can become reusable across your entire software ecosystem
- improve testability, extensibility & readability of your core domain implementation
- enhance the versioning & release capabilities of your domain logic
- plug in different infrastructure details (UIs, APIs, data sources etc.) without affecting your core domain
- adjust your architecture between monolith, SOA or microservices more easily

## The Motivation
Some might find this architectural approach an overkill for smaller, self-contained projects. However, in my experience
I have seen time and time again that even the smallest business critical application can eventually grow to become 
unmanageable with bad architectural design. Following clean architecture and DDD principles early on can help prevent 
this.

### Sources Of Inspiration:

https://www.youtube.com/watch?v=o_TH-Y78tt4

https://www.youtube.com/watch?v=DJtef410XaM
https://rhodesmill.org/brandon/slides/2014-07-pyohio/clean-architecture/

https://medium.com/21buttons-tech/clean-architecture-in-django-d326a4ab86a9

https://sdediego.hashnode.dev/django-clean-architecture

https://breadcrumbscollector.tech/python-the-clean-architecture-in-2021/