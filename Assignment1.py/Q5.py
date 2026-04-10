#WAP to enter p,t,r and calculate compound interest

#take input
p= 300000
r= 2
t=3

#perform operation 
compound_interest=p*(1+r/100)**t-p

#display output
print('Compound interest of 300000 is= ' ,compound_interest)