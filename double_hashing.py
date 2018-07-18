DEFINE_TABLE_SIZE = 13
DEFINE_PRIME = 7

class DoubleHash:

    hashTable = [-1]*DEFINE_TABLE_SIZE
    curr_size = 0

#    def __init__(self):
#        self.hashTable = hashTable
#        self.curr_size = curr_size
        
    def isFull(self):
        return (self.curr_size == DEFINE_TABLE_SIZE)

    def hash1(self, key):
        return (key%DEFINE_TABLE_SIZE)

    def hash2(self, key):
        return (DEFINE_PRIME - key%DEFINE_PRIME)

    def insertHash(self, key):
        if(self.isFull()):
            return 
        index1 = self.hash1(key)
        if self.hashTable[index1] != -1:
            index2 = self.hash2(key)
            i = 1
            while(1):
                newIndex = (index1+i*index2)%DEFINE_TABLE_SIZE
                if self.hashTable[newIndex] == -1:
                    self.hashTable[newIndex] = key
                    break
                i+=1
        else:
            self.hashTable[index1] = key
        self.curr_size+=1

    def displayHash(self):
        for i in range(DEFINE_TABLE_SIZE):
            if self.hashTable[i] != -1:
                print(i,"-->", self.hashTable[i], sep=' ')
            else:
                print(i)

def main():
    a = [19,27,36,10,64]
    n = len(a)
    h = DoubleHash()
    for i in range(n):
        h.insertHash(a[i])
    h.displayHash()


if __name__ == "__main__":
    main()

