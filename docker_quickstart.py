from instapy import InstaPy
from instapy.util import smart_run

# Write your automation here
# Stuck? Look at the github page https://github.com/InstaPy/instapy-quickstart

# ここにインスタグラムのログイン情報を入力する
insta_username = "navier_stokes_1120"
insta_password = "test1234"

bot = InstaPy(username=insta_username, password=insta_password, headless_browser=True)
with smart_run(bot):
    # フォローやlike等をする対象の範囲の設定
    # 例えば、max_followers, min_followersはそれぞれ最大・最小フォロワー数を意味し、フォロワー数がこの範囲にあるユーザーに対してフォローやlikeをする。
    # 特に条件を設ける場合はここのコメントアウトを外す。
    # bot.set_relationship_bounds(
    #     enabled=True,
    #     potency_ratio=-1.21,
    #     delimit_by_numbers=True,
    #     max_followers=200,
    #     max_following=200,
    #     min_followers=1,
    #     min_following=1,
    # )

    # 以下の場合、「カフェ」というハッシュタグの付いた投稿をしているユーザーを10人フォローする。
    # 但し、set_ralationship_boundsの設定によっては10人以下になる可能性がある。
    bot.follow_by_tags(['カフェ'], amount=10)

    # コメントの設定（コメントしたくないならTrueをFalseに変える）
    bot.set_do_comment(True, percentage=10)
    bot.set_comments(["Cool!", "Awesome!", "Nice!"])

    # 以下の場合、「dog」や「#cat」が入った投稿をlikeする
    bot.like_by_tags(["dog", "#cat"], amount=100)

    bot.end()
