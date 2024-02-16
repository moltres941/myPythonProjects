import pyfiglet
from time import sleep
score = 0

print("welcome to my computer quiz!")
sleep(1)

print("\n")

playing = input("Do you want to play? ")
sleep(1)
print("\n")

if playing.lower() != 'yes':
	quit()

print("\n")
sleep(1)
print("Welcome mf")

print("\n")
sleep(1)
answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
	print('Correct')
	score +=1
else:
	print("fuck off!!")
sleep(1)
print("\n")

answer = int(input("How many dicks you have? "))

if answer >=5:
	print("Congratulations!! now you can fuck atleast 8 girls at a time ")
else:
	print("go touch yourself")
sleep(1)
print("\n")

answer = int(input("how many guys have you fucked until now? "))
if answer >=2:
	print("u r a bitch!!")
else:
	print("why are you living1?!!")
sleep(1)
print("\n")

answer = input("what is your skin tone? ")
if answer != "iam not a racist":
	print("go die u fking racist")
else:
	print("are you even human")
	score += 1
print("\n")

print(".")
sleep(1)
print("...")
sleep(1)

print(f"your score =\t{score}/2")
print(".....")
sleep(1)
print(".......")
sleep(1)
ASCII = pyfiglet.figlet_format("THE END")
print(ASCII)

