class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged_addr = ""
        for i in range(len(address)):
            if address[i] == '.':
                defanged_addr += "[.]"
            else:
                defanged_addr += address[i]
        
        return defanged_addr
