import numpy as np
from scipy.stats import pearsonr
from ..models import Post, AppUser

def recommend_user(request_user, n=5):
    #リクエストユーザー以外の最終ログイン日時が最新１００人のユーザー（以下、対象ユーザー）を取得
    others = AppUser.objects.exclude(pk=request_user).order_by('-last_login')[:100]

    #リクエストユーザーが評価したアイテムのアイテム名と評価値の組み合わせを辞書に保存
    req_user_post = request_user.post_set.all()
    req_user_item = {p.item:p.rating for p in req_user_post}

    similarity = []

    #類似度を計算する対象ユーザーのループを回す
    for other in others:

        #対象ユーザーが評価したアイテムのアイテム名と評価値の組み合わせを辞書に保存
        other_post = other.post_set.all()
        other_item = {p.item:p.rating for p in other_post}

        #リクエストユーザーと対象ユーザーが評価したアイテムの積集合（以下、共通アイテム）を作成
        item_set = req_user_item.keys() & other_item.keys()

        #共通アイテムが２つ以上の時のみ類似度の計算を行う
        if len(item_set) > 1:

            #共通アイテムの評価値を保存するnumpy配列を作成
            req_user_rating = np.zeros(len(item_set))
            other_rating = np.zeros(len(item_set))

            for id,item in enumerate(item_set):
                req_user_rating[id] = req_user_item[item]
                other_rating[id] = other_item[item]

            #scipyのpearsonrモジュールによりユーザー間の類似度を計算
            sim = pearsonr(req_user_rating,other_rating)[0]

            similarity.append((sim, other))
    #類似度をキーとしたソートを行う
    similarity = sorted(similarity, key=lambda tup: tup[0], reverse = True)
    rank_user = [name for sim,name in similarity]

    print(similarity)


    #類似度の高い順になっているユーザー名のリストを返す
    return rank_user[:n]