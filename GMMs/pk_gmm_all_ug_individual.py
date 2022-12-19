import sklearn
from sklearn import metrics
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
import copy
import numpy as np
import itertools
from scipy import linalg
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import mixture
from scipy import linalg
from mpl_toolkits.mplot3d import Axes3D
import umap
import random
import pandas as pd
seed = 25
np.random.seed(seed)
random.seed(15)

pk_a_1 = np.load("pk_a_1.npy")
pk_a_25 = np.load("pk_a_25.npy")
ain = np.abs(np.reshape(np.array(pk_a_25),(-1,10)))


mmft = MinMaxScaler().fit_transform

ssft = StandardScaler().fit_transform


tags = ["Generic-Tag","Tag-6","Tag-8","Tag-9","Tag-12","Tag-17"]
biotin = ["6-Biotin","8-Biotin","9-Biotin","12-Biotin","17-Biotin"]
ant = ['0.25 ug']
form = ['1','2','3','4','5','6']
pl = []
pl2 = []
for i in range(len(ain)):
    a = i//180 #1 for pk_a_1 and 0 for pk_a_25
    g = i + 1 - (180*a)
    f = g%30 # if the last it is 0
    F = g//30 - (0 ** f)
    b = g%6 # if the last it is 0
    B = (g - (F*30))//6  - (0**b)
    T = g%6
    pl.append(tags[T]+"/"+biotin[B]+ " antigen ["+ant[a]+"] format "+form[F])
    pl2.append([T,B,a,F])




#pk_a shape is 180 by 10 (anal. vals), first dimension is the six tags repeated
#for each of the five biotin-IDs which in turn
#is repeated for each six formats


def thresh_h(val,ax,i1,second):
    if val == 0:
        ax[second+(i1//2)*2,i1%2].plot([200,200],[-0.1,.1],c='grey')
        ax[second+(i1//2)*2,i1%2].plot([750,750],[-0.1,.1],c='grey')
    if val in (1,2):
        ax[second+(i1//2)*2,i1%2].plot([65000,65000],[-0.1,.1],c='grey')
        ax[second+(i1//2)*2,i1%2].plot([100000,100000],[-0.1,.1],c='grey')
    if val in (3,4):
        ax[second+(i1//2)*2,i1%2].plot([500,500],[-0.1,.1],c='grey')
        ax[second+(i1//2)*2,i1%2].plot([1000,1000],[-0.1,.1],c='grey')
    if val in (5,6):
        ax[second+(i1//2)*2,i1%2].plot([3,3],[-0.1,.1],c='grey')
        ax[second+(i1//2)*2,i1%2].plot([5,5],[-0.1,.1],c='grey')
        ax[second+(i1//2)*2,i1%2].plot([10,10],[-0.1,.1],c='grey')
    if val in (7,8,9):
        ax[second+(i1//2)*2,i1%2].plot([30,30],[-0.1,.1],c='grey')
        ax[second+(i1//2)*2,i1%2].plot([20,20],[-0.1,.1],c='grey')
        ax[second+(i1//2)*2,i1%2].plot([10,10],[-0.1,.1],c='grey')


def pk_bd_s(inp,nu):
    inp = np.abs(inp)
    if nu in [0,7,8,9]:
        org = (min(inp[:,0]),np.argmin(inp[:,0]))
    else:
        org = (max(inp[:,0]),np.argmax(inp[:,0]))
    return(org)


def get_best_s(inp,nu):
    ind = pk_bd_s(inp,nu)
    return(ind)


fig, ax = plt.subplots(10, 2, figsize=(6.5, 8))

def sm_gmm(inp,metric="aic"):
    metric = metric
    bil = []
    title_l = ['Background','ULT Sen. + Ant.','ULT Sen. - Ant.','LLT Sen. + Ant.',
               'LLT Sen. - Ant.','S/N + Ant.','S/N - Ant.',"Ant. Int. [100x]",
               "Ant. Int. [10x]","Ant. Int. [1x]"]
    for i1 in np.arange(10):
        gmm_10.append([])
        gmm_10[-1].append(title_l[i1])
        avv = np.array([inp[:,i1],np.zeros(len(inp))]).transpose()
        avv2 = avv
        lowest_bic = np.infty
        bic = []
        n_components_range = range(4, 11)
        cv_types = ['diag']
        for cv_type in cv_types:
            for n_components in n_components_range:
                # Fit a Gaussian mixture with EM
                gmm = mixture.GaussianMixture(n_components=n_components,
                                            covariance_type=cv_type)
                gmm.fit(avv2)
                if metric == 'bic':
                    bic.append(gmm.bic(avv2))
                elif metric == 'aic':
                    bic.append(gmm.aic(avv2))
                elif metric == 'score':
                    bic.append(-1*gmm.score(avv2))
                gmm_10[-1].append(bic[-1])
                if bic[-1] < lowest_bic:
                    lowest_bic = bic[-1]
                    best_gmm = gmm
                    
        bic = np.array(bic)
        color_iter = itertools.cycle(['#614AEA', '#4A62EA', '#4AA7EA',
                                    '#4AE2EA','#4AEACD','#4AEA6A','#8AEA4A',
                                    '#CFEA4A','#EAD24A','#EAA568'])
        clf = best_gmm
        bars = []

        Y_ = clf.predict(avv2)
        bil.append(get_best_s(avv,i1))
        ax[second+(i1//2)*2,i1%2].scatter(get_best_s(avv,i1)[0],0,c='k',s=10)
        thresh_h(i1,ax,i1,second)
        colors = ['#1100FF', '#4AA7EA','#4AE2EA','#4AEACD','#8AEA4A' ,'#CFEA4A','#EAD24A','#EAA568', "#EA644A" ,"#E33535"]
        colors.reverse()
        Y_v_list = []
        for i in range(max(Y_)+1):
            Y_v = [avv[v[0],0] for v in enumerate(Y_) if v[1] == i]
            Y_v_list.append(np.mean(Y_v))#appends max value by increasing Y_ labels
        Y_v_list_2 = copy.deepcopy(Y_v_list)
        print(Y_v_list)
        colors_p = copy.deepcopy(colors)
        if i1 not in (0,7,8,9):
            Y_v_list = [-v for v in Y_v_list]
        cl = np.arange(10)
        cl = list(cl)
        Y_score = []
        for sort_val in enumerate(np.argsort(Y_v_list)):
            print(cl[sort_val[1]])
            Y_score.append(cl[sort_val[1]])
            sc = colors_p[sort_val[0]]
            print(sc)
            cl[sort_val[1]] = str(sc)

        Y_score.reverse()

        for index_v in enumerate(Y_):
            gmm_10_scores[index_v[0]+1].append(Y_score.index(index_v[1]))

        for i, (mean, cov, color) in enumerate(zip(clf.means_, clf.covariances_,
                                                color_iter)):
            op = 1
            if not np.any(Y_ == i):
                continue
            
            ax[second+(i1//2)*2,i1%2].scatter(avv[Y_ == i, 0], avv[Y_ == i, 1], s=5, color=cl[i])
        nc = np.mod(bic.argmin(), len(n_components_range)) + 2
        ct = cv_types[int(np.floor(bic.argmin() / len(n_components_range)))]
        ax[second+(i1//2)*2,i1%2].set_ylim([-1, 1])
        ax[second+(i1//2)*2,i1%2].tick_params(axis='both', which='major', labelsize=8)
        if not second:
            ax[second+(i1//2)*2,i1%2].set_title(title_l[i1],fontsize=12)
            ax[second+(i1//2)*2,i1%2].set_ylabel('1.0\n µg/mL',fontsize=8)
        else:
            ax[second+(i1//2)*2,i1%2].set_ylabel('0.25\n µg/mL',fontsize=8)
        ax[second+(i1//2)*2,i1%2].set_yticks(())



gmm_10 = [["Analytical Metric","4 Components",
          "5 Components", "6 Components", "7 Components", "8 Components", "9 Components",
          "10 Components"]]
gmm_10_scores = [["PKA Conditions",'Background','ULOQ Sen. + Ant.','ULOQ Sen. - Ant.','LLOQ Sen. + Ant.',
                  'LLOQ Sen. - Ant.','S/N + Ant.','S/N - Ant.',"Ant. Int. [100x]",
                  "Ant. Int. [10x]","Ant. Int. [1x]","Total"]]
for i in range(len(ain)):
    gmm_10_scores.append([pl[i]])

second = False
sm_gmm(np.abs(np.reshape(np.array(pk_a_1),(-1,10))))
c = 1
for i in gmm_10_scores[1:]:
    gmm_10_scores[c].append(sum(gmm_10_scores[c][1:]))
    c += 1

gmm_10 = pd.DataFrame(gmm_10)
gmm_10.to_csv("Data/PK/gmm_pk_individual_aic_1ug.csv",index=False,header=False)
gmm_10_scores = pd.DataFrame(gmm_10_scores)
gmm_10_scores.to_csv("Data/PK/gmm_pk_individual_scores_1ug.csv",index=False,header=False)

##############


gmm_10 = [["Analytical Metric","4 Components",
          "5 Components", "6 Components", "7 Components", "8 Components", "9 Components",
          "10 Components"]]
gmm_10_scores = [["PKA Conditions",'Background','ULOQ Sen. + Ant.','ULOQ Sen. - Ant.','LLOQ Sen. + Ant.',
                  'LLOQ Sen. - Ant.','S/N + Ant.','S/N - Ant.',"Ant. Int. [100x]",
                  "Ant. Int. [10x]","Ant. Int. [1x]","Total"]]

for i in range(len(ain)):
    gmm_10_scores.append([pl[i]])

second = True
sm_gmm(np.abs(np.reshape(np.array(pk_a_25),(-1,10))))

c = 1
for i in gmm_10_scores[1:]:
    gmm_10_scores[c].append(sum(gmm_10_scores[c][1:]))
    c += 1

gmm_10 = pd.DataFrame(gmm_10)
gmm_10.to_csv("Data/PK/gmm_pk_individual_aic_p25ug.csv",index=False,header=False)
gmm_10_scores = pd.DataFrame(gmm_10_scores)
gmm_10_scores.to_csv("Data/PK/gmm_pk_individual_scores_p25ug.csv",index=False,header=False)

plt.subplots_adjust(hspace=.4, bottom=.6)
plt.tight_layout(h_pad=.1)
plt.savefig("Plots/PK/pk_gmm_allug_individual.pdf",dpi=300)
plt.show()