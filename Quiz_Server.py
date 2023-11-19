# creating a quiz server using socket programming

import socket
from threading import Thread
import random

questions = [
"What is the Italian word for PIE? \n a.Mozarella\n b. Pasty\n c.patty\n d.Pizza",
"Water boils at 212 Units at which scale? \n a.Fahrenheit\n b.Celsius.in c.Rankine\n d.Kelvin",
"Which sea creature has three hearts? \n a.Dolphin\n b.Octopus\n Walrus n.d.Seal"
"Who was the character famous in our childhood rhymes associated with a Lamb? \n a.Mary\n b. Jack\n c.Johnny\n d.Mukesh",
"How many bones does an adult human have? \n a.206\n b.208\n c.201\n d.196",
"How many wonders are there in the world? \n a.7\n b.8\n c.10\n d.4",
"What element does not exist? \n_a.Xf\n b.Re\n c.Si \n d. Pa",
"How many states are there in India? \n a.24\n b.29\n c.30\n d.31",
"Who invented the telephone? \n a.A.G Bell\n b. John Wick \n c. Thomas Edison\n d.G Marconi",
"Who is Loki? \n a.God of Thunder\n b.God of Dwarves\n c.God of Mischief\n d.God of Gods",
"Who was the first Indian female astronaut? \n a. Sunita Williams\n b.Kalpana Chawla\n c.None of them\n d.Both of them",
"What is the smallest continent? \n a.Asia\n b.Antarctic\n c.Africa\n d. Australia",
"The beaver is the national embelem of which country? \n a.Zimbabwe\n b.Iceland\n c. Argentina\n d.Canada",
"How many players are on the field in baseball? \n a.6\n b.7\n c.9\n d.8",
'Hg stands for? \n a.Mercury\n b.Hulgerium\n c.Argenine\n d.Halfnium',
"Who gifted the Statue of Libery to the US? \n a.Brazil\n b.France\n c.Wales\n d.Germany",
" Which planet is closest to the sun? \n a.Mercury\n b. Pluto\n c.Earth\n d.Venus"
]

answers = ['d', 'a', 'b', 'a', 'a', 'a', 'a', 'b', 'a', 'c', 'b', 'd', 'd', 'c', 'a', 'b', 'a']

server = socket.socket(socket.SOCK_STREAM, socket.AF_INET)

address = "127.0.0.1"
port = 8000

server.bind((address, port))
server.listen()

clients = []

def getrandomquestionanswer(connected):
    random_index = random.randint(0, len(questions), -1)
    random_question = questions[random_index]
    random_answer = answers[random_index]
    connected.send(random_question.encode('utf-8'))

def remove(conn):
    pass

def remove_question(index):
    questions.pop(index)
    answers.pop(index)

def clientthread(connected, address):
    score = 0
    connected.send('Welcome to this quiz game'.encode('utf-8'))
    connected.send("You'll recieve a question. The answer should be a, b, c or d".encode('utf-8'))
    connected.send('Good Luck!\n\n'.encode('utf-8'))

    index, question, answer = getrandomquestionanswer(connected)
    while True:
        try:
            message = connected.recv(2048).encode('utf-8')
            if message:
                if message.lower() == answer:
                    score += 1
                    connected.send(f'Bravo, The Answer is correct! Your Score is {score}'.encode('utf-8'))
                else:
                    connected.send(f'Incorrect answer. Better luck next time!\n\n'.encode('utf-8'))

                remove_question(index)
                index, question, answer = getrandomquestionanswer(connected)
            
            else:
                remove(connected)
        except:
            continue

while True:
    connected, address = server.accept()
    clients.append(connected)

    new_thread = Thread(target=clientthread, args=(connected , address))

    new_thread.start()

    print(address[0] , " connected!")
