# fucntion
def main(lst):
    print ('The list in the array is : ', lst)
    lst.append(4)
    return lst


list1 = [1, 2, 3]
list2 = main(list1)
print('The List after passed returned from an array is : ', list2)

