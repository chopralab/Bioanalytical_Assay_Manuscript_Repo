#This script plots applies the GMM scoring 
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
import copy
import numpy as np
import itertools
import matplotlib.pyplot as plt
from sklearn import mixture
import umap
import random
import pandas as pd
seed = 7
np.random.seed(seed)
random.seed(7)

pk_a_1 = np.load("pk_a_1.npy")
ain = np.abs(np.reshape(np.array(pk_a_1),(-1,10)))


mmft = MinMaxScaler().fit_transform

tags = ["Generic-Tag","Tag-6","Tag-8","Tag-9","Tag-12","Tag-17"]
biotin = ["6-Biotin","8-Biotin","9-Biotin","12-Biotin","17-Biotin"]
ant = ['1 ug']
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


def thresh_l(val):
    if val == 0:
        plt.plot([0.8,6.2],[200,200],c='k')
        plt.plot([0.8,6.2],[750,750],c='k')
    if val in (1,2):
        plt.plot([0.8,6.2],[65000,65000],c='k')
        plt.plot([0.8,6.2],[100000,100000],c='k')
    if val in (3,4):
        plt.plot([0.8,6.2],[500,500],c='k')
        plt.plot([0.8,6.2],[1000,1000],c='k')
    if val in (5,6):
        plt.plot([0.8,6.2],[3,3],c='k')
        plt.plot([0.8,6.2],[5,5],c='k')
        plt.plot([0.8,6.2],[10,10],c='k')
    if val in (7,8,9):
        plt.plot([0.8,6.2],[30,30],c='k')
        plt.plot([0.8,6.2],[20,20],c='k')
        plt.plot([0.8,6.2],[10,10],c='k')




def thresh_h(val):
    if val == 0:
        plt.plot([200,200],[-0.1,.1],c='grey')
        plt.plot([750,750],[-0.1,.1],c='grey')
    if val in (1,2):
        plt.plot([65000,65000],[-0.1,.1],c='grey')
        plt.plot([100000,100000],[-0.1,.1],c='grey')
    if val in (3,4):
        plt.plot([500,500],[-0.1,.1],c='grey')
        plt.plot([1000,1000],[-0.1,.1],c='grey')
    if val in (5,6):
        plt.plot([3,3],[-0.1,.1],c='grey')
        plt.plot([5,5],[-0.1,.1],c='grey')
        plt.plot([10,10],[-0.1,.1],c='grey')
    if val in (7,8,9):
        plt.plot([30,30],[-0.1,.1],c='grey')
        plt.plot([20,20],[-0.1,.1],c='grey')
        plt.plot([10,10],[-0.1,.1],c='grey')

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


def sm_ggm(inp,metric="aic"):
    metric = metric
    bil = []
    title_l = ['Background','ULT Sen. + Ant.','ULT Sen. - Ant.','LLT Sen. + Ant.',
               'LLT Sen. - Ant.','S/N + Ant.','S/N - Ant.',"Ant. Int. [100x]",
               "Ant. Int. [10x]","Ant. Int. [1x]"]
    for i1 in np.arange(10):
        gmm_10.append([])
        gmm_10[-1].append(title_l[i1])
        avv = np.array([inp[:,i1],np.zeros(len(inp))]).transpose()
        #avv2 = np.array([so[0],np.zeros(len(inp))]).transpose()
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
        color_iter = itertools.cycle(['#1100FF', '#4AA7EA','#4AE2EA','#4AEACD','#8AEA4A' ,'#CFEA4A','#EAD24A','#EAA568', "#EA644A" ,"#E33535"])
        clf = best_gmm
        plt.figure(figsize=(6, 2))
        # Plot the winner
        splot = plt.subplot(1, 1, 1)
        Y_ = clf.predict(avv2)
        #pca = PCA(n_components=2)
        #pc = pca.fit_transform(ssft(avv))
        bil.append(get_best_s(avv,i1))
        plt.scatter(get_best_s(avv,i1)[0],0,c='k',s=30)
        thresh_h(i1)
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
            #colors_p.reverse()
            Y_v_list = [-v for v in Y_v_list]
        cl = np.arange(10)
        cl = list(cl)
        Y_score = []
        for sort_val in enumerate(np.argsort(Y_v_list)):
            print(cl[sort_val[1]])
            sc = colors_p[sort_val[0]]
            Y_score.append(cl[sort_val[1]])
            print(sc)
            cl[sort_val[1]] = str(sc)

        #mapping Y_ indexes to scores
        if i1 in (0,7,8,9):
            Y_score.reverse()

        for index_v in enumerate(Y_):
            gmm_10_scores[index_v[0]+1].append(Y_score.index(index_v[1]))

        for i, (mean, cov, color) in enumerate(zip(clf.means_, clf.covariances_,
                                                color_iter)):
            op = 1
            if not np.any(Y_ == i):
                continue
            
            plt.scatter(avv[Y_ == i, 0], avv[Y_ == i, 1], 10, color=cl[i])
        nc = np.mod(bic.argmin(), len(n_components_range)) + 2
        ct = cv_types[int(np.floor(bic.argmin() / len(n_components_range)))]
        splot.set_ylim([-.01, .01])
        #plt.xticks(())
        plt.xlabel(title_l[i1])
        plt.yticks(())
        #plt.title('Selected GMM: {0} model, {1} components'.format(ct,nc))
        plt.subplots_adjust(hspace=.35, bottom=.02)
        plt.tight_layout()
        #plt.savefig("pk_gmm_{0}_1ug.pdf".format(i1),dpi=300)
        plt.show()



gmm_10 = [["Analytical Metric","4 Components",
          "5 Components", "6 Components", "7 Components", "8 Components", "9 Components",
          "10 Components"]]


gmm_10_scores = [["PKA Conditions",'Background','ULT Sen. + Ant.','ULT Sen. - Ant.','LLT Sen. + Ant.',
                  'LLT Sen. - Ant.','S/N + Ant.','S/N - Ant.',"Ant. Int. [100x]",
                  "Ant. Int. [10x]","Ant. Int. [1x]","Total"]]

for i in range(len(ain)):
    gmm_10_scores.append([pl[i]])


sm_ggm(np.abs(np.reshape(np.array(pk_a_1),(-1,10))))

#gmm_10 = np.array(gmm_10)
c = 1
for i in gmm_10_scores[1:]:
    #gmm_10_scores[c].append(sum(gmm_10_scores[c][1:]))
    c += 1


#gmm_10 = pd.DataFrame(gmm_10)
#gmm_10.to_csv("gmm_10_AIC_1ug.csv",index=False,header=False)

#gmm_10_scores = pd.DataFrame(gmm_10_scores)
#gmm_10_scores.to_csv("gmm_10_scores_1ug.csv",index=False,header=False)





########### 2d plotting ############

def pk_bd_2d(inp,nu):
    inp = np.abs(inp)
    if nu in [0,7,8,9]:
        org = (min(inp[:]),np.argmin(inp[:]))
    else:
        org = (max(inp[:]),np.argmax(inp[:]))
    return(org)



def sm_ggm2(inp):
    bil = []
    title_l = ['Background','ULOQ Sen. + Ant.','ULOQ Sen. - Ant.','LLOQ Sen. + Ant.',
               'LLOQ Sen. - Ant.','S/N + Ant.','S/N - Ant.',"Ant. Int. [100x]",
               "Ant. Int. [10x]","Ant. Int. [1x]"]
    avv = np.array(np.abs(inp))
    avv[:,0] = -avv[:,0]
    avv[:,7] = -avv[:,7]
    avv[:,8] = -avv[:,8]
    avv[:,9] = -avv[:,9]
    avv = np.abs(avv)
    for i1 in np.arange(1):
        avv = np.array([avv[:,0],avv[:,5]]).transpose()
        scaler_m = preprocessing.MinMaxScaler()
        scaler_m.fit(avv)
        avv2 = scaler_m.transform(avv)
        #so = preprocessing.normalize(inp[:,i1].reshape(1,-1))
        #avv2 = np.array([so[0],np.zeros(len(inp))]).transpose()
        #avv2 = avv
        lowest_bic = np.infty
        bic = []
        n_components_range = range(2, 11)
        cv_types = ['full']
        for cv_type in cv_types:
            for n_components in n_components_range:
                # Fit a Gaussian mixture with EM
                gmm = mixture.GaussianMixture(n_components=n_components,
                                            covariance_type=cv_type)
                gmm.fit(avv2)
                #bic.append(gmm.score(avv2)**-1)
                bic.append(gmm.aic(avv2))
                #bic.append(gmm.aic(avv2)-(gmm.score(avv2)))
                if bic[-1] < lowest_bic:
                    lowest_bic = bic[-1]
                    best_gmm = gmm    
        bic = np.array(bic)
        print(best_gmm._n_parameters())
        color_iter = itertools.cycle(['#1100FF', '#4AA7EA','#4AE2EA','#4AEACD','#8AEA4A' ,'#CFEA4A','#EAD24A','#EAA568', "#EA644A" ,"#E33535"])
        clf = best_gmm
        bars = []
        # Plot the BIC scores
        plt.figure(figsize=(6, 4))
        # Plot the winner
        splot = plt.subplot(1, 1, 1)
        Y_ = clf.predict(avv2)
        #pca = PCA(n_components=2)
        #pc = pca.fit_transform(ssft(avv))
        print('hi')
        print(Y_)
        Y_v_list = []
        for i in range(max(Y_)+1):
            Y_v = [avv[v[0]] for v in enumerate(Y_) if v[1] == i]
            Y_v = np.array(Y_v)
            values = [np.mean(Y_v[:,0]),np.mean(Y_v[:,1])]
            euc_v = ( (values[0] - max(avv[:,0])) ** 2 + (values[1] - max(avv[:,1])) ** 2 ) ** .5
            Y_v_list.append(euc_v)#appends max value by increasing Y_ labels
        Y_v_list_2 = copy.deepcopy(Y_v_list)
        
        dist = []
        for values in avv2:
            dist.append(np.linalg.norm(values - [max(avv2[:,0]),max(avv2[:,1])]))
        print(Y_v_list)
        colors = ['#1100FF', '#4AA7EA','#4AE2EA','#4AEACD','#8AEA4A' ,'#CFEA4A','#EAD24A','#EAA568', "#EA644A" ,"#E33535"]
        colors.reverse()
        colors_p = copy.deepcopy(colors)
        #if i1 not in (0,7,8,9):
            #colors_p.reverse()
        #Y_v_list = [-v for v in Y_v_list]
        cl = np.arange(10)
        cl = list(cl)
        for sort_val in enumerate(np.argsort(Y_v_list)):
            print(cl[sort_val[1]])
            sc = colors_p[sort_val[0]]
            print(sc)
            cl[sort_val[1]] = str(sc)
        
        #scord = pk_bd_2d(inp,[0,1])
        plt.scatter(avv2[np.argmin(dist),0],avv2[np.argmin(dist),1],c='k',s=20)
        plt.scatter(1,1,c='k',s=20)
        #thresh_h(i1)
        #color_iter = itertools.cycle(["#003049","#d62828","#f77f00","#fcbf49","#49a078","#5bc0eb","#ee9cfc","#7ae7c7","#00a6a6","#832161"])
        for i, (mean, cov, color) in enumerate(zip(clf.means_, clf.covariances_,
                                                color_iter)):
            if not np.any(Y_ == i):
                continue
            plt.scatter(avv2[Y_ == i, 0], avv2[Y_ == i, 1], s=6, color=cl[i])
        #plt.scatter(scord[0],scord[1],facecolors='none', edgecolors='k',s=6)
        nc = np.mod(bic.argmin(), len(n_components_range)) + 2
        ct = cv_types[int(np.floor(bic.argmin() / len(n_components_range)))]
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.xlabel(title_l[0],fontsize=12)
        plt.ylabel(title_l[5],fontsize=12)
        #plt.yticks(())
        #plt.title('Selected GMM: {0} model, {1} components'.format(ct,nc))
        plt.subplots_adjust(hspace=.35, bottom=.02)
        plt.tight_layout()
        #plt.savefig("Plots/PK/pk_gmm_2d.pdf",dpi=300)
        #plt.savefig("Plots/PK/pk_gmm_2d",dpi=300)
        plt.show()
        break

def pk_bd(inp):
    scaler = preprocessing.MinMaxScaler()
    scaler.fit(np.abs(inp))
    inp = scaler.transform(inp)
    org = []
    org.append(max(inp[:,0]))
    org.append(max(inp[:,1]))
    org.append(max(inp[:,2]))
    org.append(max(inp[:,3]))
    org.append(max(inp[:,4]))
    org.append(max(inp[:,5]))
    org.append(max(inp[:,6]))
    org.append(max(inp[:,7]))
    org.append(max(inp[:,8]))
    org.append(max(inp[:,9]))
    dist =[]
    for i in inp:
        dist.append(np.linalg.norm(i - org))
    return(dist)

sm_ggm2(np.abs(np.reshape(np.array([pk_a_1]),(-1,10))))


########

def pk_bd(inp):#maybe delete
    scaler = preprocessing.MinMaxScaler()
    scaler.fit(np.abs(inp))
    inp = scaler.transform(inp)
    org = []
    org.append(max(inp[:,0]))
    org.append(max(inp[:,1]))
    org.append(max(inp[:,2]))
    org.append(max(inp[:,3]))
    org.append(max(inp[:,4]))
    org.append(max(inp[:,5]))
    org.append(max(inp[:,6]))
    org.append(max(inp[:,7]))
    org.append(max(inp[:,8]))
    org.append(max(inp[:,9]))
    dist =[]
    for i in inp:
        dist.append(np.linalg.norm(i - org))
    return(dist)



def sm_ggm_10(inp):
    bil = []
    for i1 in np.arange(1):
        gmm_all.append(["Scores"])
        avv = np.array(np.abs(inp))
        avv[:,0] = -avv[:,0]
        avv[:,7] = -avv[:,7]
        avv[:,8] = -avv[:,8]
        avv[:,9] = -avv[:,9]
        #so = preprocessing.normalize(inp[:,i1].reshape(1,-1))
        #avv2 = np.array([so[0],np.zeros(len(inp))]).transpose()
        fnd = pk_bd(avv)
        scaler_m = preprocessing.MinMaxScaler()
        scaler_m.fit(avv)
        avv2 = scaler_m.transform(avv)
        lowest_bic = np.infty
        bic = []
        n_components_range = range(4, 11)
        cv_types = ['full']
        for cv_type in cv_types:
            for n_components in n_components_range:
                # Fit a Gaussian mixture with EM
                gmm = mixture.GaussianMixture(n_components=n_components,
                                            covariance_type=cv_type)
                gmm.fit(avv2)
                #bic.append(gmm.score(avv2)**-1)
                bic.append(gmm.aic(avv2))
                #bic.append(gmm.aic(avv2)-(gmm.score(avv2)))
                gmm_all[-1].append(bic[-1]) 
                if bic[-1] < lowest_bic:
                    lowest_bic = bic[-1]
                    best_gmm = gmm  
                  
        bic = np.array(bic)
        color_iter = itertools.cycle(['navy', 'turquoise', 'cornflowerblue',
                                    'darkorange','maroon','gold','thistle',
                                    'peachpuff','lightsteelblue','pink'])
        clf = best_gmm
        bars = []

        plt.figure(figsize=(6, 6))
        splot = plt.subplot(1, 1, 1)
        Y_ = clf.predict(avv2)
        #pca = PCA(n_components=2)
        #pc = pca.fit_transform(ssft(avv))
        reducer = umap.UMAP(n_components=2,n_neighbors=50,min_dist=0.25,random_state=2)
        reducer.fit(mmft(avv2))
        pc = reducer.transform(mmft(avv2))#used to have standardizer here
        scord = np.argmin(pk_bd(avv))

        orient_p = np.arange(0,1.05,0.05)
        orient = []
        for dim in range(10):
            orient.append(orient_p)
        orient = np.array(orient)
        print(orient.T)
        orient = reducer.transform(orient.T)
        #plt.scatter(orient[0,0],orient[0,1],color='grey',s=20)
        plt.scatter(pc[scord,0],pc[scord,1],c='k',s=70)

        refrence = reducer.transform([[1,1,1,1,1,1,1,1,1,1]])
        plt.scatter(refrence[0,0],refrence[0,1],c='k',s=70)
        #thresh_h(i1)
        LLL = ['#1100FF', '#4AA7EA','#4AE2EA','#4AEACD','#8AEA4A' ,'#CFEA4A','#EAD24A','#EAA568', "#EA644A" ,"#E33535"]
        LLL.reverse()
        color_iter = itertools.cycle(LLL)
        Y_v_list = []
        for i in range(max(Y_)+1):
            Y_v = [fnd[v[0]] for v in enumerate(Y_) if v[1] == i]
            Y_v_list.append(np.mean(Y_v))#appends max value by increasing Y_ labels
            print("Y_v len",len(Y_v))
        Y_v_list_2 = copy.deepcopy(Y_v_list)
        print(Y_v_list)
        colors_p = copy.deepcopy(LLL)
        cl = np.arange(10)
        cl = list(cl)
        Y_score = []
        for sort_val in enumerate(np.argsort(Y_v_list)):
            print(cl[sort_val[1]])
            sc = colors_p[sort_val[0]]
            Y_score.append(cl[sort_val[1]])
            print(sc)
            cl[sort_val[1]] = str(sc)
        Y_score.reverse()
        #mapping Y_ indexes to scores
        
        for index_v in enumerate(Y_):
            gmm_all_scores[index_v[0]+1].append(Y_score.index(index_v[1]))
        #color_iter = itertools.cycle(["#003049","#d62828","#f77f00","#fcbf49","#49a078","#5bc0eb","#ee9cfc","#7ae7c7","#00a6a6","#832161"])
        for i, (mean, cov, color) in enumerate(zip(clf.means_, clf.covariances_,
                                                color_iter)):
            if not np.any(Y_ == i):
                continue
            plt.scatter(pc[Y_ == i, 0], pc[Y_ == i, 1], 40, c=cl[i])
        #plt.scatter(scord[0],scord[1],facecolors='none', edgecolors='k',s=6)
        nc = np.mod(bic.argmin(), len(n_components_range)) + 2
        ct = cv_types[int(np.floor(bic.argmin() / len(n_components_range)))]
        #plt.xticks(())
        plt.xlabel('Component_1',fontsize=12)
        plt.ylabel('Component_2',fontsize=12)
        plt.yticks(fontsize=10)
        plt.xticks(fontsize=10)
        #plt.title('UMAP of GMM Clustered PKA Assays')
        plt.subplots_adjust(hspace=.35, bottom=.02)
        plt.tight_layout()
        #plt.savefig("Plots/PK/pk_gmm_full_1ug.pdf",dpi=300)
        plt.show()
        return(Y_)
        break


gmm_all = [["# Components","4 Components",
          "5 Components", "6 Components", "7 Components", "8 Components", "9 Components",
          "10 Components"]]

gmm_all_scores = [["PKA Conditions",'Score']]

for i in range(len(ain)):
    gmm_all_scores.append([pl[i]])

c_LLL = sm_ggm_10(np.abs(np.reshape(np.array(pk_a_1),(-1,10))))

gmm_all = pd.DataFrame(gmm_all)
#gmm_all.to_csv("Data/PK/gmm_pk_full_aic_1ug.csv",index=False,header=False)

gmm_all_scores = pd.DataFrame(gmm_all_scores)
#gmm_all_scores.to_csv("Data/PK/gmm_pk_full_scores_1ug.csv",index=False,header=False)
