
class CalculateService:
    def get_scale(self, key):
        sclae = self.calculate_interval(self.get_temp_scale(key))
        return sclae

    def get_temp_scale(self, key):
        scale = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
        idx = scale.index(key)
        cnt = 0
        result = []

        while True:
            if cnt < len(scale):
                cnt += 1
            else:
                break

            result.append(scale[idx])

            if idx < len(scale) - 1:
                idx += 1
            else:
                idx = 0
        return result

    def calculate_interval(self, scale):
        interval = {'c' : 1, 'd' : 2, 'e' : 3, 'f' : 3.5, 'g' : 4.5, 'a' : 5.5, 'b' : 6.5}
        major_interval = [0, 1, 2, 2.5, 3.5, 4.5, 5.5]

        m_idx = 0
        key = interval[scale[0]]
        for k in interval.keys():
            if interval[k] < key:
                interval[k] += 6

        for s in scale:
            if major_interval[m_idx] > (interval[s] - key):
                scale[m_idx] = scale[m_idx] + '+'
            elif major_interval[m_idx] < (interval[s] - key):
                scale[m_idx] = scale[m_idx] + '-'
            m_idx += 1
        return scale