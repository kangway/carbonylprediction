

import matplotlib.pyplot as plt
import numpy as np
import itertools

def plotDecisionBoundary(model, X, y, ax=None, cmap='rainbow'):
    '''
    Visualizer from Jake VanderPlas
    https://github.com/jakevdp/PythonDataScienceHandbook
    '''
    ax = ax or plt.gca()
    
    ax.scatter(X[:, 0],
               X[:, 1],
               c=y,
               s=30,
               cmap=cmap,
               clim=(y.min(), y.max()),
               zorder=3,
               edgecolor='black',
               alpha=0.7)
        
    plt.axis('tight')
    xlim = plt.gca().get_xlim()
    ylim = plt.gca().get_ylim()
               
    xx, yy = np.meshgrid(np.linspace(*xlim, num=100),
                         np.linspace(*ylim, num=100))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
               
    # Create a color plot with the results
    n_classes = len(np.unique(y))
    contours = ax.contourf(xx, yy, Z, alpha=0.3,
                           levels=np.arange(n_classes + 1) - 0.5,
                           cmap=cmap, clim=(y.min(), y.max()),
                           zorder=1)


def plot_confusion_matrix(mat, classes, pltTitle, cmap=plt.cm.Blues):
    plt.imshow(mat, interpolation='nearest', cmap=cmap)
    plt.title(pltTitle)
    plt.colorbar(fraction=0.046, pad=0.04)
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    
    thresh = mat.max() / 2.
    for i, j in itertools.product(range(mat.shape[0]), range(mat.shape[1])):
        plt.text(j, i, mat[i, j],
                 horizontalalignment="center",
                 color="white" if mat[i, j] > thresh else "black")
    
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted')



