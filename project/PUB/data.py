from sklearn.datasets import fetch_20newsgroups

class Data:
    def __init__(self):

        self.interesting_categories = [
            'alt.atheism',
            'comp.graphics',
            'comp.os.ms-windows.misc',
            'comp.sys.ibm.pc.hardware',
            'comp.sys.mac.hardware',
            'comp.windows.x',
            'misc.forsale',
            'rec.autos',
            'rec.motorcycles',
            'rec.sport.baseball'
        ]
        print("finsih 1")
        self.not_interesting_categories = [
            'rec.sport.hockey',
            'sci.crypt',
            'sci.electronics',
            'sci.med',
            'sci.space',
            'soc.religion.christian',
            'talk.politics.guns',
            'talk.politics.mideast',
            'talk.politics.misc',
            'talk.religion.misc'
        ]
        print("finsih 2")

    def data_loader_interesting(self):
        newsgroups_interesting = fetch_20newsgroups(
            subset='all',
            categories=self.interesting_categories
        )
        category_dict = {name: [] for name in newsgroups_interesting.target_names}
        for text, label in zip(newsgroups_interesting.data, newsgroups_interesting.target):
            category_name = newsgroups_interesting.target_names[label]
            category_dict[category_name].append(text)

        return category_dict


    def data_loader_not_interesting(self):
        newsgroups_not_interesting = fetch_20newsgroups(
            subset='all',
            categories=self.not_interesting_categories
        )
        category_dict = {name: [] for name in newsgroups_not_interesting.target_names}
        for text, label in zip(newsgroups_not_interesting.data, newsgroups_not_interesting.target):
            category_name = newsgroups_not_interesting.target_names[label]
            category_dict[category_name].append(text)

        return category_dict
#
# d=Data()
# dw=d.data_loader_interesting()
# print(dw['comp.graphics'][2])
# de=d.data_loader_not_interesting().data
#
# category_dict = {name: [] for name in dw.target_names}
# for text, label in zip(dw.data, dw.target):
#     category_name = dw.target_names[label]
#     category_dict[category_name].append(text)

# r=0
# print(type(dw))
# for i in dw:
#     r+=1
#     print(r)
# r=0
# for i in de:
#     r+=1
#     print(i)
#     print(r)