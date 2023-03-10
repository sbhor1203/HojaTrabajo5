# Audrey Samatha Bhor López
# Hoja de trabajo 5
# python 3.10.4
# última modificación 10-3-2023




import simpy
import random
import statistics




## estos se usan para el proceso del cpu y ram en el programa
# %s → String formating
# %d → truncate floating
# %f → float reference

##class Memory: # clase contenedora de función completa

def Memory(selram, time,ramQty, speedT, cpuInstructions):
        
        global Ttimes, total ### variables globales para uso 

        global env, ram, cpu, wait
        

        env = simpy.Environment()
        ram = simpy.Container(env, init=100, capacity=100)
        cpu = simpy.Resource(env, capacity=1)
        wait = simpy.Resource(env, capacity=1)

        random.seed(10) ## cantidad defecto


        

        # status system 

        # %s → String formating
        # %d → truncate floating
        # %f → float reference


        yield env.timeout(time)
        print("The %s needs %d quantity of RAM" % (selram, ramQty)) # módulo de la operación (%)
        total = env.now

        endIstruct = 0 ## contador en 0


        print("The %s will do a total of %d instructions in the CPU." % (selram, cpuInstructions))

        while endIstruct < cpuInstructions:
            with cpu.request() as cpuRequest:
                yield cpuRequest

                # Calculates the number of instructions the CPU will do per clock cycle for the process
                if (cpuInstructions - endIstruct) >= speedT:
                    new_velocity = speedT

                else:
                    new_velocity = (cpuInstructions - endIstruct)

                print("The %s will do %d instructions in the CPU per clock cycle." % (selram, new_velocity))
                yield env.timeout(new_velocity / speedT)

                endIstruct += new_velocity
                print("The %s has completed %d of %f instructions" % (selram, endIstruct, cpuInstructions))

            
            timelaps = random.randint(1, 2)  # time comparation parameters

            if (timelaps == 1) and (endIstruct < cpuInstructions):

                with wait.request() as queuetime:
                    yield queuetime
                    yield env.timeout(1)
                    print("The %s has completed I/O operations" % selram)

        ram.put(ramQty)
        print("The %s returns %f of RAM memory" % (selram, ramQty))
        Ttimes+= (env.now - total) # average time
        elapsed_times.append(Ttimes)

Ttimes = 0
elapsed_times = []

for i in range(100):
    ramQty = random.randint(1, 10)
    cpuInstructions = random.randint(1, 10)
    env.process(Memory(env, "Process %s" % i , random.expovariate(1.0 / 10.0), ram, ramQty, cpuInstructions, 3))

env.run()
restantI = statistics.stdev(elapsed_times) ## rest
proccesingRun = statistics.mean(elapsed_times)
#####################################################################finalresult#################################################
print("Process succesfully completed at time: ", proccesingRun)
print("")
print("Restant instructions: ", restantI)




   