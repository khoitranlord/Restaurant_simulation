import random
from customer import *

class CustomerEvent:
    def __init__(self, arrivalRate = 1):
        self.event = None
        self.arrivalRate = arrivalRate
        self.eventList = []
    # def generate(self, customerNum):
    #     if customerNum < 1:
    #         return
    #     self.eventList = [Customer(0)]   
    #     for i in range(self.customerNum + 1):
    #         # Generate a new customer arrival time
    #         arrivalTime = int(random.expovariate(1/self.arrivalRate)*60)
    #         # Create a new customer
    #         self.eventList.append(Customer(arrivalTime + self.eventList[i].arrivalTime, CustomerStatus.ARRIVAL))
    
    
    #Generate a list of customers with a given number of customers        
    def numGenerate(self, customerNum, arrivalTime = 0):
        if customerNum < 1:
            return
        self.eventList.append(Customer(arrivalTime))   
        for i in range(customerNum + 1):
            # Generate a new customer arrival time
            arrivalTime = int(random.expovariate(1/self.arrivalRate)*60)
            # Create a new customer
            self.eventList.append(Customer(arrivalTime + self.eventList[i].arrivalTime, CustomerStatus.ARRIVAL))

    #Generate a list of customers with a given simulation time
    def timeGenerate(self, simulationTime, arrivalTime = 0):
        self.eventList.append(Customer(arrivalTime))
        while True:
            # Create a new customer
            if (self.eventList[-1].arrivalTime < simulationTime):
                arrivalTime = int(random.expovariate(1/self.arrivalRate)*60)
                self.eventList.append(Customer(arrivalTime + self.eventList[-1].arrivalTime, CustomerStatus.ARRIVAL))
            else:
                break
                
    def addCustomerEvent(self, event):
        if len(self.eventList) == 0:
            self.eventList.append(event)
        else:        
            i = 0
            for i in range(len(self.eventList)+1):
                if len(self.eventList) == i:
                    break
                if self.eventList[i].arrivalTime > event.arrivalTime:
                    break
            
            self.eventList.insert(i, event)
    
    def printList(self):
        print('\n=======printList======')
        for i in range(len(self.eventList)):
            print('\narrival=', self.eventList[i].arrivalTime, 'event=', self.eventList[i].CustomerStatus)
        
        
        


# We will simulate the system for a given time period. The system will have 3 queues (entrances, food, drink), each with its own arrival rate, service rate, and capacity.