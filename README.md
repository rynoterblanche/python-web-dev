This is a starter repo for python web development that aims to use clean architecture and DDD principles to separate 
core business logic from implementation details such as data sources and web frameworks.

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