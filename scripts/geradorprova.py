import random;

arq = open("caminho_completo_do_arquivo", 'r')
texto = arq.readlines()
questao = "";
alternativas = [];
questoes = dict([])
prova = []
i=0
letras = ['a','b','c','d','e']

lendo = ""
for linha in texto :
    if linha.__contains__("[QUESTAO]"):
        i+=1;
        lendo = "Q";
    elif linha.__contains__("[ALTERNATIVAS]"):
       lendo = "A";
    elif linha.__contains__("[FIM]"):
        questoes["Q"+str(i)] = questao;
        questoes['alt'] = alternativas;
        prova.append(questoes)
        lendo = "";
        questao = "";
        alternativas = [];
        questoes = dict([]);

    else:
        if lendo == "Q":
            questao += linha;
        elif lendo == "A":
            alternativas.append(linha);
print(prova)
arq.close()

#Gerar provas
numeroProvas = 5;
st =""

while (numeroProvas>0):
    numeroProvas -= 1;

    provaImpressa = random.sample(prova,2);

    numeroQ = 1;
    for q in provaImpressa:
        for key in q.keys():
            if key!="alt":
                st = st + "Q" +str(numeroQ) + str(": "+q[key]+"\n")
                numeroQ +=1;
            else:
                opcoes = random.shuffle(q["alt"]);
                l = 0;
                for op in q["alt"]:
                    st = st + letras[l]+") " + op
                    l+=1;
                st += "\n";
    st += "---------------------------------------------------------------\n"+chr(12)

test = "prova.rtf"
out_file = open(test,'w')
out_file.write(st)
out_file.close() 