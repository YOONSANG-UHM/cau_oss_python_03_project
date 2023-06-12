#%%
class parking_spot:
    __item = {}

    # you have to implement 'constructor(생성자)' and 'get' method
    def __init__(self, name, city, distict, ptype, \
                 longitude, latitude):
        self.__item = \
            {
             'name':name,
             'city':city,
             'district':distict,
             'ptype':ptype,
             'longitude':float(longitude),
             'latitude':float(latitude)
            }
             
        
    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s

    def get(self, keyword='name'):
        return self.__item[keyword]
    
def str_list_to_class_list(str_list):
    list_parking_spot = []
    for i in str_list:
        list1 = i.split(",")
        value = parking_spot(list1[1], list1[2], list1[3], \
                         list1[4], list1[5], list1[6])
        list_parking_spot.append(value)
    return list_parking_spot
    
def print_spots(spots):
    print(f"---print elements({len(spots)})---")
    for a in spots:
        print(a)

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    import file_manager
    str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    spots = str_list_to_class_list(str_list)
    print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)
# %%