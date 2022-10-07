from pymagnitude import Magnitude, MagnitudeUtils

# ダウンロード
# デフォルトのダウンロード先: `~/.magnitude/`
vectors = Magnitude(MagnitudeUtils.download_model("chive-1.2-mc90", remote_path="https://sudachi.s3-ap-northeast-1.amazonaws.com/chive/"))

# リモートでのロード
# 下記例は300MBのベクトル、検証環境で1分弱
# vectors = Magnitude("https://sudachi.s3-ap-northeast-1.amazonaws.com/chive/chive-1.1-mc90-aunit.magnitude")

# リモートでのストリーム
# ローカルにファイルをダウンロードせず、ベクトルをすばやく取得
# vectors = Magnitude("https://sudachi.s3-ap-northeast-1.amazonaws.com/chive/chive-1.1-mc90-aunit.magnitude", stream=True)

print(vectors.query("徳島"))