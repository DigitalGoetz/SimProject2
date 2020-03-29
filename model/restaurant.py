import simpy, numpy, random, time
class Sim(object):
    def nextArrival(self):
        # Exponential Variable with
        #   scale: 0.862052785924
        return round(numpy.random.exponential(0.862052785924), 4);

    def nextOrder(self):
        # LogNormal Variable with
        #   scale:  -0.5137166258214053
        #   shape:  0.799858597093
        return round(numpy.random.lognormal(-0.5137166258214053, 0.799858597093), 4)

    def nextPayment(self):
        # LogNormal Variable with
        #   scale:  -0.4903622325760071
        #   shape:  0.794724403708
        return round(numpy.random.lognormal(-0.4903622325760071, 0.794724403708), 4)

    def nextPickup(self):
        # Gamma Variable with
        #   shape:  1.0811523137
        #   scale:  0.8677960404637084
        return round(numpy.random.gamma(1.0811523137, 0.8677960404637084), 4)

    def formatTime(self, time):
        return "{:.2f}".format(time)

    def __init__(self, env):
        self.env = env
        self.orderstation = simpy.Resource(self.env, capacity=1)
        self.paymentqueue = simpy.Resource(self.env, capacity=2)
        self.paymentstation = simpy.Resource(self.env, capacity=1)
        self.pickupqueue = simpy.Resource(self.env, capacity=1)
        self.pickupstation = simpy.Resource(self.env, capacity=1)
        self.numberserved = 0
        self.customerId = 0

    def arrivals(self):
        while True:
            print(self.formatTime(self.env.now) + "\tCustomer " + str(self.customerId) + " arrives.")
            c = self.customer(self.customerId)
            self.customerId = self.customerId + 1
            self.env.process(c)
            yield self.env.timeout(self.nextArrival())
            
    def customer(self, id):
        with self.orderstation.request() as oReq:
            yield oReq 
            print(self.formatTime(self.env.now) + "\tCustomer " + str(id) + " starts ordering.")
            yield self.env.timeout(self.nextOrder())
            print(self.formatTime(self.env.now) + "\tCustomer " + str(id) + " completes ordering.")
            with self.paymentqueue.request() as payQReq:
                yield payQReq
                with self.paymentstation.request() as payReq:
                    yield payReq
                    print(self.formatTime(self.env.now) + "\tCustomer " + str(id) + " starts paying.")
                    yield self.env.timeout(self.nextPayment())
                    print(self.formatTime(self.env.now) + "\tCustomer " + str(id) + " completes paying.")
                    with self.pickupqueue.request() as pickQReq:
                        yield pickQReq
                        with self.pickupstation.request() as pickReq:
                            yield pickReq
                            print(self.formatTime(self.env.now) + "\tCustomer " + str(id) + " starts pickup.")
                            yield self.env.timeout(self.nextPickup())
                            print(self.formatTime(self.env.now) + "\tCustomer " + str(id) + " completes pickup.")
                            self.numberserved = self.numberserved + 1

    def report(self):
        return self.numberserved      

def run(minutesToRun):
    random.seed(int(round(time.time() * 1000)))
    env = simpy.Environment()
    env.process(Sim(env).arrivals())
    env.run(until=minutesToRun)

run(60)