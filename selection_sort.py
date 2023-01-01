    def select(self, my_list, i):
        return my_list[i]
    
    def selectionSort(self, my_list,n):
        for i in range(n - 1):
            min_index = i
            for j in range(i+1, n):
                if my_list[j] < my_list[min_index]:
                    min_index = j
            if i != min_index:
                temp = my_list[i]
                my_list[i] = my_list[min_index]
                my_list[min_index] = temp
        return my_list
