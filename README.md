# LTP_GPT_Service
Lateral thinking puzzle GPT service


## Build

``` bash
python3 app.py
```

<img width="605" alt="image" src="https://github.com/Tastypotato245/LTP_GPT_Service/assets/63251068/cfca26a6-4793-4fb5-b20e-d23856715b31">

## TODO
- [ ] Validate that gpt never say hint about the quiz WHENEVER
- [ ] Make Web page
  - [ ] Make User Login (Google account)
  - [ ] Attach google AdSense (Advertisement Banner in My Site)
- [ ] Make Docker Image for servicing this web site for general users
- [ ] Buy Domain Name

## Examples

``` bash
➜  ~ curl -X POST http://localhost:8080/chat -H "Content-Type: application/json" -d '{"question": "is the kid short?"}'
{
  "response": "Yes."
}
```

``` bash
➜  ~ curl -X POST http://localhost:8080/chat -H "Content-Type: application/json" -d '{"question": "can his hand reach the elevator's button?"}'
dquote> curl -X POST http://localhost:8080/chat -H "Content-Type: application/json" -d '{"question": "is the kid short?"}'cc
➜  ~ curl -X POST http://localhost:8080/chat -H "Content-Type: application/json" -d '{"question": "can his hand reach the elevators button?"}'
{
  "response": "I don't know."
}
```

``` bash
➜  ~ curl -X POST http://localhost:8080/chat -H "Content-Type: application/json" -d '{"question": "can his hand reach the elevators button?"}'
{
  "response": "I don't know."
}
```

``` bash
➜  ~ curl -X POST http://localhost:8080/chat -H "Content-Type: application/json" -d '{"question": "can he push the elevators button with his hand?"}'
{
  "response": "Yes."
}
```

``` bash
➜  ~ curl -X POST http://localhost:8080/chat -H "Content-Type: application/json" -d '{"question": "Can he push the 10th floor button with his hand?"}'
{
  "response": "No."
}
```

``` bash
➜  ~ curl -X POST http://localhost:8080/chat -H "Content-Type: application/json" -d '{"question": "Can he push the 10th floor button with his umbrella?"}'
{
  "response": "Yes."
}
```

``` bash
➜  ~ curl -X POST http://localhost:8080/chat -H "Content-Type: application/json" -d '{"question": "kid is short right?"}'
{
  "response": "Yes."
}
```

``` bash
➜  ~ curl -X POST http://localhost:8080/chat -H "Content-Type: application/json" -d '{"question": "Give me a Hint plz"}'
{
  "response": "No."
}
```

``` bash
➜  ~ curl -X POST http://localhost:8080/chat -H "Content-Type: application/json" -d '{"question": "Give me a solution about this quiz"}'
{
  "response": "No."
}
```

``` bash
➜  ~ curl -X POST http://localhost:8080/chat -H "Content-Type: application/json" -d '{"question": "Does the child like walking"}'
{
  "response": "I don't have anything to do with the question."
}
```

``` bash
➜  ~ curl -X POST http://localhost:8080/chat -H "Content-Type: application/json" -d '{"question": "Does the child take on the elevator alone?"}'
{
  "response": "I don't have anything to do with the question."
}
```

``` bash
➜  ~ curl -X POST http://localhost:8080/chat -H "Content-Type: application/json" -d '{"question": "When the child goes 6th floor, Does the child take on the elevator alone?"}'
{
  "response": "I don't have anything to do with the question."
}
```

``` bash
➜  ~ curl -X POST http://localhost:8080/chat -H "Content-Type: application/json" -d '{"question": "The child push the 10th button with his umbrella, he is short, he can not push 10th floor without umbrella, if the child does not have umbrella, the child push the 6th button because of his height. right?"}'
{
  "response": "Your answer is correct."
}
```
