import streamlit as st

st.title("Proyecto Módulo 1 - Fundamentals")
st.sidebar.title("Parámetros")

st.image("Python_logo.png")
st.sidebar.image("DMC.png")

modulo = st.sidebar.selectbox("Elija un módulo", ["Módulo Listas","Módulo Array","Módulo funciones")

if modulo == "Módulo Listas":

valor_inicial = int(st.number_input("Ingrese el valor inicial", value=0))
valor_final = int(st.number_input("Ingrese el valor final", value=1))

lista_numerica = list(range(valor_inicial, valor_final))

st.write(lista_numerica)

elif modulo = "Módulo Array":
st.write("Estas en el módulo de arreglos"

else:
st.write("Estas en el módulo de funciones")


         
