def is_valid_walk(walk):
    if len(walk) > 10 or len(walk) < 10:
        return False
    elif len(walk) == 10:
        walk_bantu = walk
        walk = ''.join(walk)
        set_v = list(set(walk))
        for i in range(len(walk_bantu)):
            pass
        
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))