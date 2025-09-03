class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for _ in range(self.MAX)] 

    def get_hash(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.MAX

    def __getitem__(self, key):
        hash_index = self.get_hash(key)
        for k, v in self.arr[hash_index]:
            if k == key:
                return v
        raise KeyError(f"Key '{key}' not found in HashTable")

    def __setitem__(self, key, value):
        hash_index = self.get_hash(key)
        found = False
        for idx, (k, v) in enumerate(self.arr[hash_index]):
            if k == key:
                self.arr[hash_index][idx] = (key, value)
                found = True
                break
        
        if not found:
            self.arr[hash_index].append((key, value))

    def del_item(self, key):
        hash_index = self.get_hash(key)
        for idx, (k, v) in enumerate(self.arr[hash_index]):
            if k == key:
                del self.arr[hash_index][idx]
                return 
        print(f"Key '{key}' not found, cannot delete.")

t = HashTable()

t["Apple"] = 100
t["Banana"] = 200
t["Grapes"] = 300
t["Orange"] = 400
t["Mango"] = 500
t["Cherry"] = 600
t["Elppa"] = 700 
t["ppleA"] = 800
print(f"Value for 'Apple': {t['Apple']}")
print(f"Value for 'Banana': {t['Banana']}")
print(f"Value for 'Grapes': {t['Grapes']}")
print(f"Value for 'Orange': {t['Orange']}")
print(f"Value for 'Mango': {t['Mango']}")
print(f"Value for 'Cherry': {t['Cherry']}")
print(f"Value for 'Elppa': {t['Elppa']}")
print(f"Value for 'ppleA': {t['ppleA']}")


t.del_item("Grapes")

t.del_item("Watermelon")

t["Apple"] = 1000
print(f"New Value for 'Apple': {t['Apple']}")





'''''class HashTable:
    def __init__(self):
        self.MAX=10
        self.l1=[[] for i in range(self.MAX)]
    def get_hash(self, key):
        hash =0
        for char in key:
            hash +=ord(char)
        return hash%self.MAX
    def __getitem__(self,key):
        l1_index = self.get_hash(key)
        for k in self.l1[l1_index]:
            if k[0]==key:
                return k[1]
        h=self.get_hash(index)
        return self.l1[h]
    def __setitem__(self,key,value):
        h=self.get_hash(key)
        found=False
        for idx,element in enumerate(self.l1[h]):
            if len(element)==2 and element[0]==key:
                self.arr[n][idx]=(key,value)
                found=True
        if not found:
            self.l1[h].append((key,value))
        self.l1[h]=value
    def del_item(self,key):
        h=self.get_hash(key)
        for index,kv in enumerate(self.l1[h]):
            if kv[0]==key:
                print("Deleted_index",index)
                del self.l1[h][index]
        self.l1[h]=None
t=HashTable()
t["Apple"] = 100
t["Banana"] = 200
t["Grapes"] = 300
t["Orange"] = 400
t["Mango"] = 500
t["Cherry"] = 600


print(f"Value for 'Apple': {t['Apple']}")
print(f"Value for 'Banana': {t['Banana']}")
print(f"Value for 'Grapes': {t['Grapes']}")
print(f"Value for 'Orange': {t['Orange']}")
print(f"Value for 'Mango': {t['Mango']}")
print(f"Value for 'Cherry': {t['Cherry']}")

print(f"Value for 'Pineapple': {t['Pineapple']}")

t.del_item("Grapes")
print(f"Value for 'Grapes' after deletion: {t['Grapes']}")

'''''