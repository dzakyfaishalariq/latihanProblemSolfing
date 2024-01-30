def cannons_ready(gunners):
    lis_ada = []
    for key, value in gunners.items():
        lis_ada.append(value)
    if "nay" in lis_ada:
        return 'Shiver me timbers!'
    else:
        return "Fire!"

print(cannons_ready({'Mike':'aye','Joe':'aye','Johnson':'aye','Peter':'aye'}))