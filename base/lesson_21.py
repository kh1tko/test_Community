spoken = lambda greeting: greeting.title() + '.'
shouted = lambda greeting: greeting.upper() + '!'
whispered = lambda greeting: greeting.lower() + '.'

greet = lambda style, msg: style(msg)
msg = 'Hello World!'
print(greet(spoken(msg)))
