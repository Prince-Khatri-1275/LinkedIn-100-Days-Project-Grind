import random

def get_accuracy(y_true, y_pred):
    if len(y_pred) != len(y_true):
        raise Exception("The dimensions are not compatible.")
        
    n = len(y_true)
    
    if n<=0:
        return float("inf")
    
    acc = 0
    for i in range(n):
        acc += 1 if (round(y_true[i], 8) == round(y_pred[i], 8)) else 0
    
    acc *= 1/n
    
    
    
    return acc


def calculate_gradients(y_true, y_pred, x):
    assert len(y_true) == len(y_pred) and len(y_true) == len(x)
    n = len(y_true)
    
    # if n<=0:
    #     return 0,  0
    
    dm = 0
    dc = 0
    
    for i in range(n):
        dm += (y_true[i] - y_pred[i]) * x[i]
        dc += (y_true[i] - y_pred[i])
    
    dm *= -2/n
    dc *= -2/n
    
    return dm, dc

def get_loss(y_true, y_pred):
    if len(y_pred) != len(y_true):
        raise Exception("The dimensions are not compatible.")

    n = len(y_true)
    
    if n<=0:
        return float("inf")
    
    loss = 0
    for i in range(n):
        loss += (y_true[i] - y_pred[i]) ** 2
    
    loss *= 1/n
    
    return loss

def predict(m, c, x):
    y = []
    for xi in x:
        y.append(m*xi + c)
    return y

def process(X, Y, epochs=10, batch_size=32, learning_rate=0.01, verbose=1):
    m = random.random()
    c = 0
    n = len(X)
    
    assert len(X) == len(Y)

    if batch_size == -1:
        batch_size = n

    for iteration in range(epochs):
        
        total_loss = 0
        total_acc = 0
        
        for i in range(0, n, batch_size):
            x_batch = X[i:i+batch_size]
            y_batch = Y[i:i+batch_size]

            y_pred = predict(m=m, c=c, x=x_batch)

            loss = get_loss(y_pred=y_pred, y_true=y_batch)
            acc = get_accuracy(y_true=y_batch, y_pred=y_pred)

            total_loss += loss
            total_acc += acc

            dm, dc = calculate_gradients(x=x_batch, y_true=y_batch, y_pred=y_pred)

            # Gradient Descent
            m -= dm * learning_rate
            c -= dc * learning_rate
            
        total_acc *= batch_size/n
        total_loss *= batch_size/n
        
        if verbose == 2 or verbose == 1 and iteration %50 == 0:
            print(f"Iteration :- {iteration} | Loss :- {total_loss} | Accuracy :- {total_acc}")
            
    print("Training Completed.\n Final slope (m) :- {m} | Final Intercept (c) :- {c}")
    
    return m, c

