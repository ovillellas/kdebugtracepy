import time
import kdebugtracepy


def run_test():
    kdebugtracepy.kdebug_signpost(42, 0, 0, 0, 0)

    kdebugtracepy.kdebug_signpost_start(12, 0, 0, 0, 0)
    time.sleep(10)

    kdebugtracepy.kdebug_signpost_start(15, 0, 0, 0, 0)
    time.sleep(5)
    kdebugtracepy.kdebug_signpost_end(12, 0, 0, 0, 0)

    kdebugtracepy.kdebug_signpost_start(13, 0, 0, 0, 0)
    time.sleep(5)
    kdebugtracepy.kdebug_signpost_end(15, 0, 0, 0, 0)
    time.sleep(5)
    kdebugtracepy.kdebug_signpost_end(13, 0, 0, 0, 0)

    kdebugtracepy.kdebug_signpost(110, 0, 0, 0, 0)

if __name__=='__main__':
    run_test()
