import os

soma=0
cont = 0

for i in range(25):
  
  #Foi utilizado end para manter na mesma linha a contagem de alunos
  cont = cont +1 
  print(cont,"ºAluno-> ", end="")
  nota = float(input("Qual a nota do aluno: "))
  
  os.system('clear')

  #calculo
  soma = soma + nota
  media = soma /cont
  
else:
  if(media > 8):
    print("Esta turma é excelente!!!")
  elif(media >=5 and media <=8):
    print("Esta turma é boa.")
  elif(media<=4):
    print("Esta turma já era...")  
  
  
