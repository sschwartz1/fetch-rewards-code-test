from similarity_scorer import SimilarityScorer

def main():
    text1 = "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."
    text2 = "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."
    text3 = "We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way."

    test1 = SimilarityScorer(text1, text2)
    test1.create_count_dict()
    score1 = test1.compare_texts()

    test2 = SimilarityScorer(text1, text3)
    test2.create_count_dict()
    score2 = test2.compare_texts()

    print(f'Text 1 and Text 2 similarity score: {score1}\nText 1 and Text 3 similarity score: {score2}')

if __name__ == '__main__':
    main()