# Project Name: Network Analysis - Twitter Data and Random Network

## Project Description
This project focuses on analyzing a real-world network represented by the uploaded file named `Twitter_edges`. The goal is to form a network based on the provided data and compare it with a random network created using the Erdos-Rényi model. The analysis includes plotting the average local clustering coefficients (C(k)) in terms of the degree (k) for both the real-world data set and the random network. Additionally, the effects of changing the probability parameter (P) in the random network on the resulting clustering coefficient will be investigated.

## Dataset
The project utilizes the `Twitter_edges` file, which represents the edges of a real-world network. This dataset contains the necessary information to construct the network and perform the analysis.

## Tasks
The project involves the following tasks:

### Task A: Forming a Network from the Real-World Data
The first task is to form a network based on the edges provided in the `Twitter_edges` file. By constructing the network, we can analyze its properties and characteristics.

### Task B: Creating a Random Network using Erdos-Rényi Model
The next step is to create a random network using the Erdos-Rényi model with a network size (N) and a probability parameter (P) set to 0.1. This random network will serve as a comparison for the real-world data set.

### Task C: Plotting C(k) for Real-World and Random Networks
In this task, we will plot the average local clustering coefficients (C(k)) in terms of the degree (k) for both the real-world data set and the random network. The horizontal axis represents the degree (k), while the vertical axis represents the corresponding clustering coefficient (C(k)).

### Task D: Comparing Results and Providing Analysis
We will compare the results obtained from Task C and analyze the differences between the clustering coefficients of the real-world network and the random network. An explanation of the findings will be provided.

### Task E: Exploring the Effects of P on Clustering Coefficient
In this task, we will investigate the effects of changing the probability parameter (P) to 0.4 on the random network. We will compare the resulting clustering coefficients with the previous charts and examine if there is a relationship between the value of P and the resulting clustering coefficient.

## Getting Started
To run the project and perform the required analysis, follow these steps:

1. Ensure you have the necessary dependencies installed (Python, relevant libraries, etc.).
2. Download the `Twitter_edges` file and place it in the designated directory.
3. Execute the provided Python scripts for each task to obtain the desired results.

## Results
Upon running the project, the following information and visualizations will be generated:

1. Task A: The constructed network based on the real-world data.

![2 1](https://github.com/MiladAlipour98/Twitter_RandomNets/assets/105122009/60440ea0-670f-4336-adbc-24ecc8eb0fe8)

3. Task B: The random network created using the Erdos-Rényi model with a probability parameter (P) of 0.1.

![0 1](https://github.com/MiladAlipour98/Twitter_RandomNets/assets/105122009/16f46f99-c7a0-4072-920e-0dbb24d7701c)

![0 4](https://github.com/MiladAlipour98/Twitter_RandomNets/assets/105122009/a59a590e-6976-49a0-8ae2-13a1988fc211)


4. Task C: Plots of C(k) in terms of k for both the real-world network and the random network.

   
Real World Network  C(k):
![2 3](https://github.com/MiladAlipour98/Twitter_RandomNets/assets/105122009/502b9463-6cb5-4c2b-b757-287a1df2384a)

Erdos_Renyi Model G(N,P) , P = 0.1
![2 41](https://github.com/MiladAlipour98/Twitter_RandomNets/assets/105122009/9cfd4693-73e8-4689-8d59-ef50aff4af0d)

Erdos_Renyi Model G(N,P) , P = 0.4
![2 44](https://github.com/MiladAlipour98/Twitter_RandomNets/assets/105122009/d3ac4392-768f-4959-a82a-38c22e75ae39)


5. Task D: Analysis of the differences between the clustering coefficients of the real-world and random networks.
6. Task E: Investigation of the effects of changing the probability parameter (P) to 0.4 on the random network and comparison of resulting clustering coefficients.

## Conclusion
This project provides a comprehensive analysis of a real-world network represented by the `Twitter_edges` file and compares it with a random network created using the Erdos-Rényi model. By examining the average local clustering coefficients (C(k)) in terms of the degree (k), we gain insights into the clustering characteristics of both networks. Additionally,

 the effects of changing the probability parameter (P) on the random network's clustering coefficient are explored. The findings contribute to a better understanding of network properties and their relationship to clustering coefficients.
