class TopKByHeap(object):
    __k=0
    __topk=None
    __bigdata=None

    def __init__(self,bigdata,k):
        self.__bigdata = bigdata
        self.__k = k
        self.__topk = self.__bigdata[:k]

    """
    set top k
    """
    def setTopK(self,topk):
        self.__topk=topk


    """
    left child for i index
    """
    def __left(self,i):
        return 2*i+1

    """
    right child for i index
    """
    def __right(self,i):
        return 2*i+2

    """
    swap two elements
    i,j shows index
    """
    def __swap(self,i,j):
        temp = self.__topk[i]
        self.__topk[i] = self.__topk[j]
        self.__topk[j] = temp

    """
    n: number of elements to build heap
    i: current index of element
    arr: elements to build heap
    """
    def  __buildHeap(self,i):
        while self.__left(i) <self.__k:
            leftIndex = self.__left(i)
            rightIndex = self.__right(i)
            if rightIndex<self.__k and \
                self.__topk[rightIndex] < self.__topk[leftIndex] and \
                self.__topk[rightIndex] < self.__topk[i]:
                    self.__swap(i,rightIndex)
            elif self.__topk[leftIndex] < self.__topk[i]:
                    self.__swap(i,leftIndex)
            else:
                break
            i = leftIndex

    """
    find top k
    """
    def findTopK(self):
        # build heap
        i = int(self.__k/2)-1
        while i>=0:
            self.__buildHeap(i)
            i-=1
        self.__print(1)
        # adjust heap
        nlen = len(self.__bigdata) # array length
        nbegIndex = self.__k
        printcnt=2
        while nbegIndex < nlen :
            if self.__bigdata[nbegIndex] < self.__topk[0]:
                nbegIndex+=1
                continue
            temp = self.__topk[0]
            self.__topk[0] = self.__bigdata[nbegIndex]
            self.__bigdata[nbegIndex] = temp

            self.__buildHeap(0)
            self.__print(printcnt)
            printcnt+=1
            nbegIndex+=1
        return self.__topk

    """
    print top k 
    """
    def __print(self,i):
        r = str(i)+'th: '
        for item in self.__topk:
            r+=str(item)+','
        print(r+'\r')


"""
test following
"""

topkheap = TopKByHeap(bigdata=[6,4,-9,10,3,2,14,5,6,4,3,2,6,5,444,665,4,3],k=5)
topk = topkheap.findTopK()