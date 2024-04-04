# olá, como está? espero que bem, pois eu não estou
#já que estamos aqui vou dar uma explica nas maluquices que tive que aprender/criar
import requests
import random


url = "https://rickandmortyapi.com/api"

response = requests.get(url)

dados = response.json() 
#da linha 4 a 11 recebi a api de rick and morty(foi a unica que achei)
{
  "characters": "https://rickandmortyapi.com/api/character",
  "locations": "https://rickandmortyapi.com/api/location",
  "episodes": "https://rickandmortyapi.com/api/episode"
}
#por algum motivo o maluco que criou essa api fez ela por paginas oq fez eu ter que ir alternando entre elas
Rpersonagens = requests.get("https://rickandmortyapi.com/api/character/?page=0")
link = Rpersonagens.json()
aux = link["info"]
npages = aux["pages"]
totalP = aux["count"]
rid = random.randint(1,totalP)

#declarando as variaveis 
nome = ""
status = ""
especie = ""
tipo = ""
genero = ""
auxorigem = ""
origem = ""
linkep = ""
eps = ""
chute = ""
sair = False

dstatus = ""
despecie = ""
dtipo = ""
dgenero = ""
dorigem = ""
depisodeo = ""

def main(sair):
	restp = []

	global nome

	print("              BEM VINDO!              ")
	print("esse é o quem eu sou de rick and morty")
	print("")
	print("antes de começar uma explicação\nquando o jogo comecar um nome aleatorio vai ser sorteado\nvc vai tentar descobrir com base nas dicas que voce escolher\nquando todas as dicas forem dadas e voce nao acertar o jogo acaba")
	print("vamos comecar (digite enter)")
	chute = input()
	print("carregando..")
	iniciarjogo(restp)
	cont = 0
	while sair != True:
		chute = ""
		dica(restp)
		mostrarpersonagens(restp)
		mostrardica()
		print("escolha um personagem: ")
		chute = input()
		sair = verifica_chute(chute, nome)
		cont = cont + 1
		if cont == 5 and sair == False:
			break
	if sair == False:
		mostrarpersonagens(restp)
		print("ultima chance!\n a primeira aparissao desse personagen foi:")
		print("epsodio: ", eps["name"], " ", eps["episode"])
		mostrardica()
		print("digite o nome do personagem: ")
		chute = input()
		sair = verifica_chute(chute, nome)
	if sair == False:
		print("uma pena, mais sorte da proxima vez, obrigado por jogar")
		print("o personagem era: ", nome)
	print("obrigado por jogar")



		

def iniciarjogo(rest):
	newlink = "https://rickandmortyapi.com/api/character/?page=0"
	# não sei se tem uma forma mais facil mas foi a unica que achei para pegar o npages disso ai(poderia ter só colocado 42 já que é o npages atual mas sofri por 3horas para achar uma forma)
	for x in range(npages):
		
		Rpersonagens = requests.get(newlink)
		personagens = Rpersonagens.json()
		
		#Rlocais = requests.get("https://rickandmortyapi.com/api/location")
		#locais = Rlocais.json()
		
		'''for resultados in personagens["results"]:
			print(resultados["name"])'''
		
		global eps
		global nome
		global status
		global especie
		global tipo
		global genero
		global origem
		for results in personagens["results"]:
			rest.append(results["name"])
			if rid == results["id"]:
				nome = results["name"]
				status = results["status"]
				especie = results["species"]
				tipo = results["type"]
				genero = results["gender"]
				auxorigem = results["origin"]
				origem = auxorigem["name"]
				auxlinkep = results["episode"]
				linkep = auxlinkep[0]
				Reps = requests.get(linkep)
				eps = Reps.json()
		
		'''
		if eps != "":
			print("epsodio: ", eps["name"], " ", eps["episode"])
		'''	

		passagem = personagens["info"]
		newlink = passagem["next"]

def verifica_chute(chute, nome):
	newlink = "https://rickandmortyapi.com/api/character/?page=0"
	# não sei se tem uma forma mais facil mas foi a unica que achei para pegar o npages disso ai(poderia ter só colocado 42 já que é o npages atual mas sofri por 3horas para achar uma forma)
	for x in range(npages):
		
		Rpersonagens = requests.get(newlink)
		personagens = Rpersonagens.json()
		global sair
		if chute == nome:
			print("parabens voce acertou")
			return True

		passagem = personagens["info"]
		newlink = passagem["next"]
	print("personagem errado")
	return False

def dica(pdel):
	sairdica = False
	while sairdica != True: 
		global dstatus
		global despecie
		global dtipo
		global dgenero
		global dorigem
		global status
		global especie
		global origem
		global genero
		global eps

		print("1 status: ", dstatus)
		print("2 especie: ", despecie)
		print("3 tipo: ", dtipo)
		print("4 Genero: ", dgenero)
		print("5 Origem: ", dorigem)
		print("qual dica você deseja escolher: ")
		escolha = input()

		match escolha:
			case "1":
				dstatus = status
				sairdica = True
				deletar(1, status, pdel)
			case "2":
				if despecie == "":
					despecie = especie
					sairdica = True
					deletar(2, especie, pdel)
			
			case "3":
				if dtipo == "":
					dtipo = tipo
					sairdica = True
					deletar(3, tipo, pdel)
			
			case "4":
				if dgenero == "":
					dgenero = genero
					sairdica = True
					deletar(4, genero, pdel)
			
			case "5":
				if dorigem == "":
					dorigem = origem
					sairdica = True
					deletar(5, origem, pdel)
			
	print("1 status: ", dstatus)
	print("2 especie: ", despecie)
	print("3 tipo: ", dtipo)
	print("4 Genero: ", dgenero)
	print("5 Origem: ", dorigem)

def deletar(n, q, r1):
	global npages
	global dorigem
	global dtipo
	match n:
		case 1:
			valor = "status"
		case 2:
			valor = "species"
		case 3:
			valor = "type"
		case 4:
			valor = "gender"
		case 5:
			valor = "origin"
			
	newlink = "https://rickandmortyapi.com/api/character/?page=0"
	# não sei se tem uma forma mais facil mas foi a unica que achei para pegar o npages disso ai(poderia ter só colocado 42 já que é o npages atual mas sofri por 3horas para achar uma forma)
	for x in range(npages):
		int(x)
		Rpersonagens = requests.get(newlink)
		personagens = Rpersonagens.json()
		for results in personagens["results"]:
			j = results[valor]
			if valor == "origin":
				y = results[valor]
				j = y["name"]
			if q != j:
				for aux in r1:
					if aux == results["name"]:
						r1.remove(aux)

		passagem = personagens["info"]
		newlink = passagem["next"]
	if valor == "type":
		if dtipo == "":
			dtipo = "sem tipagem" 


def mostrarpersonagens(p1):
	for i in p1:
		print(i)
	print("")

def mostrardica():

	global dstatus
	global despecie
	global dtipo
	global dgenero
	global dorigem

	print("1 status: ", dstatus)
	print("2 especie: ", despecie)
	print("3 tipo: ", dtipo)
	print("4 Genero: ", dgenero)
	print("5 Origem: ", dorigem)
main(sair)