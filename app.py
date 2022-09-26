import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict
st.title('Оптимизация системы сбора продукции скважин с использованием методов машинного обучения (Поиск оптимальной комбинации трубопроводов)')
st.markdown('Решение предоставлено командой BUSY из Astana IT University')
st.header('Вводимые данные(Gas Oil Rate, Pressure)')
col1, col2 = st.columns(2)
with col1:
	st.text('GOR')
	gor_1 = st.number_input('GOR_1', min_value=0.0, max_value=5000.0, value=1.0)
	gor_2 = st.number_input('GOR_2', min_value=0.0, max_value=5000.0, value=1.0)
	gor_3 = st.number_input('GOR_3', min_value=0.0, max_value=5000.0, value=1.0)
	gor_4 = st.number_input('GOR_4', min_value=0.0, max_value=5000.0, value=1.0)
	gor_5 = st.number_input('GOR_5', min_value=0.0, max_value=5000.0, value=1.0)
	gor_6 = st.number_input('GOR_6', min_value=0.0, max_value=5000.0, value=1.0)
	gor_7 = st.number_input('GOR_7', min_value=0.0, max_value=5000.0, value=1.0)
	gor_8 = st.number_input('GOR_8', min_value=0.0, max_value=5000.0, value=1.0)
	gor_9 = st.number_input('GOR_9', min_value=0.0, max_value=5000.0, value=1.0)
	gor_10 = st.number_input('GOR_10', min_value=0.0, max_value=5000.0, value=1.0)
	gor_11 = st.number_input('GOR_11', min_value=0.0, max_value=5000.0, value=1.0)
	gor_12 = st.number_input('GOR_12', min_value=0.0, max_value=5000.0, value=1.0)
	gor_13 = st.number_input('GOR_13', min_value=0.0, max_value=5000.0, value=1.0)
	gor_14 = st.number_input('GOR_14', min_value=0.0, max_value=5000.0, value=1.0)
	gor_15 = st.number_input('GOR_15', min_value=0.0, max_value=5000.0, value=1.0)
	gor_16 = st.number_input('GOR_16', min_value=0.0, max_value=5000.0, value=1.0)
	gor_17 = st.number_input('GOR_17', min_value=0.0, max_value=5000.0, value=1.0)
	gor_18 = st.number_input('GOR_18', min_value=0.0, max_value=5000.0, value=1.0)
with col2:
	st.text('Pressure')
	p_1 = st.number_input('p_1', min_value=0.0, max_value=5000.0, value=1.0)
	p_2 = st.number_input('p_2', min_value=0.0, max_value=5000.0, value=1.0)
	p_3 = st.number_input('p_3', min_value=0.0, max_value=5000.0, value=1.0)
	p_4 = st.number_input('p_4', min_value=0.0, max_value=5000.0, value=1.0)
	p_5 = st.number_input('p_5', min_value=0.0, max_value=5000.0, value=1.0)
	p_6 = st.number_input('p_6', min_value=0.0, max_value=5000.0, value=1.0)
	p_7 = st.number_input('p_7', min_value=0.0, max_value=5000.0, value=1.0)
	p_8 = st.number_input('p_8', min_value=0.0, max_value=5000.0, value=1.0)
	p_9 = st.number_input('p_9', min_value=0.0, max_value=5000.0, value=1.0)
	p_10 = st.number_input('p_10', min_value=0.0, max_value=5000.0, value=1.0)
	p_11 = st.number_input('p_11', min_value=0.0, max_value=5000.0, value=1.0)
	p_12 = st.number_input('p_12', min_value=0.0, max_value=5000.0, value=1.0)
	p_13 = st.number_input('p_13', min_value=0.0, max_value=5000.0, value=1.0)
	p_14 = st.number_input('p_14', min_value=0.0, max_value=5000.0, value=1.0)
	p_15 = st.number_input('p_15', min_value=0.0, max_value=5000.0, value=1.0)
	p_16 = st.number_input('p_16', min_value=0.0, max_value=5000.0, value=1.0)
	p_17 = st.number_input('p_17', min_value=0.0, max_value=5000.0, value=1.0)
	p_18 = st.number_input('p_18', min_value=0.0, max_value=5000.0, value=1.0)
if st.button('Predict'):
	result = predict(np.array([[gor_1,gor_2,gor_3,gor_4,gor_5,gor_6,gor_7,gor_8,gor_9,gor_10,gor_11,gor_12,gor_13,gor_14,gor_15,gor_16,gor_17,gor_18,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,p_9,p_10,p_11,p_12,p_13,p_14,p_15,p_16,p_17,p_18]]))
	st.text('An Optimal Pipeline Combination:')
	st.text(str(round(result[0][0])) + '/' + str(round(result[0][1])) + '/' + str(round(result[0][2])) + '/' + str(round(result[0][3])) + '/' + str(round(result[0][4])) + '/' + str(round(result[0][5])) + '/' + str(round(result[0][6])) + '/' + str(round(result[0][7])) + '/' + str(round(result[0][8]))+ '/' + str(round(result[0][9])) + '/' + 
		str(round(result[0][10])) + '/' + str(round(result[0][11])) + '/' + str(round(result[0][12])) + '/' + str(round(result[0][13])) + '/' + str(round(result[0][14])) + '/' + str(round(result[0][15])) + '/' + str(round(result[0][16])) + '/' + str(round(result[0][17])) + '/' + str(round(result[0][18])) + '/' + 
		str(round(result[0][19])) + '/' + str(round(result[0][20])) + '/' + str(round(result[0][21])) + '/' + str(round(result[0][22])) + '/' + str(round(result[0][23])) + '/' + str(round(result[0][24])) + '/' + str(round(result[0][25])) + '/' + str(round(result[0][26])) + '/' + str(round(result[0][27])) + '/' + 
		str(round(result[0][28])) + '/' + str(round(result[0][29])) + '/' + str(round(result[0][30])) + '/' + str(round(result[0][31])) + '/' + str(round(result[0][32])) + '/' + str(round(result[0][33])) + '/' + str(round(result[0][34])) + '/' + str(round(result[0][35])) + '/' + str(round(result[0][36])) + '/' + 
		str(round(result[0][37])) + '/' + str(round(result[0][38])) + '/' + str(round(result[0][39])) + '/' + str(round(result[0][40])) + '/' + str(round(result[0][41])) + '/' + str(round(result[0][42])) + '/' + str(round(result[0][43])) + '/' + str(round(result[0][44])) + '/' + str(round(result[0][45])) + '/' + 
		str(round(result[0][46])) + '/' + str(round(result[0][47])) + '/' + str(round(result[0][48])) + '/' + str(round(result[0][49])) + '/' + str(round(result[0][50])) + '/' + str(round(result[0][51])) + '/' + str(round(result[0][52])) + '/' + str(round(result[0][53])) + '/' + str(round(result[0][54])) + '/' + 
		str(round(result[0][55])) + '/' + str(round(result[0][56])) + '/' + str(round(result[0][57])) + '/' + str(round(result[0][58])) + '/' + str(round(result[0][59])) + '/' + str(round(result[0][60])) + '/' + str(round(result[0][61])) + '/' + str(round(result[0][62])) + '/' + str(round(result[0][63])) + '/' + 
		str(round(result[0][64])) + '/' + str(round(result[0][65])) + '/' + str(round(result[0][66])) + '/' + str(round(result[0][67])) + '/' + str(round(result[0][68])) + '/' + str(round(result[0][69])) + '/' + str(round(result[0][70])) + '/' + str(round(result[0][71])) + '/' + str(round(result[0][72])) + '/' + 
		str(round(result[0][73])) + '/' + str(round(result[0][74])) + '/' + str(round(result[0][75])) + '/' + str(round(result[0][76])) + '/' + str(round(result[0][77])) + '/' + str(round(result[0][78])) + '/' + str(round(result[0][79])) + '/' + str(round(result[0][80])))
