import json
from unicode_codepoints import transform
def test_transform():
    value='A'
    if True: result=transform(value)
    else: result=transform(json.loads(value))
    assert 'U+0041' in json.dumps(result,ensure_ascii=False)
