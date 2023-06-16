#%%
"""
데이터 처리와 관련된 클래스와 함수를 구현해놓은 모듈입니다.
parking_spot이라는 이름의 클래스와
함수 str_list_to_class_list, print_spots, filter_by_name,
filter_by_city, filter_by_district, filter_by_ptype,
filter_by_location, sort_by_keyword를 포함합니다.
"""
class parking_spot:
    """
    parking_spot class는 2023 설날 무료주차장에 대한
    정보를 제공합니다.
    변수로는 외부에서 접근 불가능한 __item라는 이름의
    dictionary가 있으며 접근하기 위하여 get 메소드를 제공합니다.
    """
    __item = {}

    def __init__(self, name, city, distict, ptype, \
                 longitude, latitude):
        """ 생성자 초기 name, city, district, ptype,
            longitude, latitude값을 받습니다.
        Args:
            name(str): 주차장의 이름
            city(str): 주차장이 속한 도시(도, 광역시, 특별시)
            district(str): 주차장이 속한 도시의 구역(시, 군, 구)
            ptype(str): 주차장의 종류(노상, 노외, 부설)
            longitude(str): 주차장 위치의 경도
            latitude(str): 주차장 위치의 위도
        """
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
        """ 클래스를 문자로 변환할 때 수행될 내용입니다.
        Returns:
            str: 객체의 딕셔너리의 값들을
                 하나의 문자열로 반환합니다.
        """
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s

    def get(self, keyword='name'):
        """ keyword를 받아 객체의 딕셔너리의 값을 반환합니다.
        Args:
            keyword(str): 반환할 키의 키워드이며
            'name'이 디폴트입니다.
        """
        return self.__item[keyword]
    
def str_list_to_class_list(str_list):
    """ 주차장의 정보들이 문자열로 담긴 리스트를 받아
        parking_spot 클래스로 구성된 리스트로 반환합니다.
    Args:
        str_list(list): 주차장의 정보들이 문자열로 담긴 list
    Returns:
        list: parking_spot 클래스로 구성된 리스트
    """
    list_parking_spot = []
    for i in str_list:
        list1 = i.split(",")
        value = parking_spot(list1[1], list1[2], list1[3], \
                         list1[4], list1[5], list1[6])
        list_parking_spot.append(value)
    return list_parking_spot
    
def print_spots(spots):
    """ parking_spot 클래스로 구성된 리스트를 받아
        그 정보를 출력합니다.
    Args:
        spots(list): parking_spot 클래스로 구성된 리스트
    """
    print(f"---print elements({len(spots)})---")
    for a in spots:
        print(a)

def filter_by_name(spots, name):
    """ parking_spot 클래스로 구성된 리스트와 주차장 이름을 받아
        그 이름이 들어간 주차장들만 필터링하여 리스트로 반환합니다.
    Args:
        spots(list): parking_spot 클래스로 구성된 리스트
        name(str): 필터링의 기준이 되는 주차장 이름
    Returns:
        list: 필터링 후의 리스트를 반환합니다.
    """
    list_name = [a for a in spots if name in a.get('name')]
    return list_name

def filter_by_city(spots, city):
    """ parking_spot 클래스로 구성된 리스트와 도시 이름을 받아
    그 이름이 들어간 도시의 주차장들만 필터링하여
    리스트로 반환합니다.
    Args:
        spots(list): parking_spot 클래스로 구성된 리스트
        city(str): 필터링의 기준이 되는 도시 이름
    Returns:
        list: 필터링 후의 리스트를 반환합니다.
    """
    list_city = [a for a in spots if city in a.get('city')]
    return list_city

def filter_by_district(spots, district):
    """ parking_spot 클래스로 구성된 리스트와 도시 구역 이름을 받아
        그 이름이 들어간 주차장들만 필터링하여 리스트로 반환합니다.
    Args:
        spots(list): parking_spot 클래스로 구성된 리스트
        district(str): 필터링의 기준이 되는 도시 구역 이름
    Returns:
        list: 필터링 후의 리스트를 반환합니다.
    """
    list_district = [a for a in spots if \
                     district in a.get('district')]
    return list_district

def filter_by_ptype(spots, ptype):
    """ parking_spot 클래스로 구성된 리스트와 주차장 종류를 받아
        그 종류의 주차장들만 필터링하여 리스트로 반환합니다.
    Args:
        spots(list): parking_spot 클래스로 구성된 리스트
        ptype(str): 필터링의 기준이 되는 주차장 종류
    Returns:
        list: 필터링 후의 리스트를 반환합니다.
    """
    list_ptype = [a for a in spots if ptype in a.get('ptype')]
    return list_ptype

def filter_by_location(spots, tuple1):
    """ parking_spot 클래스로 구성된 리스트와 최소/최대
        위도/경도에 대한 튜플을 받아
        그 범위 안에 있는 주차장들만 필터링하여 리스트로 반환합니다.
    Args:
        spots(list): parking_spot 클래스로 구성된 리스트
        tuple1(tuple): 필터링의 기준이 되는 이름
    Returns:
        list: 필터링 후의 리스트를 반환합니다.
    """
    list_location = [a for a in spots if \
                     tuple1[0] < a.get('latitude') and \
                     tuple1[1] > a.get('latitude') and \
                     tuple1[2] < a.get('longitude') and \
                     tuple1[3] > a.get('longitude')]
    return list_location

def sort_by_keyword(spots, keyword):
    """ parking_spot 클래스로 구성된 리스트와 키워드를 받아
        키워드에 대하여 정렬한 리스트를 반환합니다.
    Args:
        spots(list): parking_spot 클래스로 구성된 리스트
        keyword(str): 정렬 기준이 되는 키워드
    Returns:
        list: 정렬 후의 리스트를 반환합니다.
    """
    list_sorted = sorted(spots, key=lambda x: x.get(keyword))
    return list_sorted

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.read_file("./input/free_parking_spot.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)
# %%