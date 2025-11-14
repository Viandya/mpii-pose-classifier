import matplotlib.pyplot as plt


def plot_train_history(train_loss, val_loss, train_acc, val_acc):
    plt.figure(figsize=(10, 5))
    plt.plot(train_loss, label="Train loss")
    plt.plot(val_loss, label="Val loss")
    plt.legend()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.plot(train_acc, label="Train acc")
    plt.plot(val_acc, label="Val acc")
    plt.legend()
    plt.show()
