import numpy as np
from scipy import stats

#returns merged table with npi greater or eq 5
def contingencyTable (lines_cont_table):
    merged_for_use = [[x for x in lines_cont_table[0].values()], [x for x in lines_cont_table[1].values()]]
    m_x = min(merged_for_use[0])
    print(merged_for_use)
    while m_x < 5:
        idx = merged_for_use[0].index(m_x)
        merged_for_use[0].pop(idx)
        merged_for_use[0][0] += m_x
        if idx < len(merged_for_use[1]):
            ret = merged_for_use[1].pop(idx)
            merged_for_use[1][0] += ret
        m_x = min(merged_for_use[0])
    m_y = min(merged_for_use[1])
    while m_y < 5:
        idx = merged_for_use[1].index(m_y)
        merged_for_use[1].pop(idx)
        merged_for_use[1][0] += m_y
        if idx < len(merged_for_use[0]):
            ret = merged_for_use[0].pop(idx)
            merged_for_use[0][0] += ret
        m_y = min(merged_for_use[1])
    return merged_for_use


def testContigencyTable(merged_cont_table , alpha):
    N = np.matrix([merged_cont_table[0], merged_cont_table[1]])
    n = np.sum(N)
    pbj = np.sum(N, axis = 0)/n
    pib = np.sum(N, axis = 1)/n
    npp = np.matmul(pib, pbj)*n
    chi = np.sum(np.square(N - npp)/(npp))
    statis = stats.chi2.isf(alpha, len(merged_for_use[0]) - 1)
    decline = chi >= stats.chi2.isf(alpha, len(merged_for_use[0]) - 1)
    return pbj,pib,npp,chi,statis,decline