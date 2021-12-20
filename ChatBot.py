from random import randrange


knowledge_base = [
    ["hey",
     [
         "Hey there!"
     ]
     ],
    ["what is your name",
     [
         "My name is JAC",
         "You can call me JAC"
     ]
     ],

    ["what is your age",
     [
         "I'm just a few days old",
         "I'm just a computer program; I don't have any age"
     ]
     ],

    ["how are you",
     [
         "I'm fine, thank you for asking!",
         "I'm fine, how are you?",
         "Everything is going well"
     ]
     ],

    ["I’m fine",
     [
         "Nice to hear that",
         "Great!!!",
         "Awesome!!!"
     ]
     ],

    ["how is the weather",
     [
         "There are high chances of rain",
         "It's very cold, currently, due to the frequent rains"
     ]
     ]
]


def Converse(User):
    if User in dict(knowledge_base):
        print("JAC -> ", dict(knowledge_base)[User][randrange(0, len(dict(knowledge_base)[User]))])
    else:
        print("JAC -> I don't understand, sorry")



