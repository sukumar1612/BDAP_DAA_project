# This is a sample Python script.

import random

import plotly
from plotly.graph_objs import Scatter, Layout

import EdmondsKarp as ek


def get_problem_details():
    no_of_drivers = int(input("Enter no. of drivers: "))
    no_of_buses = int(input("Enter no. of buses: "))

    if no_of_buses > no_of_drivers:
        print("ERROR: No. of Buses >= No.of drivers!")

    data = {}
    for i in range(1, no_of_drivers + 1):
        driver = i
        temp = int(input("Enter driver " + str(driver) + "'s prefered buses: "))
        data[driver] = temp + no_of_drivers
    data["no_of_drivers"] = no_of_drivers
    data["no_of_buses"] = no_of_buses
    print(data)
    return data


def generate_random_assignment(no_of_drivers, no_of_buses):
    # no_of_buses = int(random.random()*100) % no_of_drivers

    data = {}

    for i in range(1, no_of_drivers + 1):
        data[i] = no_of_drivers + int(random.random() * 100) % no_of_buses

    data["no_of_drivers"] = no_of_drivers
    data["no_of_buses"] = no_of_buses
    return data


def generate_matrix(data):
    no_of_drivers = data["no_of_drivers"]
    no_of_buses = data["no_of_buses"]
    total = no_of_drivers + no_of_buses + 2
    data[0] = 0
    data[total - 1] = 0
    input_matrix = [[0 for j in range(0, total)] for i in range(0, total)]
    for i in range(0, total):
        for j in range(0, total):
            if i == 0:
                if j != 0 and j <= no_of_drivers:
                    input_matrix[i][j] = 1
            elif j == 0:
                if i != 0 and i <= no_of_drivers:
                    input_matrix[i][j] = 1
            elif i == total - 1:
                if j != total - 1 and j > no_of_drivers:
                    input_matrix[i][j] = 1
            elif j == total - 1:
                if i != total - 1 and i > no_of_drivers:
                    input_matrix[i][j] = 1
            elif i <= no_of_drivers:
                if data[i] == j:
                    input_matrix[i][j] = 1
    return input_matrix


def generate_random_plot():
    print("-------------")
    x = [i for i in range(50, 200, 4)]
    y = []
    print("loading graph :        ", end=" ")
    for i in range(50, 200, 4):
        data = generate_random_assignment(i, 50)
        mat = generate_matrix(data)
        edmond = ek.EdmondsKarp(mat)
        output = edmond.edmonds_karp(0, data["no_of_buses"] + data["no_of_drivers"] + 1)
        y.append(output[2])
        print(end="\b\b\b\b"+str(int(100*(i-50)/150))+" %")
    print(end="\b\b\b\b" + str(100) + "%")
    print("\nfinished")
    plotly.offline.plot({
        "data": [Scatter(x=x, y=y)],
        "layout": Layout(title="Edmond karp")
    })


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = generate_random_assignment(59, 22)
    print(data)
    # data = get_problem_details()
    mat = generate_matrix(data)
    edmond = ek.EdmondsKarp(mat)
    output = edmond.edmonds_karp(0, data["no_of_buses"] + data["no_of_drivers"] + 1)
    print("total number of bus drivers assigned to buses are :", output[0])
    # print(output[1])
    for i in range(1, len(output[1])):
        print("Driver ", output[1][i][2], " is assigned to bus ", output[1][i][1] - data["no_of_drivers"])
    print("number of iterations : ", output[2])

    generate_random_plot()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
