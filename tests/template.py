from potentiostat import Potentiostat
import matplotlib.pyplot as plt

port = 'COM3'
datafile = ["cyclic.txt", "sinusoid.txt","constant.txt","squareWave.txt","linearSweep.txt","chronoamp.txt","multiStep.txt"]

test_name = ["cyclic", "sinusoid","constant","squareWave","linearSweep","chronoamp","multiStep"]
curr_range = '100uA'        
sample_rate = 100.0         
int_test = int(input("номер теста: "))
# All Tests
# ["cyclic","sinusoid","constant","squareWave","linearSweep","chronoamp","multiStep"]
test_data = [
# Cyclic Test Data
        {
            'quietValue' : -0.1,   # quiet period voltage (V)
            'quietTime'  : 1000,   # quiet period duration (ms)
            'amplitude'  :  0.6,   # waveform peak amplitude (V)
            'offset'     :  0.5,   # waveform offset (V)
            'period'     : 2000,   # waveform period (ms)
            'numCycles'  :    4,   # number of cycles
            'shift'      :  0.0,   # unitless phase shift
        },

# Sinusoid Test Data
        {
            'quietValue' : 0.0,
            'quietTime'  : 0,
            'amplitude'  : 2.0,
            'offset'     : 0.0,
            'period'     : 2000,
            'numCycles'  : 3,
            'shift'      : 0.0,
        },

# Constant Test Data
        {
            'quietValue' : 0.0,
            'quietTime'  : 2000,
            'value'      : 0.7,
            'duration'   : 8000,
        },

# squareWave Test Data
        {
            'quietValue' : -0.4,
            'quietTime'  :  500,
            'amplitude'  :  0.05,
            'startValue' : -0.4,
            'finalValue' :  0.2,
            'stepValue'  :  0.005,
            'window'     :  0.3,
        },

# linearSweep Test Data
        {
            'quietTime'  : 2000,   # quiet period voltage (V)
            'quietValue' :  0.0,   # quiet period duration (ms)
            'startValue' : -0.8,   # linear sweep starting value (V)
            'finalValue' :  1.2,   # linear sweep final value (V)
            'duration'   : 8000,   # linear sweep duration (ms)
        },

# Chronoamp Test Data
        {
            'quietValue' : 0.0,
            'quietTime'  : 1000,
            'step'       : [(1000,-0.25), (1000,0.5)],
        },

# Multistep Test Data
        {
            'quietValue' : 0.0,
            'quietTime'  : 1000,
            'step'       : [(1000,-0.5), (1000,-0.2), (1000,-0.3), (1000,-0.0), (1000,-0.1), (1000,0.3), (1000,0.2), (1000, 0.5)],
        },
]


cpp = Potentiostat(port)     
cpp.set_curr_range(curr_range)   
cpp.set_sample_rate(sample_rate)
print(test_name[int_test],test_data[int_test])
cpp.set_param(test_name[int_test],test_data[int_test])


t,volt,curr = cpp.run_test(test_name[int_test],display='pbar')
file = open(datafile[int_test], 'w')
file.write('Time \n' + str(t) + '\n'+ 'Volt \n' + str(volt) + '\n' 'Curr \n'+ str(curr) + '\n')
plt.figure(1)
plt.subplot(211)
plt.plot(t,volt)
plt.ylabel('potential (V)')
plt.grid('on')

plt.subplot(212)
plt.plot(t,curr)
plt.ylabel('current (uA)')
plt.xlabel('time (sec)')
plt.grid('on')

plt.figure(2)
plt.plot(volt,curr)
plt.xlabel('potential (V)')
plt.ylabel('current (uA)')
plt.grid('on')

plt.show()