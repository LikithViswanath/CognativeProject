import pandas, sys
import pandas as pd

a = pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/lieModified/kushagra_lie_R.csv")
b = pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/truthModified/kushagra_truth_R.csv")
c=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/lieModified/komal_lie_R.csv")
d=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/truthModified/komal_truth_R.csv")
e=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/lieModified/nirma_lie_R.csv")
f=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/truthModified/nirma_truth_R.csv")
g=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/lieModified/nisha_lie_R.csv")
h=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/truthModified/nisha_truth_R.csv")
i=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/lieModified/himani_lie_R.csv")
j=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/truthModified/himani_truth_R.csv")
k=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/lieModified/jayti_lie_R.csv")
l=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/truthModified/jayti_truth_R.csv")
m=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/lieModified/disha_lie_R.csv")
n=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/truthModified/disha_truth_R.csv")
o=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/lieModified/kaajal_lie_R.csv")
#p=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/truthModified/kaajal_truth_R.csv")
#q=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/lieModified/malvika_lie_R.csv")
#r=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/truthModified/malvika_truth_R.csv")
#s=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/lieModified/rakhi_lie_R.csv")
#t=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/truthModified/rakhi_truth_R.csv")
# u=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/shubhi_lie_R.csv")
# v=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/shubhi_truth_R.csv")
# w=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/arpit_lie_R.csv")
# x=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/arpit_truth_R.csv")
# y=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/nobha_lie_R.csv")
# z=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/nobha_truth_R.csv")
# ab=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/priya_lie_R.csv")
# cd=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/priya_truth_R.csv")
# ef=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/risana_lie_R.csv")
# gh=pd.read_csv("C:/Users/likith viswanath/PycharmProjects/lie_detector/risana_truth_R.csv")
merged = pd.concat([a,b,c,d,e,f,g,h,i,j,
                    k,l,m,n,o
                    #,p,q,r,s,t,
                    # u,v,w,x,y,z,ab,cd,ef,gh
                    ])

mergedLie = pd.concat([a,c,e,g,i,k,m,o])

mergedTruth = pd.concat([b,d,f,h,j,l,n])

merged.to_csv('C:/Users/likith viswanath/PycharmProjects/lie_detector/result_new_now.csv', index=False)

mergedTruth.to_csv('C:/Users/likith viswanath/PycharmProjects/lie_detector/merged_truth.csv', index=False)

mergedLie.to_csv('C:/Users/likith viswanath/PycharmProjects/lie_detector/merged_lie.csv', index=False)
