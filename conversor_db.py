import streamlit as st
import math

st.set_page_config(layout="centered", page_icon="https://cdn-icons-png.flaticon.com/512/3308/3308060.png",
                   page_title= "Conversor dB Watt")
st.title("Conversor dB Watt")

#variables
col1, col2 = st.columns([1,1])
calculus = -1
global index1
index1 = [0, 0, -9, -6, -3, 0, 3, 6, 9]

#calculus formulas
def conv_dBtodBm(value):
    result = value + 30
    return result

def conv_dBmtodB(value):
    result = value - 30
    return result

def conv_dBtoWatt(value):
    result = math.pow(10, value/10)  #10^((value)/10)) #formula example
    return result

def conv_Watt_todB(index, value):
    result = 10 * math.log10(value*10 ** index1[index])
    return result


with col1:
    array1 = ["dB", "dBm", "nW", "uW", "mW", "W", "kW", "MW", "GW"]
    choice1 = st.selectbox("Escolha uma unidade", array1, key= 'db1')
    numberField = st.number_input(
        "Digite um valor", -100.0, 200.0, key = 'nF1',
        value=10.0
    )
    clicked = st.button("Converter")

with col2:
    array2 = ["dBm", "dB", "W"]
    choice2 = st.selectbox("Escolha uma unidade", array2, key = 'db2')
    st.write("")
    if choice1 == choice2:
        calculus = numberField

    elif choice1 == 'dB' and choice2 == 'dBm':
        calculus = conv_dBtodBm(numberField)

    elif choice1 == 'dBm' and choice2 == 'dB':
        calculus = conv_dBmtodB(numberField)

    elif choice2 == 'dB': #watts to db
        if(array1.index(choice1) >= 2):
            calculus = conv_Watt_todB(array1.index(choice1), numberField)


    elif choice2 == 'dBm': #watts to dbm
        if(array1.index(choice1) >= 2):
            calculus = conv_Watt_todB(array1.index(choice1), numberField) + 30

    elif choice2 == 'W': #db  or dbm to watts
        if(choice1 == 'dB'):
            calculus = conv_dBtoWatt(numberField)

    elif(choice1 == 'dBm'):
        calculus = conv_dBtoWatt(numberField-30)

    if clicked and calculus != -1:
        result = st.success(f"{calculus: .3f} {choice2}")