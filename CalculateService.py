# -*- coding: utf-8 -*-
from http import HTTPStatus

class CalculateService:
    def get_scale(self, key):
        result = False
        try:
            # 입력 받은 key 유효성 검사
            key = self.check_key_validation(key)

            sclae = self.calculate_interval(self.get_temp_scale(key))
            result = sclae
        except Exception as e:
            print(e)
            result = False
            
        return result

    def check_key_validation(self, key):
        key_str_list = list(key.lower())
        # A~G, a ~ g, +, - 아스키 코드
        asck_list = [43, 45, 97, 98, 99, 100, 101, 102, 103]

        # key는 a ~ g 까지 알파벳과 +, -로 구성
        if len(key_str_list) > 2:
            raise Exception('The number of characters in the key must be 2 characters or less.')

        idx = 0
        for s in key_str_list:
            if not ord(s) in asck_list:
                raise Exception('Key must be a ~ g and +, -')
            if len(key_str_list) == 1 and (ord(s) == 43 or ord(s) == 45):
                raise Exception('Key must have a ~ g key.')
            if idx == 0 and (ord(s) == 43 or ord(s) == 45):
                raise Exception('Key order error')
            idx += 1
        return key.lower()
    # key를 기준으로 임시적인 음계 나열
    def get_temp_scale(self, key):
        scale = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
        key_idx = scale.index(key[0])

        cnt = 0
        result = []

        while True:
            if cnt < 7:
                cnt += 1
            else:
                break

            result.append(scale[key_idx])

            if key_idx < 6:
                key_idx += 1
            else:
                key_idx = 0
        result[0] = key
        return result
    # 임시로 나열한 스케일에 정확한 음정 계산
    def calculate_interval(self, scale):
        interval = {'c' : 1.0, 'c+': 1.5, 'd' : 2.0, 'd+':2.5, 'e' : 3.0, 'e+' : 3.5, 'f' : 3.5
                 , 'f+' : 4.0, 'g' : 4.5, 'g+' : 5.0, 'a' : 5.5, 'a+': 6.0, 'b' : 6.5, 'b+' : 7.0}

        major_interval = [0, 1, 2, 2.5, 3.5, 4.5, 5.5]
        key_val = interval[scale[0]]
        
        # key 보다 값이 작으면 옥타브 증가
        for k in interval.keys():
            if interval[k] < key_val:
                interval[k] += 6
        
        key_num = 0
        for s in scale:
            interval_from_key = interval[s] - key_val
            # 기준 스케일 키 간격보다 좁다면 반음 올림
            if major_interval[key_num] > interval_from_key:
                scale[key_num] = scale[key_num] + '+'
                interval_from_key += 0.5
            # 기준 스케일 키 간격보다 넓다면 반음 내림
            elif major_interval[key_num] < interval_from_key:
                scale[key_num] = scale[key_num] + '-'
                interval_from_key -= 0.5

            # +이 붙은 스케일은 겹증(++)이 가능 하기에 2번까지 확인해야함
            # 기준 스케일 키 간격보다 좁다면 반음 올림
            if major_interval[key_num] > interval_from_key:
                scale[key_num] = scale[key_num] + '+'
            # 기준 스케일 키 간격보다 넓다면 반음 내림
            elif major_interval[key_num] < interval_from_key:
                scale[key_num] = scale[key_num] + '-'
            key_num += 1

        return scale
