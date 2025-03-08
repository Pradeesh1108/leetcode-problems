class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if len(blocks) > 100:
            return 0
        if k == len(blocks):
            return blocks.count("W")
        mini = float('inf')
        for i in range(len(blocks)-k+1):
            mini = min(mini,blocks[i:i+k].count('W'))
        return mini

        
