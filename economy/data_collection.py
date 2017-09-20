f = open("data.txt", 'w')

import consumer_tester
f.write("CLASSICAL CONSUMER: " + str(consumer_tester.classical_list) + '\n')
f.write("SIMULATOR CONSUMER: " + str(consumer_tester.simulator_list) + '\n')

import producer_tester
f.write("CLASSICAL PRODUCER: " + str(producer_tester.classical_list) + '\n')
f.write("SIMULATOR PRODUCER: " + str(producer_tester.simulator_list) + '\n')

import market_tester
f.write("CLASSICAL MARKET: " + str(market_tester.classical_list) + '\n')
f.write("SIMULATOR MARKET: " + str(market_tester.simulator_list) + '\n')

f.close()
