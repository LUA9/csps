import json
import requests
import fake_useragent
from . import implemention

class TimeTable:
    user_agent = fake_useragent.UserAgent().random
    def __init__(self):
        self.session = requests.Session()
        response = requests.get(
            'http://comci.kr:4082/st',
            headers={
                'User-Agent': self.user_agent,
            },
        )
        response.raise_for_status()
        text = response.text
        try:
            school_ra_index = text.index('school_ra(sc)')
            sc_data_index = text.index('sc_data(\'')
        except:
            raise AttributeError('comsigan_parser.__init__:13: 소스에서 식별 코드를 찾을 수 없습니다.')

        school_ra = implemention.substr(text, school_ra_index, 50)
        school_ra = school_ra.strip()
        school_ra = implemention.match_school_ra(school_ra)

        sc_data = implemention.substr(text, sc_data_index, 30)
        if not sc_data:
            raise AttributeError('comsigan_parser.__init__:21: 소스에서 식별 코드를 찾을 수 없습니다.')
        sc_data = sc_data.strip()
        sc_data = implemention.match_sc_data(sc_data)
        sc_data = implemention.resolve_sc_data(sc_data[0])
        
        self.school_ra, self.sc_data = school_ra, sc_data
    
    def SetSchool(self, school: str):
        buffer = school.encode('euc-kr', 'ignore')
        hex_buffer = buffer.hex('%')
        hex_buffer = hex_buffer.upper()
        print(f'http://comci.kr:4082{self.school_ra[1]}%{hex_buffer}')
        response = requests.get(
            f'http://comci.kr:4082{self.school_ra[1]}%{hex_buffer}',
            headers={
                'User-Agent': self.user_agent,
            },
        )
        text = response.text
        body = implemention.substr(text, 0, implemention.last_index_of(text, '}') + 1)
        body = json.loads(body)
        print(implemention.decode_json(body))
