with open('D:\\THUY\\alibaba\\Factory-directly-biodegradable-disposable-grass-reed-straw.jpg', 'rb') as rf:
    with open('D:\\THUY\\alibaba\\Factory-directly-biodegradable-disposable-grass-reed-straw_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)
        # # Or this is more controlable:
        # size = 4086
        # rf_size = rf.read(size)
        # while len(rf_size) > 0:
        #     wf.write(rf_size)
        #     rf_size = rf.read(size)