import numpy as np


class free_code_comp:

    def __init__(self, lists):
        self.lists = lists


    def calcul(self):
        means = [(self.lists.mean(axis=0).tolist()),
            (self.lists.mean(axis=1).tolist()),
            (self.lists.flatten().mean())]

        Variance = [(self.lists.var(axis=0).tolist()),
            (self.lists.var(axis=1).tolist()),
            (self.lists.flatten().var())]

        std = [(self.lists.std(axis=0).tolist()),
            (self.lists.std(axis=1).tolist()),
            (self.lists.flatten().std())]

        max = [(self.lists.max(axis=0).tolist()), 
            (self.lists.max(axis=1).tolist()), 
            (self.lists.flatten().max())]

        min = [(self.lists.min(axis=0).tolist()), 
            (self.lists.min(axis=1).tolist()), 
            (self.lists.flatten().min())]

        sum = [(self.lists.sum(axis=0).tolist()),
            (self.lists.sum(axis=1).tolist()),
            (self.lists.flatten().sum())]

        return {
            'Means: ' : means,
            'Variance: ' : Variance,
            'Standard Deviation: ': std,
            'Max: ' : max,
            'Min: ' : min,
            'Sum: ' : sum,
        }

    def stats(self):
        
        if len(self.lists) != 9:
            raise ValueError('List must contain nine numbers.')
        else:
            self.lists = np.array(obj.lists).reshape(3, 3)
            return self.calcul()
    
    def by_default(self):
        self.lists = np.array([0,1,2,3,4,5,6,7,8]).reshape(3, 3)
        return self.calcul()
    
if __name__ == '__main__':
    obj = free_code_camp([])

    [print(key,':',value) for key, value in obj.by_default().items()]

    click = input('\n If you want to try custom list, click on Enter')
    if click == '':
        print('Enter a list of 9 degits: \n')
        i = 1
        obj.lists = list()

        while True:

            obj.lists.append(int(input('{}-Degit number: '.format(i))))
            enter = input('Do you want to enter degits, if no click space')
            i += 1

            if enter == ' ':
                print(' Thank you for passing the list below: \n {}'.format(obj.lists))
                break
        
        [print(key,':',value) for key, value in obj.stats().items()]