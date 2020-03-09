# Streamlit Application - Monte Carlo simulation - eastimating pi
# some code copied from here: https://github.com/dandrewmyers/numerical/blob/master/monte_carlo_pi/mc_pi_array.ipynb
# https://towardsdatascience.com/quickly-build-and-deploy-an-application-with-streamlit-988ca08c7e83

import streamlit as st
import numpy as np
import time
import matplotlib.pyplot as plt

st.title("Estimation of Pi Using Monte Carlo Simulation")
input_iterations = (st.sidebar.text_input("Number of iterations"))

if input_iterations!='':
    iter_num = int(input_iterations)
    start_time = time.time()
    x_array = np.random.rand(1,iter_num)
    y_array = np.random.rand(1,iter_num)
    radius_array = np.sqrt(x_array**2 + y_array**2)
    inside_circle = np.sum(radius_array < 1.0)
    pi_approx = (inside_circle*1.0 / iter_num) * 4.0

    st.write('Approximate value for pi:', pi_approx)
    st.write('Difference from numpy pi:', pi_approx-np.pi)
    st.write('Percent Error:', (pi_approx-np.pi)/np.pi*100)
    st.write('Execution Time:' ,time.time() - start_time, 'seconds')

    random_points_plot = plt.scatter(x_array, y_array, color='blue', s=.1)
    circle_plot = plt.Circle(( 0, 0 ), 1, color='red', linewidth=2, fill=False)
    ax = plt.gca()
    ax.cla()
    ax.add_artist(random_points_plot)
    ax.add_artist(circle_plot)
    st.pyplot()
