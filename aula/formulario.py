import tkinter as tk






def mostrar_console():
    nome = nome_input.get()
    print('Nome:', nome)
    idade = idade_input.get()
    print('Idade:', idade)
    email = email_input.get()
    print ('E-mail:', email)
    endereço = Endereço_input.get()
    print ('Endereço:', endereço)
    celula = Celular_input.get()
    print ('Celular:', celula)
    cep = Cep_input.get()
    print ('CEP:', cep)
    cidade = cidade_input.get()
    print ('Cidade: ', cidade)
    curso = curso_input.get()
    print ('Curso:', curso)





janela  = tk.Tk()
janela.geometry('1700x750')
janela.title('formulário')
janela.configure(bg = "#FFFFFF")
img = 'ng.ico'
janela.iconbitmap(img)


fr1 =  tk.Frame(janela, bg = "#FFFFFF")
fr1.grid(columnspan=3)

nome_texto = tk.Label(fr1, text = 'Nome: ', font=('Montserrat', 13), bg = "#FFFFFF")
nome_texto.grid(column=1, row=0)

nome_input = tk.Entry(fr1, font=('Montserrat', 17), bg = "#F5F5F5")
nome_input.grid(column=2, row=0)

idade_texto = tk.Label(fr1, text = 'Idade: ', font=('Montserrat', 13), bg = "#FFFFFF")
idade_texto.grid(column=1, row=2)

idade_input = tk.Entry(fr1, font=('Montserrat', 17), bg = "#F5F5F5")
idade_input.grid(column=2, row=2)

email_texto = tk.Label(fr1, text = 'E-mail: ', font=('Montserrat', 13), bg = "#FFFFFF")
email_texto.grid(column=1, row=3)

email_input = tk.Entry(fr1, font=('Montserrat', 17), bg = "#F5F5F5")
email_input.grid(column=2, row=3)

Endereço_texto = tk.Label(fr1, text = 'Endereço: ', font=('Montserrat', 13), bg = "#FFFFFF")
Endereço_texto.grid(column=1, row=4)

Endereço_input = tk.Entry(fr1, font=('Montserrat', 17), bg = "#F5F5F5")
Endereço_input.grid(column=2, row=4)

Celular_texto = tk.Label(fr1, text = 'Celular: ', font=('Montserrat', 13), bg = "#FFFFFF")
Celular_texto.grid(column=1, row=5)

Celular_input = tk.Entry(fr1, font=('Montserrat', 17), bg = "#F5F5F5")
Celular_input.grid(column=2, row=5)

Cep_texto = tk.Label(fr1, text = 'Cep: ', font=('Montserrat', 13), bg = "#FFFFFF")
Cep_texto.grid(column=1, row=6)

Cep_input = tk.Entry(fr1, font=('Montserrat', 17), bg = "#F5F5F5")
Cep_input.grid(column=2, row=6)

cidade_texto = tk.Label(fr1, text = 'Cidade: ', font=('Montserrat', 13), bg = "#FFFFFF")
cidade_texto.grid(column=1, row=7)

cidade_input = tk.Entry(fr1, font=('Montserrat', 17), bg = "#F5F5F5")
cidade_input.grid(column=2, row=7)

curso_texto = tk.Label(fr1, text = 'Curso: ', font=('Montserrat', 13), bg = "#FFFFFF")
curso_texto.grid(column=1, row=8)

curso_input = tk.Entry(fr1, font=('Montserrat', 17), bg = "#F5F5F5")
curso_input.grid(column=2, row=8)

fr2 = tk.Frame(janela, bg = "#FFFFFF")
fr2.grid(columnspan=3 )

btn_soma =  tk.Button(fr2, text='Enviar', font=('Montserrat', 12), bg = '#00ff00', width=12, command=mostrar_console)
btn_soma.grid(row=11, column=1, pady=20)

janela.mainloop()