class Solution:
    def defangIPaddr(self, address: str) -> str:
        for i in range(0,len(address) + 1):
            if address [i] == ".":
              return address.replace(".", "[.]")
