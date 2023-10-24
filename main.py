import random
import math
import numpy as np
from customer import Customer
from simulations import *
from MMCKQueue import *
from threading import Thread

if __name__ == '__main__':
    totalServedCustomers = 0
    entranceCustomerEvent = CustomerEvent(0.05)
    foodCustomerEvent = CustomerEvent(0.05)
    drinkCustomerEvent = CustomerEvent(0.05)

    simulationTime = 1000
    
    entranceCustomerEvent.timeGenerate(simulationTime = simulationTime, arrivalTime = 0)
    
    drinkMMCK = MMCKQueue("drink_queue",0.04, 10, 15, drinkCustomerEvent, waitCustomerFromOtherQueue = True)
    foodMMCK = MMCKQueue("food_queue",0.03, 10, 15, foodCustomerEvent, waitCustomerFromOtherQueue = True)
    entranceMMCK= MMCKQueue("entrance_queue",0.05, 5, 15, entranceCustomerEvent, nextQueueList = [ foodMMCK, drinkMMCK], queueRatio = [1, 1])
    
    
    print(len(entranceMMCK.customerEventSim.eventList),' customer go to entrance', entranceMMCK.customerEventSim.eventList)
    
    
    threads     = [None, None, None]
    threads[0]  = Thread(target=entranceMMCK.run, args=(simulationTime, ))
    threads[1]  = Thread(target=drinkMMCK.run, args=(simulationTime, ))
    threads[2]  = Thread(target=foodMMCK.run, args=(simulationTime, ))
    
    for thread in threads:
        thread.start()
        
        
    # while True:    
    #    if entranceMMCK.queueStatus == QueueStatus.IDLE and drinkMMCK.queueStatus == QueueStatus.IDLE and foodMMCK.queueStatus == QueueStatus.IDLE:
    #         entranceMMCK.stop()
    #         drinkMMCK.stop()
    #         foodMMCK.stop()
    #         break
        
    
   
    for thread in threads:
        thread.join()
        
    for queue in [entranceMMCK, drinkMMCK, foodMMCK]:
        queue.stats()
        print("-------------------------------------------------")
        print("queueName=",queue.name, "\nstats:")
        print("avgWaitTime=", queue.avgWaitTime)
        print('awgWaitLen=', queue.avgWaitLen)
        print('avgWaitQuTime=', queue.avgWaitQuTime)
        print('avgWaitQuLen=', queue.avgWaitQuLen)
        print('totalServedCustomers=', queue.totalServedCustomers)
    print("-------------------------------------------------")
    # print('totalServedCustomers of the system: ')
    # for queue in [entranceMMCK, drinkMMCK, foodMMCK]:
    #     totalServedCustomers += queue.totalServedCustomers
    # print('totalServedCustomers=', totalServedCustomers)
