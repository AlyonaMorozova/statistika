__author__ = 'student'
def get_percentile_number(value, percentiles)
    m=True
    A=0
    for n in range(len( percentiles)-1,0,-1):
        if (value >= percentiles[n]) and m=True:
            A=1
            m=False
    return A

file_input = open('/home/student/PycharmProjects/')

plt.subplot(121)