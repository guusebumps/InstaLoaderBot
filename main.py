import datetime
import instaloader

L = instaloader.Instaloader()
L.login('*SEU LOGIN*', '*SUA SENHA*')

followers = instaloader.Profile.from_username(L.context, "*PERFIL QUE DESEJA PROCURAR*").get_followers()
followees = instaloader.Profile.from_username(L.context, "*PERFIL QUE DESEJA PROCURAR*").get_followees()

list_followee = []
for followee in followees:
    list_followee.append(followee.username)

list_follower = []
for follower in followers:
    list_follower.append(follower.username)

print("Quantidade de pessoas seguindo: " + str(len(list_followee)))
print("Quantidade de seguidores: " + str(len(list_follower)))

res = [x for x in list_followee + list_follower if x not in list_followee or x not in list_follower]

print("Quantidade de pessoas que não te seguem de volta: " + str(len(res)))

print("Lista de usuários que não te seguem de volta: ")
for i in res:
    print(i)