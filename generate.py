'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import itertools

team_a_wk = ["ishan"]
team_b_wk = ["dhoni"]
team_a_bat = ["Rohith","Tilak","Sky","Green","David","Nehal"]
team_b_bat = ["Conway","Rutu","Rahane","Dube","Jadeja","Moen Ali"]
team_b_bowl = ["Tushar","aakash","Theeskshana","pathirana"]
team_a_bowl = ["meredith","arjun","behrendroff","Piyush"]

# Generate all combinations
all_combinations = []
for i in range(11, 12):
    for combination in itertools.combinations(team_a_wk + team_b_wk + team_a_bat + team_b_bat + team_b_bowl + team_a_bowl, i):
        if "ishan" not in combination and "dhoni" not in combination:
            continue
        if not any(player in team_a_bat + team_a_bowl for player in combination) or not any(player in team_b_bat + team_b_bowl for player in combination):
            continue
        all_combinations.append(combination)
        
print("Number of possible combinations:", len(all_combinations))
print(all_combinations[0])
d={}
d["Rohith"]=5
d["Tilak"]=7
d["Sky"]=7
d["Green"]=7
d["David"]=4
d["Nehal"]=2
d["Conway"]=7
d["Rutu"]=6
d["Rahane"]=6
d["Dube"]=7
d["Jadeja"]=7
d["Moen Ali"]=7
d["ishan"]=6
d["dhoni"]=3
d["Tushar"]=7
d["aakash"]=5
d["meredith"]=6
d["arjun"]=5
d["behrendroff"]=5
d["Theeskshana"]=5
d["Piyush"]=8
d["pathirana"]=7
# print(type(all_combinations[0]))
score_d={}
for i in all_combinations:
    val=0
    for j in i:
        val+=d[j]
    score_d[i]=val

# sortedDict = sorted(score_d)
newl=list(score_d.values())
# sorted(newl,reversed=True)
newl.sort()
newl=newl[::-1]
print(newl[:10])
print(i,score_d[i])
maxl=list(score_d.items())
rl=sorted(score_d.items(),key=lambda x:x[1],reverse=True)
# print(rl[:50])

    
    
# for i in sortedDict[:10]:
#     print(i,score_d[sortedDict[0]])
# sortedDict=sortedDict[::-1]
# print(sortedDict[0],score_d[sortedDict[0]])
# for i in all_combinations[:50]:
#     print(i)