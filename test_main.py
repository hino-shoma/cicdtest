import pytest
from main import validate_username

def test_fail_case():
    # 本当は ValueError が起きるはずなのに、
    # あえて「エラーが起きないこと」を期待するテストを書くと失敗します
    assert validate_username("テスト") == True