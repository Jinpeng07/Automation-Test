# # import json
# # with open("data.json","r",encoding='utf8') as f:
# #     d=json.load(f)
# #
# # print(d)
# # print(type(d))
# #
# # #注意,这里要单包双,不能双包单
# # mystr='{"ID":1,"name":"maker"}'
# # d2=json.loads(mystr)
# # print(d2)
# # print(type(d2))
# import yaml
# mydata={
#     "id": 1,
#     "地区": "深圳",
#     "data": [{
#         "id": 1,
#         "名字": "南山区"
#         },
#         {
#          "id": 2,
#         "名字": "福田区"
#         },
#         {
#         "id": 3,
#         "名字": "光明区"
#         }]
# }
#
# mydata2={
#     "id": 2,
#     "地区": "深圳",
#     "data": [{
#         "id": 1,
#         "名字": "南山区"
#         },
#         {
#          "id": 2,
#         "名字": "福田区"
#         },
#         {
#         "id": 3,
#         "名字": "光明区"
#         }]
# }
# with open("1.yaml",'w',encoding='utf8') as f:
#     yaml.dump_all(documents=[mydata,mydata2],stream=f,allow_unicode=True)
import yaml

with open("1.yaml",'r',encoding='utf8') as f:
    res=yaml.load_all(f.read(),Loader=yaml.FullLoader)
    print(res)
    for r in res:
        print(r)
