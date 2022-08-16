
from nltk.chat.util import Chat, reflections
#Pairs is a list of patterns and responses.
pairs = [
    [
        r"Bonjour",
        ["Bonjour, ca va?",]
    ],
    [
        r"ca va et toi?",
        ["Ca va merci", "ca va mais je suis tres fatigué", "moi aussi ca va"]
    ],
    [
        r"ca va toi?",
        ["Ca va merci", "ca va mais je suis tres fatigué", "moi aussi ca va"]
    ],
     [
        r"Tu t'appelle comment?", 
        ["Je m'apelle Botif et je suis ravis de parler avec toi!","Je suis Botif, enchante!", "Je suis Botif, et toi?"]
    ],
    [
        r"Tu peux parler anglais?",
        ["Yes of course, i can speak in english if you want!"]
       
    ],
    [
        r"J'aime bien programmation(.*)",
        ["Moi aussi!",]
    ],
    [
        r"Je suis un human",
        ["Eh, moi non!",]
    ],
    [
        r"Coucou",
        ["Hello", "Coucou!",]
    ],
    [
        r"qu'est ce que (.*) veut ?",
        ["Alors, moi aussi je n'ai pas compris mais tous les monde veut quelque chose",]
        
    ],
    [
        r"(.*)qui t'as creé? (.*)",
        ["Elifsu ","Je pense tu le sais deja ;) ",]
    ],
    [
        r"bye",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['Oui. Tu peut parler avec moi!']
    ],
    [
        r"tu fais quoi?",
        ["Rien, j'attends pour parler avec quelqu'un! et toi?"]
    ],
    [
        r"rien et toi?",
        ['Ah, mais il faut faire quelque chose la']
    ],
]
chat = Chat(pairs, reflections)
chat.converse()

