class Saver:

    def __init__(self,filename):
        self.filename = filename


    def saveSolution(self,cost,couriers):
        
        with open(self.filename, 'a') as file:
            file.write(f'Total Cost of Deliveries {cost}\n')
            
            for courier in couriers:
                file.write('\n' + str(courier) + '\n')
            
            file.close()