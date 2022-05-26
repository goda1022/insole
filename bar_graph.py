import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt


def main():
    rg = default_rng(seed=0)
    students_count = 2
    examinations_count = 3
    sensor_count = 5
    #xmm=[-0.2031255888577916, -1.5127773386594867, 0.3820059257847792, -0.6753763663539327, -5.130061755516968]
    #xms=[0.3773264780985801, 0.8248321713234268, 0.3771786417936941, 0.3437425447490893, 2.544349090347357]
    #xkm=[-0.8069154979613536, -0.2712856963405894, 0.07004852066670374, 0.5784426846022379, -1.5598686147687093]
    #xks=[1.3283541440977755, 0.8815200291476809, 0.7472525676734582, 0.8137970321923985, 3.800048890244863]
    xmm=[-0.37980726445251695, -4.384251348062746, -2.798047898551083, 0.3029444201542497, -4.189788787824702]
    xms=[0.14129656447294575, 2.1372375562109975, 0.8537722153787759, 0.2717218962539136, 1.6358461876877675]
    xkm=[1.8545741240846016, 1.8683848612388627, 1.1945690175947807, -0.023257425059866794, -4.090348305401114]
    xks=[0.8499095061346549, 1.0095832930828905, 0.7804616104999824, 0.7547789968230201, 1.5894628992462123]
    #xmm=[2.320500208869214, 17.81611860952871, 9.19884625038333, 3.3852808359457205, 26.419585536685027]
    #xms=[1.258729052530216, 7.27828392585264, 4.325999186922437, 1.2184428408990726, 7.089186241656426]
    #xkm=[4.6110571886651375, 22.694385214535444, 6.5880905685631, 7.411760165287045, 20.708128343261407]
    #xks=[1.9873105765877164, 8.470641682009001, 2.4120374461963943, 1.4965399461606192, 7.81511504967341]
    x = np.arange(sensor_count)

    fig = plt.figure()
    ax = fig.add_subplot()
    width = 0.8
    w = width / students_count
    ax.bar(x + 0 * w + w / 2 - width / 2, xmm, yerr=xms, ecolor='black', capsize=3, width=w, label='expert')
    ax.bar(x + 1 * w + w / 2 - width / 2, xkm, yerr=xks, ecolor='black', capsize=3, width=w, label='beginner')
    ax.set_xticks(x)
    ax.set_xticklabels(['#1', '#2', '#3', '#4', '#5'])
    ax.set_xlabel('Sensor_number')
    ax.set_ylabel(' impulse of per step [N·s]')
    ax.legend(loc='best')
    #ax.set_title('Fig.1: Average and standard deviation of scores for each subject.')
    ax.grid(color='black', linestyle='dotted', axis='y')
    ax.set_axisbelow(True)
    fig.savefig("Fy_Average and standard deviation.svg")
    plt.show()


if __name__ == '__main__':
    main()