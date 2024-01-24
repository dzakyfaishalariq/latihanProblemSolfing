def past(h, m, s):
    # ubah ke mili detik
    h_mil = h * 3600 * 1000
    m_mil = m * 60 * 1000
    s_mil = s * 1000
    return sum([h_mil,m_mil,s_mil])

print(past(0,1,1))