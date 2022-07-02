from Mean_Variance_Standard_Deviation_Calculator import free_code_comp


if __name__ == '__main__':
    obj = free_code_comp([])

    [print(key,':',value) for key, value in obj.by_default().items()]

    click = input('\n If you want to try custom list, click on Enter: ')
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