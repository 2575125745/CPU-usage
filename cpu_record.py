#coding=utf-8
#!/usr/bin/python3

import psutil
import time
import log

record_interval = 60 # record is second
logger=log.logger()
def getCpu():
    logger.info("%s"%"Go to the get CPU function.")
    try:
        cpu = str(psutil.cpu_percent(interval=record_interval ))+"%"
    except Exception as e:
        logger.error("%s"%e)
        cpu=" "
    return cpu

def main():
    logger.info("Coming in main function.")
    now = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
    fname = now+"-report.csv"
    try:
        with open('%s' % fname,'w') as f:
            title_str = "Time, CPU "
            print(title_str)
            f.write("Time, CPU "+"\n")#title
            for i in range(4):
                info = getCpu()
                tmp_str = "%3s,%6s" % (i*record_interval,info)
                print(tmp_str)
                f.write(tmp_str+"\n")
    except IOError as e:
        logger.error(e)
        pass

if __name__=="__main__":
    logger.info("Starting Now")
    main()
    logger.info("End Program")