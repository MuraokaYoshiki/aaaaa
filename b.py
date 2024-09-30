import numpy as np
import math

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

def forward_propagation(A, x):
    activations = []
    for i in range(len(A)//2):
        y = sigmoid(np.dot(x, A[i*2]) + A[i*2+1][0])  # Fix: Swap x and A[i*2]
        activations.append(y)
    output = softmax(np.dot(activations[-1], A[-2].T) + A[-1][0])  # Fix: Transpose A[-2]
    return output, activations

def error(output, target):
    return -np.sum(target * np.log(output + 1e-10))  # Add a small epsilon to avoid log(0)

def backward_propagation(A, x, target):
    lenA = len(A)//2
    dEdaj = 0
    dEdrjm = 0
    dEdcm = 0
    dEdqmn = 0

    for n in range(len(x)):
        y, activations = forward_propagation(A, x[n])
        dEdakj = y - target[n]
        dEdaj += dEdakj
        dEdrjmk = np.outer(activations[-1], dEdakj)  # Fix: Swap arguments for np.outer
        dEdrjm += dEdrjmk
        dEdukm = np.dot(A[-2].T, dEdakj)  # Fix: Transpose A[-2]
        dEdvkm = dEdukm * activations[-1] * (1 - activations[-1])
        dEdcm += dEdvkm
        dEdqmn += np.outer(dEdvkm, x[n])  # Fix: Use x[n] instead of x

    return dEdaj, dEdrjm, dEdcm, dEdqmn / len(x)

def update_parameters(A, gradients, learning_rate):
    for n in range(len(A)//2):
        A[n*2] -= learning_rate * gradients[n]
        A[n*2+1] -= learning_rate * gradients[len(A)//2 + n]

# パラメータの初期化
A1 = np.array([[0, 0], [0, 0]])
b1 = np.array([[0, 0, 0]])
A2 = np.array([[0, 0], [0, 0], [0, 0]])
b2 = np.array([[0, 0, 0]])
A = [A1, b1, A2, b2]

# 入力データと正解データ
x = [np.array([0, 0]), np.array([0, 1]), np.array([1, 0]), np.array([1, 1])]
ans = [np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 1, 0]), np.array([0, 0, 1])]

lenA = len(A)//2

# 学習パラメータ
delta = 0.000001
alpha = 0.2
epsilon = 0.1

gradients = [np.zeros_like(param) for param in A]

for iter in range(2):
    e = error(forward_propagation(A, x)[0], ans)
    print(e)
    
    if e < epsilon:
        break
    
    gradients = backward_propagation(A, x, ans)
    
    update_parameters(A, gradients, alpha)

# テストデータでの予測
for x1 in range(2):
    for x2 in range(2):
        x_input = np.array([x1, x2])
        y_output, _ = forward_propagation(A, x_input)
        binary_output = ''.join(str(int(round(y))) for y in y_output)
        print(f"{x1} {x2} {binary_output}")
